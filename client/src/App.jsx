import { useState } from 'react'
import sccLogo from  './assets/SacCity.jpg'
import pantherLogo from './assets/Panther.webp'
import './App.css'
import IDAndDOBComponent from './IDAndDOBComponent'

function App() {

  return (
    <>

      <div>
        <a href="https://scc.losrios.edu/student-resources/counseling-and-transfer" target= "_blank">
          <img src={sccLogo} className="logo scc" alt="Scc Logo" />
        </a>
        <a href="https://scc.losrios.edu" target= "_blank">
          <img src={pantherLogo} className="logo scc spin" alt="Panther Logo" />
        </a>
      </div>

      <h1>One more step before we can book your appointment</h1>
      <div className="card">
        <IDAndDOBComponent />
      </div>
    </>
  )
}

export default App
