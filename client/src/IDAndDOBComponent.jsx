import { useState } from 'react';
import './IDAndDOBComponent.css'; // Import CSS file for styling
import ClearButton from './ClearButton';
import axios from 'axios';

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

    const data = {
      id: id,
      dob: dob,
      email: email,
      counselingReason: parseInt(counselingReason)
    };
    try {
      await axios.post('http://localhost:5000/save-student-info', data);
      console.log(data);
      alert('Data saved successfully!');
    } catch (error) {
        console.error('Error saving data', error);
        alert('Failed to save data.');
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
          <option value="1">Academic Renewal</option>
          <option value="2">Consortium</option>
          <option value="3">Financial Aid Course Review</option>
          <option value="4">Graduation Petition</option>
          <option value="5">IGETC/CSU Certification</option>
          <option value="6">International Student</option>
          <option value="7">Personal or Emotional Concern</option>
          <option value="8">Petition for .5 Priority Registration</option>
          <option value="9">Pick Classes (multi-semester)</option>
          <option value="10">Pick Classes 1-sem</option>
          <option value="11">Pre-Requisite Info</option>
          <option value="12">Probation & Dismissal (Hold on record)</option>
          <option value="13">Transcript Evaluation</option>
          <option value="14">Transfer or TAG Questions</option>
          <option value="15">Veteran Student (VA Planner)</option>
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
