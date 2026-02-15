import './App.css'

import MyDetails from './MyDetails'
import Map from './Map'


function App() {

  const isUserLoggedIn = true;                      // condition
  // const isUserLoggedIn = false;                      // condition

  return (
    <>
      <div>
        <h2>This is Nabil Ahmed</h2>


        {isUserLoggedIn ? <h3>Welcome to this site </h3> : <p> Please Login </p> } 

        <Map/>

      </div>
    </>
  )
  
}

export default App
