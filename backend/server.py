from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/save-student-info', methods=['POST'])
def save_student_info():
    data = request.json
    with open('../client/public/student_info.json', 'w') as f:
        json.dump(data, f, indent=4)
    return jsonify({'message': 'Data saved successfully!'}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
