from flask import request, jsonify
from config import app, db
from models import Contact

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

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)