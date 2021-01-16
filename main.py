from flask import Flask, render_template, request, redirect, url_for 
from flask_socketio import SocketIO, send
import json
import requests
import geocoder
from time import gmtime, strftime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def home():
    return render_template("index.html")
	
@socketio.on('message')
def handleMessage(name, msg):
	g = geocoder.ip('me')

	timeStamp = str(strftime("%H:%M:%S", gmtime()))
	info = {
		"msg": msg, 
		"name": name, 
		"time": timeStamp, 
		"lat": g.lat, 
		"lng": g.lng
		}

	send(msg, broadcast=True)
	send(name, broadcast=True)
	send(timeStamp, broadcast=True)
	print(str(info))


@socketio.on('2')
def handleMessage2(msg):
	print("HI")

if __name__ == '__main__':
	socketio.run(app, debug=True)

