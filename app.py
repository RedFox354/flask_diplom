import sqlite3
from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import abort
import import_module as module
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    data = module.index()
    return render_template('index.html', data=data)

@app.route('/', methods=['POST'])
def process_data():
    ip_address = request.remote_addr
    data = request.get_json()
    module.process_data(data, ip_address)
    response = jsonify({'result': 'ok'})
    return response

@app.route('/<int:post_id>')
def post(post_id):
    post = module.get_data(post_id)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
