from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from todo import Todo

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/todo", methods=["GET"])
def get_todos():
    all_todos = Todo.query.all() 

    print(all_todos[0])
    return json.dumps([i.to_json() for i in all_todos])

@app.route("/todo", methods=["POST"])
def new_todo():
    data = request.data
    dataDict = json.loads(data)

    name = dataDict["name"]
    description = dataDict["description"]
    status = dataDict["status"]

    todo = Todo(name, description, status)

    try:
        db.session.add(todo)
        db.session.commit()
    except Exception as e: 
        print(e)
    
    return json.dumps(todo.to_json())

@app.route("/goodbye")
def goodbye():
    return "Good Bye Cruel World!"
if __name__ == '__main__':
    app.run()
