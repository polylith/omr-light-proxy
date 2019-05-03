from flask import Flask, jsonify, request
from flask_cors import CORS
import socket 
import os

app = Flask(__name__)
CORS(app)

TCP_IP = os.getenv('TCP_IP', '192.168.10.10')
TCP_PORT = os.getenv('TCP_PORT', 5000)

def send_message(message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(message.encode())
    s.close()

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