import { useState } from 'react';
import './IDAndDOBComponent.css'; // Import CSS file for styling
import ClearButton from './ClearButton';

const IDAndDOBComponent = () => {
  const [id, setID] = useState('');
  const [dob, setDOB] = useState('');
  const [email, setEmail] = useState('');
  const [counselingReason, setCounselingReason] = useState('');

  const handleIDChange = (e) => {
    setID(e.target.value);
  };

  const handleDOBChange = (e) => {
    setDOB(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handleCounselingReasonChange = (e) => {
    setCounselingReason(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = {
      id: id,
      dob: dob,
      email: email,
      counselingReason: counselingReason
    };
    const url = "http://127.0.0.1:5000/create_contact"
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(formData)
    }
    try{
      const response = await fetch(url, options)
      if (response.status !== 201 && response.status !== 200) {
        const data = await response.json()
        alert(data.message)
      } else {
        // successful
      } 
    } catch (error) {
      console.log(formData);
    }
  };

  const handleClear = () => {
    setID('');
    setDOB('');
    setEmail('');
    setCounselingReason('');
  };

  return (
    <form className="id-dob-container" onSubmit={handleSubmit}>

      <div className="input-group">
        <label htmlFor="id">Losrios WiD:</label>
        <input
          type="text"
          id="id"
          value={id}
          onChange={handleIDChange}
          placeholder="Enter your WiD"
        />
      </div>

      <div className="input-group">
        <label htmlFor="dob">Date of Birth:</label>
        <input
          type="date"
          id="dob"
          value={dob}
          onChange={handleDOBChange}
        />
      </div>

      <div className="input-group">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={handleEmailChange}
          placeholder="Enter your email address"
        />
      </div>


      <div className="input-group">
        <label htmlFor="counselingReason">Counseling Reason:</label>
        <select id="counselingReason" value={counselingReason} onChange={handleCounselingReasonChange}>
          <option value="">Select Counseling Reason</option>
          <option value="Option 1">Academic Renewal</option>
          <option value="Option 2">Consortium</option>
          <option value="Option 3">Financial Aid Course Review</option>
          <option value="Option 4">Graduation Petition</option>
          <option value="Option 5">IGETC/CSU Certification</option>
          <option value="Option 6">International Student</option>
          <option value="Option 7">Personal or Emotional Concern</option>
          <option value="Option 8">Petition for .5 Priority Registration</option>
          <option value="Option 9">Pick Classes (multi-semester)</option>
          <option value="Option 10">Pick Classes 1-sem</option>
          <option value="Option 10">Pre-Requisite Info</option>
          <option value="Option 10">Probation & Dismissal (Hold on record)</option>
          <option value="Option 10">Transcript Evaluation</option>
          <option value="Option 10">Transfer or TAG Questions</option>
          <option value="Option 10">Veteran Student (VA Planner)</option>
        </select>
      </div>

      <div className="button-group">
        <button type="submit"> Submit </button>
        <ClearButton onClick={handleClear} />
      </div>
    </form>
  );
};

export default IDAndDOBComponent;
