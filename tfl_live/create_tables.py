"""
CreateTables.py created by Alan D 04/08/2022
"""

import json, psycopg2

"""
Create a tfl line status database table
"""
def create_line_status_table():

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
    cursor.execute("DROP TABLE IF EXISTS LINE_STATUS, LINE_STATUS")

    #Creating table as per requirement
    commands= (
      """
      CREATE TABLE LINE_STATUS
        (
        id VARCHAR PRIMARY KEY,
        name VARCHAR,
        modeName VARCHAR,
        disruptions VARCHAR,
        modified TIMESTAMP,
        created TIMESTAMP,
        lineStatuses VARCHAR,
        routeSections VARCHAR,
        serviceTypes VARCHAR,
        crowding VARCHAR,
        lastupdate TIMESTAMP,
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
        restoretime VARCHAR,
        information VARCHAR,
        starttime VARCHAR,
        reports INT,
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



#----- Execute functions ------#
create_disruptions_table()
create_line_status_table()