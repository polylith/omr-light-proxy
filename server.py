from flask import Flask, jsonify, request
import socket 
import os

app = Flask(__name__)

TCP_IP = os.getenv('TCP_IP', '127.0.0.1')
TCP_PORT = os.getenv('TCP_PORT', 5005)

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((TCP_IP, TCP_PORT))

@app.route('/light', methods=['POST'])
def light():
    if request.method == 'POST':
        data = request.json

        state = data.get('state')
        if state:
            print(state)
            # s.send(state)

        return jsonify({"state":state})


if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)