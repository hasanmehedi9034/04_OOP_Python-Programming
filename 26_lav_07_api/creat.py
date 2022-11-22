from flask import Flask, request

#init flask app
app = Flask(__name__)

database = {
    'minhaj': '100'
}

@app.route('/', methods=['GET'])
def home():
    return 'Welcom to cute API'

@app.route('/something', methods=['GET'])
def something():
    return str(1)

@app.route('/getdata', methods=['GET'])
def get_data():
    return database

# api/adddata?name=id
@app.route('/adddata', methods=['GET', 'PUT'])
def add_data():
    key, value = list(request.agrs.items())[0]
    database[key] = value
    
    print(key, value)
    return f'{key} added'

if __name__ == '__main__':
    app.run()