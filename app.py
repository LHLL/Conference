#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from Utility import Utility

app = Flask(__name__)

#API List:
#Test method to test if server is running
@app.route('/')
def index():
	return 'Hello World! Awesome! The Server is up running!!! Hail Hydra!!!'

#Help method to shut down server
@app.route('/shutdown', methods=['POST'])
def shutdown():
	shutdown_server()
	return 'shutdown'

#GET Token
@app.route('/token',methods=['POST'])
def generate_token():
	if not request.json or not 'identifier' in request.json:
			abort(400)
	name = request.json['identifier']
	room = request.json['roomName']
	uti = Utility(name,room)
	return jsonify({'accessToken':uti.generate_token().decode('utf-8')})
		

#Help Method
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

#Entrence
if __name__ == '__main__':
	#Replace host with your own IP!!!
	app.run(host='10.0.0.184')