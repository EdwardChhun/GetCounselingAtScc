import React from 'react';

const ClearButton = ({ onClick }) => {
  return (
    <button type="button" onClick={onClick}>
      Clear
    </button>
  );
};

export default ClearButton;
