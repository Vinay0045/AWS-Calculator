from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression')
    
    try:
        # Dangerous eval in production, but okay for a simple calculator demo
        # restricting characters to basic math to be safer
        allowed_chars = "0123456789+-*/.()"
        if not all(char in allowed_chars for char in expression):
             return jsonify({'result': 'Error', 'error': 'Invalid characters'})
        
        # Evaluate the expression
        result = eval(expression)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'result': 'Error', 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
