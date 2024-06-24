import json, psycopg2, os.path, os

def create_line_status_table():

  local_connect = open('data/connect.json', 'r')
  connects = json.load(local_connect)

  try:
    #establishing the connection
    conn = psycopg2.connect(
      database=connects[0]['database'], user=connects[0]['user'], password=connects[0]['password'], host=connects[0]['host'], port= connects[0]['port'])
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Executing an MYSQL function using the execute() method
    cursor.execute("DROP TABLE IF EXISTS LINE_STATUS, LINE_STATUS")

    #Creating table as per requirement
    commands= (
      """
      CREATE TABLE LINE_STATUS
        (
        id VARCHAR PRIMARY KEY,
        type VARCHAR,
        name VARCHAR,
        modeName VARCHAR,
        disruptions VARCHAR,
        created TIMESTAMP,
        modified TIMESTAMP,
        linestatuses JSON,
        routesections JSON,
        servicetypes JSON,
        crowding JSON,
        lastupdate TIMESTAMP
        )
      """
    )

    # for command in commands:
    cursor.execute(commands)
    print('Table created successfully......')
    conn.commit()
    #Closing the connection
    conn.close()
  except Exception as e:
    print(e)
    print('Table creation failed')
    conn.close()


"""
Create a tfl line disruptions datable table
"""
def create_disruptions_table():
  local_connect = open('data/connect.json', 'r')
  connects = json.load(local_connect)

  try:
    #establishing the connection
    conn = psycopg2.connect(
      database=connects[0]['database'], user=connects[0]['user'], password=connects[0]['password'], host=connects[0]['host'], port= connects[0]['port']
    )
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Executing an MYSQL function using the execute() method
    cursor.execute("DROP TABLE IF EXISTS LINE_DISRUPTIONS, LINE_DISRUPTIONS")

    #Creating table as per requirement
    commands= (
      """
      CREATE TABLE LINE_DISRUPTIONS
        (
        id VARCHAR PRIMARY KEY,
        type VARCHAR,
        category VARCHAR,
        categorydescription VARCHAR,
        description VARCHAR,
        affectedroutes JSON,
        affectedstops JSON,
        closuretext VARCHAR,
        lastupdated TIMESTAMP
        )
      """
    )

    # for command in commands:
    cursor.execute(commands)
    print('Table created successfully......')
    conn.commit()
    #Closing the connection
    conn.close()
  except Exception as e:
    print(e)
    print('Table creation failed')
    conn.close()



#----- Execute functions ------#
# create_disruptions_table()
# create_line_status_table()