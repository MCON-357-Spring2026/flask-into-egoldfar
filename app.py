from flask import Flask, jsonify, request

app = Flask(__name__)

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
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    operation = request.args.get('operation')
    if operation == 'add':
        return jsonify({'result': num1 + num2, 'operation': 'add'})
    elif operation == 'subtract':
        return jsonify({'result': num1 - num2, 'operation': 'subtract'})
    elif operation == 'multiply':
        return jsonify({'result': num1 * num2, 'operation': 'multiply'})
    elif operation == 'divide':
        return jsonify({'result': num1 / num2, 'operation': 'divide'})
    else:
        return jsonify({'error': 'Invalid operation'})

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)