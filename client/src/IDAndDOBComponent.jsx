import React, { useState } from 'react';
import './IDAndDOBComponent.css'; // Import CSS file for styling

const IDAndDOBComponent = () => {
  const [id, setID] = useState('');
  const [dob, setDOB] = useState('');

  const handleIDChange = (e) => {
    setID(e.target.value);
  };

  const handleDOBChange = (e) => {
    setDOB(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const formData = {
      id: id,
      dob: dob
    };

    console.log(formData);
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
          placeholder="Enter your ID"
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

      <button type="submit"> Submit </button>
    </form>
  );
};

export default IDAndDOBComponent;
