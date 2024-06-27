import datetime, json, os, requests
from extensions import app, db
from models import LineStatus, LineDisruptions
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
# from flask import Flask, request, jsonify
load_dotenv()

disrupt_url = os.environ.get('TFL_URL_LINE_DISRUPTIONS')

    
"""
Create json file
"""
def create_json(x, filename):
  with open('data/'+filename+'.json', 'w') as filehandle:
    json.dump(x, filehandle)

"""
Open and load json data
"""
def open_json(filename):
  file_json = open('data/'+filename+'.json', 'r')
  data_json = json.load(file_json)
  return data_json

"""
Convert key names to lowercase letters
"""
# def keys_to_lowercase(obj):
#     if isinstance(obj, dict):
#         return {k.lower(): keys_to_lowercase(v) for k, v in obj.items()}
#     elif isinstance(obj, list):
#         return [keys_to_lowercase(item) for item in obj]
#     else:
#         return obj
    
def keys_to_lowercase_letters(obj):
    import re
    if isinstance(obj, dict):
        new_obj = {}
        for k, v in obj.items():
            # Convert key to lowercase and keep only letters
            new_key = re.sub(r'[^a-z]', '', k.lower())
            new_obj[new_key] = keys_to_lowercase_letters(v)
        return new_obj
    elif isinstance(obj, list):
        return [keys_to_lowercase_letters(item) for item in obj]
    else:
        return obj

"""
Create an ID for disruptions table
"""
def create_id_key(descript):
  return None

"""
Flattening the dictionary from line status data
"""
def flatten_dict(dict_data):
  return None

"""
Get line status
"""
def get_line_status_api(line_id):
  status_url = os.environ.get('TFL_URL_LINE_STATUS')
  tfl_api = os.environ.get('TEST_TFL_KEY')
  tfl_app_id = os.environ.get('APP_ID')
  tfl_headers = {'app_id': tfl_app_id, 'app_key': tfl_api}

  url_with_custom_id = status_url.format(ids=line_id)
  r = requests.get(url_with_custom_id, headers=tfl_headers)
  data_lower = keys_to_lowercase_letters(r.json())
  create_json(data_lower, 'line_status')
  print('Success data to json')
  # upload_data(r.json())

"""
Get line disruption data
"""
# Should call if line_status.disruption is not empty
# save up on API calls
def get_line_disrupt(api_url, line_id, tfl_headers):
  url_with_line_id = api_url.format(ids=line_id)
  r = requests.get(url_with_line_id, headers=tfl_headers)
  print(r.text)

"""
Upload data to database
"""
def upload_data(filename):
  line_status = open_json(filename)
  try:
    with app.app_context(): # Ensure the application context is pushed
      lineTable = db.session.query(LineStatus)
  except Exception as e:
    print(e)
    return 'Failure'
  
  try:
    # inspect module to get the columns of the table in database
    inspector = inspect(LineStatus)
    columns = [col.name for col in inspector.columns]

    # Dynamically set attributes if the key matches a column name in table
    for item in line_status:
      linedata = LineStatus()

      for column in columns:
        print(column)
        if column in item:
          print(item[column])
          setattr(linedata, column, item[column])
      linedata.lastupdate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

      if lineTable is not None:
        db.session.merge(linedata)
      else:
        db.session.add(linedata)
  except Exception as e:
    db.session.rollback()
    print(e)
    print('Failed to upload TFL Line Status Data')

  try:
    db.session.commit()
    print('Success')
    return 'Success'
  except Exception as e:
    db.session.rollback()
    print(e)
    print('Failed to upload')
    return str(e)
  finally:
    db.session.close()

"""
Format and create json file
"""
def open_format_json():
  line_status = open_json('line_status')
  data_lower = keys_to_lowercase_letters(line_status)
  create_json(data_lower, 'line_status_lower')
  with open('data/line_status_lower.json', 'w') as filehandle:
    json.dump(data_lower, filehandle)

"""
Get current status of line stored in db
"""
def get_status(line):
  line = line.lower()
  try:
    with app.app_context(): # Ensure the application context is pushed
      lineTable = db.session.query(LineStatus)
  except Exception as e:
    print(e)
    return 'Failure'
  try:
    if lineTable is not None:
      line_db = db.session.get(LineStatus, line)
      print(bool(line_db.disruptions))
      print(type(line_db.disruptions))

      if bool(line_db.disruptions):     
        disrupt_db = db.session.get(LineDisruptions, line)
        if disrupt_db is not None:
          affected_stops = disrupt_db.affectedstops.values()
      elif not line_db.disruptions:
        print('Empty dic')
      else:
        return None
    return line_db.disruptions
  except Exception as e:
    print(e)
    return 'Falied to get status'

# The `if` statement Checks if this script is being run as the main program,
# and so calls the functions below.
# If this script were imported then the functions called
# would not be executed automatically.
if __name__ == '__main__':
    with app.app_context():  # Push the application context to the main script
        get_status('dlr')
        # upload_data('line_status_lower')
        # open_format_json()