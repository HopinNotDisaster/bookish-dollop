from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html", name="qiku", age=10)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
