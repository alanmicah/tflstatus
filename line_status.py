import datetime, os, requests
from extensions import db
from models import LineStatus, LineDisruptions
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
# from flask import Flask, request, jsonify
load_dotenv()

disrupt_url = os.environ.get('TFL_URL_LINE_DISRUPTIONS')
status_url = os.environ.get('TFL_URL_LINE_STATUS')
tfl_api = os.environ.get('TEST_TFL_KEY')
tfl_app_id = os.environ.get('APP_ID')
tfl_headers = {'app_id': tfl_app_id, 'app_key': tfl_api}

def get_line_status(api_url, line_id, tfl_headers):
  url_with_custom_id = api_url.format(ids=line_id)
  # print(url_with_custom_id)
  r = requests.get(url_with_custom_id, headers=tfl_headers)
  # r.status_code
  # r.head['application/json']
  print(r.text)

def get_line_disrupt(api_url, line_id, tfl_headers):
  url_with_line_id = api_url.format(ids=line_id)
  r = requests.get(url_with_line_id, headers=tfl_headers)
  print(r.text)


def upload_data(line_status):
  try:
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
        if column in item:
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


# get_line_status(status_url,'dlr', tfl_headers)
# get_line_disrupt(disrupt_url,'dlr', tfl_headers)