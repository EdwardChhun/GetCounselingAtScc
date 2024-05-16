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

  const handleSubmit = (e) => {
    e.preventDefault();

    const formData = {
      id: id,
      dob: dob,
      email: email,
      counselingReason: counselingReason
    };

    console.log(formData);
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
        <label htmlFor="id">ID:</label>
        <input
          type="text"
          id="id"
          value={id}
          onChange={handleIDChange}
          placeholder="Enter your WID"
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
          <option value="Option 1">Option 1</option>
          <option value="Option 2">Option 2</option>
          <option value="Option 3">Option 3</option>
          <option value="Option 4">Option 4</option>
          <option value="Option 5">Option 5</option>
          <option value="Option 6">Option 6</option>
          <option value="Option 7">Option 7</option>
          <option value="Option 8">Option 8</option>
          <option value="Option 9">Option 9</option>
          <option value="Option 10">Option 10</option>
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
