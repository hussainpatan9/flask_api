from flask import Flask, jsonify, request

app = Flask(__name__)


# @app.route()
@app.route(rule="/", methods=["GET"])
def main():

    return "hello World"


@app.route(rule="/get_data", methods=["GET"])
def get_data():
    name = "hussain"
    class_ = "CDE"
    # print(sdf)
    return jsonify('{"name":"hussain","session":"Data Engineering","Teacher":"Awais"}')


@app.route(rule="/pagination/<int:number>/", methods=["GET"])
def pagination(number):

    return f"onPage: {number}"


@app.route(rule="/user/<string:name>/", methods=["GET"])
def get_user(name):

    return f"User Name: {name}"


@app.route(rule="/post_data", methods=["GET", "POST"])
def post_data():
    if request.method == "GET":

        return f"GET REQUEST"
    elif request.method == "POST":
        data = request.get_json()
        return jsonify({"user data": data})


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port="8080")
