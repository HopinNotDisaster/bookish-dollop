from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>我是首页</h1>"


# @app.route("/detail/<b_id>/")
@app.route("/detail/<int:b_id>/")
def detail(b_id):
    print(type(b_id))
    return f"<h1>我是详情{b_id}</h1>"


@app.route("/media/<path:path>/")
def media(path):
    print(type(path))
    return f"你放问的资源是{path}"


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
