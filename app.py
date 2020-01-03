from flask import Flask, request, make_response, jsonify
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__)

data = []

@auth.get_password
def get_password(username):
    if username == 'username':
        return 'password'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.route('/', methods = ['GET'], defaults={'info':None})
@app.route('/<info>', methods = ['POST','GET'])
@auth.login_required
def input_data(info):
    global data
    if info:
        data.append(info)
    return jsonify(data)

if __name__ == '__main__':
    app.run()
