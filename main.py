from flask import Flask, render_template, request, redirect, url_for 
from flask_socketio import SocketIO, send
import json
import requests
import geocoder


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def home():
    return render_template("index.html")
	
@socketio.on('message')
def handleMessage(msg):
	print("message")
	g = geocoder.ip('me')
	print(g.latlng)
	send(g.latlng, broadcast=True)
	send(msg, broadcast=True)


if __name__ == '__main__':
	socketio.run(app, debug=True)

#json with name, message, time.
# metadata: coordinates, 