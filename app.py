from flask import Flask, request, jsonify
from flask_cors import CORS  
app = Flask(__name__)
CORS(app)

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({
        "operation_code": 1
    })

@app.route('/bfhl', methods=['POST'])
def process_request():
    data = request.json.get('data', [])
    
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    lowercase_alphabets = [item for item in alphabets if item.islower()]

    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

    response = {
        "is_success": True,
        "user_id": "Siddhant_Varshney_31032003",  
        "email": "siddhant.varshney2021@vitstudent.ac.in",  
        "roll_number": "21BCE0277",  
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
