from flask import request, jsonify
from config import app, db
from models import Contact
from script import WebBot
import json

@app.route("/contacts" , methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts" : json_contacts})

@app.route("/create_contact", methods=["POST"])
def create_contact():
    student_id = request.json.get("studentId")
    dob = request.json.get("dob")
    email = request.json.get("email")
    counselingReason = request.json.get("counselingReason")
    
    if not student_id or not dob or not email or not counselingReason or not counselingReason:
        return {
            jsonify({"message" : "You must include a student ID, dob, email address, and counselingReason"}),
            400,
        }
    new_contact = Contact(student_id=student_id, dob=dob, email=email , counselingReason=counselingReason)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message" : str(e)}), 400
    
    return jsonify({"message": "User created!"}), 201

#----------------------------------------------------------------
""" 

THIS EXISTS IN "server.py"

This function is used solely for local testing purposes
This will write to "client\public\student_info.json" with a JSON opject
Used for "backend\script1.py" to listen and execute the webbot
"""
@app.route('/save-student-info', methods=['POST'])
def save_student_info():
    data = request.json
    with open('../client/public/student_info.json', 'w') as f:
        json.dump(data, f, indent=4)
    return jsonify({'message': 'Data saved successfully!'}), 200

#----------------------------------------------------------------

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(port=5000,debug=True)