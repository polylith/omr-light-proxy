from flask import Flask, jsonify, request
from flask_cors import CORS
import socket 
import os

app = Flask(__name__)
CORS(app)

SOCKET_ENABLED = os.getenv('SOCKET_ENABLED', "True") == "True" 
SOCKET_IP = os.getenv('SOCKET_IP', '192.168.10.10')
SOCKET_PORT = int(os.getenv('SOCKET_PORT', 5000))

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

@app.route('/light/<message>', methods=['GET'])
def light(message):
    if request.method == 'GET':
        if message:
            send_message(message)

        return jsonify({"message":message})


if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)