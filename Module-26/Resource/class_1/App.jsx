import './App.css'
import Notun from './Notun.jsx'

function App() {
  const isUserLoggedIn = true;
  
  return (
    <div>
      Hello World!
      {isUserLoggedIn ? <Notun/> : <></>}
    </div>
  )
}

export default App
