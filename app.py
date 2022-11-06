from flask import Flask, request, render_template, jsonify, json

app = Flask("__name__")


@app.route("/result", methods=["POST"])
def operation():
    body = request.get_json()
    operation_type = body.get("operation_type")
    x_val = body.get("x")
    y_val = body.get("y")
    val = {
         "operation_type": operation_type,
            "x": x_val,
            "y": y_val
        }
    data = json.dumps(val)

    if operation_type == "add" or operation_type == "addition":
         result = x_val + y_val
    elif operation_type == "subtract" or operation_type == "subtraction":
         result = x_val - y_val
    elif operation_type == "multiply" or operation_type == "multiplication":
         result = x_val * y_val
    return jsonify({"slackUsername" : "Leele Barry Baribeop",
        "operation_type": operation_type,
        "result" : result,
    })


if __name__ == "__main__":
    app.run(debug=False)