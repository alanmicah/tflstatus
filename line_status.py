import os
from dotenv import load_dotenv
# from flask import Flask, request, jsonify
load_dotenv()

disrupt_url = os.environ.get('TFL_URL_DISRUPTIONS')

tfl_api = os.environ.get('TEST_TFL_KEY')
tfl_app_id = os.environ.get('APP_ID')
tfl_headers = {'app_id': tfl_app_id, 'app_key': tfl_api}
# print(disrupt_url)
def call_api(api_url, line_id, tfl_headers):
  import requests         
  url_with_custom_id = api_url.format(ids=line_id)
  # print(url_with_custom_id)
  r = requests.get(url_with_custom_id, headers=tfl_headers)
  # r.status_code
  # r.head['application/json']
  print(r.text)

# call_api(disrupt_url,'dlr', tfl_headers)