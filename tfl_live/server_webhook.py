import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
load_dotenv()

app = Flask(__name__)

# Secret token for basic security
SECRET_TOKEN = os.environ.get('LOCAL_WEBHOOK_TOKEN')

@app.route('/webhook', methods=['POST'])
def webhook():
  #Check if the request contains a valid token
  token = request.headers.get('Authorization')
  if token != f"Bearer {SECRET_TOKEN}":
    return jsonify({'status': 'error', 'message': 'Unauthorized'}), 401

  # Handle invalid JSON
  if not request.is_json:
    return jsonify({'status': 'error', 'message': 'Invalid JSON'}), 400

  data = request.json
  # Example of required field validation
  if 'message' not in data or 'timestamp' not in data:
    return jsonify({'status': 'error', 'message': 'Missing fields'}), 400

  print(f"Received webhook data: {data}")
  return jsonify({'status': 'success', 'data': data}), 200

@app.errorhandler(404)
def page_not_found(e):
  return jsonify({'status': 'error', 'message': 'Not Found'}), 404

@app.errorhandler(500)
def internal_server_error(e):
  return jsonify({'status': 'error', 'message': 'Internal Server Error'}), 500

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050)