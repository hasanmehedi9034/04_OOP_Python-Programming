from flask import Flask, jsonify, request

app = Flask(__name__)

students =[
    {'id': 1,
     'name': 'Rahim'
    },
    {'id': 2,
     'name': 'Karim'
    }
]

@app.route("/")
def hello():
    return jsonify(students)

@app.route("/add", methods=['GET', "POST"])
def add():
    students.append(request.get_json())
    print(request.get_json())
    return 'Student added succesfully', 200

@app.route('/update', methods=['PUT', 'GET'])
def update():
    for student in students:
        if str(student.get('id')) == request.get_json().get('id'):
            student.update(request.get_json())
    return 'Student updated succesfully'

@app.route('/delete', methods=[ 'GET', 'DELETE'])
def delete():
    for i in range(len(students)):
        if str(students[i].get('id')) == request.args.get('id'):
            del students[i]
            break
    return 'student deleted succesfully'

app.run(debug=True)















