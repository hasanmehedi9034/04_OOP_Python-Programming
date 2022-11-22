'''My cute API'''

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Welcom to cute API'

@app.route('/something', methods=['GET'])
def something():
    return str(1)

if __name__ == '__main__':
    app.run()

