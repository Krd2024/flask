import requests

# from flask import jsonify


# def _task_1():
#     response = requests.get("https://api.github.com/")
#     response_json = response.json()
#     print(response_json)


def _task_1():
    response = requests.get("https://annrus23.ru/")
    response_json = response.text
    print(response_json)


# def _task_1():
#     response = requests.get("https://annrus23.ru/")
#     response_json = response.headers
#     for key, value in response_json.items():
#         print(key, ": ", value)


_task_1()
# def _task_():
#     response = requests.get("https://api.github.com/")
#     response_json = response.json()
#     return jsonify({"result": response_json})
