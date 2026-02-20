from flask import Flask, jsonify, request

app = Flask(__name__)

@app.before_request
def before_request_func():
    print(f"Before request: {request.method} {request.path}")

@app.after_request
def after_request_func(response):
    response.headers['X-Custom-Header'] = 'FlaskRocks'
    return response

@app.teardown_request
def teardown_request_func(exception=None):
    if exception:
        print(f"Teardown request - Exception occurred: {exception}")

@app.route('/')
def index():
    return '<h1>Welcome to My Flask API!</h1>'

@app.route('/about')
def about():
    return jsonify({"name": "Elisheva Goldfarb", "course": "MCON357", "semester": "Spring 2026"})

@app.route('/greet/<name>')
def greet(name):
    return f'<p>Hello, {name}! Welcome to Flask</p>'

@app.route('/calculate')
def calculate():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    operation = request.args.get('operation')
    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operation"}), 400
        return jsonify({"result": result, "operation": operation})
    except Exception as e:
        # Log the exception and return an error response
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred during calculation"}), 500

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    data['echoed'] = True
    return jsonify(data)

@app.route('/status/<int:code>')
def status(code):
    message = f'<p>This is a {code} status message</p>'
    status_code = code
    return message, status_code

@app.route('/debug/routes')
def show_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'path': str(rule)
        })
    return jsonify(routes)

if __name__ == '__main__':
    app.run(debug=True, port=5000)