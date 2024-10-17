# from flask import Flask
from flask import Flask, abort, jsonify, request
import flask
import requests

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html", name="FLASK", age=30)


@app.route("/user/<username>")
def index1(username=None):
    return flask.render_template(
        "index.html",
        name=username,
    )


# Список задач
tasks = [
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
        "done": False,
    },
    {
        "id": 2,
        "title": "Learn Python",
        "description": "Need to find a good Python tutorial on the web",
        "done": False,
    },
    {"id": 3, "title": "Read a book", "description": "", "done": False},
]


# Получение списка задач
@app.route("/todo/api/v1.0/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})


# Получение задачи по id
@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = filter(lambda t: t["id"] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({"task": task[0]})


# Создание новой задачи
@app.route("/todo/api/v1.0/tasks", methods=["POST"])
def create_task():
    if not request.json or "title" not in request.json:
        abort(400)
    task = {
        "id": tasks[-1]["id"] + 1,
        "title": request.json["title"],
        "description": request.json.get("description", ""),
        "done": False,
    }
    tasks.append(task)
    return jsonify({"task": task}), 201


# Обновление задачи
@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = filter(lambda t: t["id"] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if "title" in request.json and type(request.json["title"]) != str:
        abort(400)
    if "description" in request.json and type(request.json["description"]) is not str:
        abort(400)
    if "done" in request.json and type(request.json["done"]) is not bool:
        abort(400)
    task[0]["title"] = request.json.get("title", task[0]["title"])
    task[0]["description"] = request.json.get("description", task[0]["description"])
    task[0]["done"] = request.json.get("done", task[0]["done"])
    return jsonify({"task": task[0]})


# Удаление задачи
@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = filter(lambda t: t["id"] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({"result": True})


# @app.route("/todo/")
# def _task_1():
#     response = requests.get("https://api.github.com/")
#     response_json = response.json()
#     return jsonify({"result": response_json})


# @app.route("/todo/2")
# def _task_():
#     response = requests.get("https://api.github.com/")
#     response_json = response.json()
#     return jsonify({"result": response_json})


if __name__ == "__main__":
    app.run(debug=True)

# if __name__ == "__main__":
#     app.run()

# waitress-serve --listen=127.0.0.1:5000 main:app
# waitress-serve --listen=127.0.0.1:5000 --reload main:app
