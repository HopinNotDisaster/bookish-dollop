from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>我是首页</h1>"


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
