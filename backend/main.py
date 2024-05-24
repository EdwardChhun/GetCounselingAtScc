from flask import request, jsonify
from config import app, db
from models import Contact
from script1 import WebBot

@app.route("/contacts" , methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts" : json_contacts})

""" 
Function that takes info from user and runs the web bot script
Inputs  : studentId, dob, email, counselingReason
Outputs : <Respond to front end with error handling>
"""
@app.route("/get_info", methods=["POST"])
def get_info():
    try:
        # Extract JSON data from request
        data = request.get_json()
        
        # Parse JSON data
        student_id = data.get("studentId")
        dob = data.get("dob")
        counseling_reason = data.get("counselingReason")
        
        # Validate received data
        if not student_id or not dob or counseling_reason is None:
            return jsonify({"error": "Missing required fields"}), 400
        
        # Initialize and run WebBot
        bot = WebBot(student_id, dob, counseling_reason)
        bot.open_web_page()
        bot.execute_web_bot()
        
        return jsonify({"message": "WebBot executed successfully"}), 200
    
    except Exception as e:
        # Handle errors
        return jsonify({"error": str(e)}), 500
        

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)