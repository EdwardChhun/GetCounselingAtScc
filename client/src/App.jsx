// import { useState } from 'react'
import sccLogo from  './assets/SacCity.jpg'
import pantherLogo from './assets/Panther.webp'
import './App.css'
import IDAndDOBComponent from './IDAndDOBComponent'
import axios from 'axios'

function App() {

  return (
    <>

      <div>
        <a href="https://scc.losrios.edu/student-resources/counseling-and-transfer" target= "_blank">
          <img src={sccLogo} className="logo scc" alt="Scc Logo" />
        </a>
        <a href="https://scc.losrios.edu" target= "_blank">
          <img src={pantherLogo} className="logo scc" alt="Panther Logo" />
        </a>
      </div>

      <h1>One more step before we can book your appointment</h1>
      <div className="card">
        <IDAndDOBComponent />
      </div>

      <h1> What We Do </h1>
      <h3> Students at SCC tend to have to wait till midnight for the school's counseling
        website to restart. </h3>
     
      <h3> 
        We made this website for students to input
        their preferred times and book them an appointment without the risk of losing sleep.
      </h3>
    </>
  )
}

export default App
