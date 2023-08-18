from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello World!", 200

@app.route("/calculator/add", methods=['POST'])
def add():
    try:
        a = request.json['first']
        b = request.json['second']
        result = a + b
        return jsonify({"result": result}), 200
    except KeyError:
        return jsonify({"error": "Missing 'first' or 'second' in request data"}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    try:
        a = request.json['first']
        b = request.json['second']
        result = a - b
        return jsonify({"result": result}), 200
    except KeyError:
        return jsonify({"error": "Missing 'first' or 'second' in request data"}), 400

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')


