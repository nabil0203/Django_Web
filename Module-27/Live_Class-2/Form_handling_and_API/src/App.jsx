import './App.css'
import Home from './components/home/Home'
import About from './components/about/About'

import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'


function App() {
  return (

    <BrowserRouter>


    <Routes>

        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />

      </Routes>



    <nav>

      <Link to="/">Go to home page</Link>
      <br />
      <Link to="/about">Go to about page</Link>

    </nav>


    </BrowserRouter>

  )
}

export default App
