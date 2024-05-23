from config import db

class Contact(db.Model):
    student_id = db.Column(db.String, primary_key=True)
    dob= db.Column(db.String(8), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    counseling_reason= db.Column(db.String(20), unique=False, nullable=False)
    
    def to_json(self):
        return {
            "studentId" : self.student_id,
            "dob" : self.dob,
            "email" : self.email,
            "counselingReason" : self.counseling_reason
        }