
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Docker Calculator API",
        "operations": [
            "addition",
            "subtraction",
            "multiplication",
            "division"
        ]
    })


@app.route("/calculate", methods=["GET"])
def calculate():

    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        operation = request.args.get("operation")

        if operation == "add":
            result = num1 + num2

        elif operation == "subtract":
            result = num1 - num2

        elif operation == "multiply":
            result = num1 * num2

        elif operation == "divide":
            if num2 == 0:
                return jsonify({"error": "Cannot divide by zero"}), 400
            result = num1 / num2

        else:
            return jsonify({"error": "Invalid operation"}), 400

        print(f"Calculation: {num1} {operation} {num2} = {result}")

        return jsonify({
            "num1": num1,
            "num2": num2,
            "operation": operation,
            "result": result
        })

    except (TypeError, ValueError):
        return jsonify({"error": "Please provide valid numbers"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
