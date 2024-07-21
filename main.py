# from flask import Flask
import flask


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


# if __name__ == "__main__":
#     app.run()

# waitress-serve --listen=127.0.0.1:5000 main:app
