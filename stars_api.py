from flask import Flask , jsonify , request
from data import data

app = Flask(__name__)

@app.route('/')

def index():
    return jsonify({
        'data' : data,
        'message' : 'success'
    }), 200
    
@app.route('/stars')

def starr():
    name = request.args.get('Name')
    star_data = next(item for item in data if item['Name'] == name)
    return jsonify({
        'data' : star_data,
        'message' : 'success'
    }), 200 

if __name__ == '__main__':
    app.run()

