from flask import Flask, jsonify, request
from flask_cors import CORS
import socket 
import os

app = Flask(__name__)
CORS(app)

SOCKET_ENABLED = os.getenv('SOCKET_ENABLED', "True") == "True" 
SOCKET_IP = os.getenv('SOCKET_IP', '192.168.10.10')
SOCKET_PORT = os.getenv('SOCKET_PORT', 5000)

def send_message(message):
    if not SOCKET_ENABLED:
        app.logger.info('Socket disabled, but would have send message: %s', message)
        return

    app.logger.info('Try to connect to %s:%s', SOCKET_IP, SOCKET_PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SOCKET_IP, SOCKET_PORT))
    app.logger.info('Connected.')
    s.send(message.encode())
    app.logger.info('Send message %s', message)
    s.close()
    app.logger.info('Closed connection')

@app.route('/light', methods=['POST'])
def light():
    if request.method == 'POST':
        data = request.json

        state = data.get('state')
        if state:
            send_message(state)

        return jsonify({"state":state})


if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)