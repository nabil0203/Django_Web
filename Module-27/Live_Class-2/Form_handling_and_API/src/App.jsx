import './App.css'
import Home from './components/home/Home'
import About from './components/about/About'
import Users from './components/users/Users'
import SingleUser from './components/users/SingleUser'

import { BrowserRouter, Routes, Route, Link, NavLink } from 'react-router-dom'


function App() {
  return (

    <BrowserRouter>


    <Routes>

      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/users" element={<Users />} />

      <Route path="/users/:id" element={<SingleUser />} />                   {/* ----single user route with dynamic id parameter-------Dynamic Routing */}

  </Routes>



    <nav>


      {/*------- Link --------- */}

      {/*
      <Link to="/">Go to home page</Link>
      <br />
      <Link to="/about">Go to about page</Link>
      */}



      {/*------- NavLink ---------*/}
      
      <NavLink to="/" className={({ isActive }) => ( isActive ? 'active-link' : 'inactive-link' )}>Go to home page</NavLink>                                                  {/* ----- Linked to home page */}
      <br />
      <NavLink to="/about" className={({ isActive }) => (isActive ? 'active-link' : 'inactive-link' )} >Go to about page</NavLink>                                            {/* ----- Linked to about page */}
      <br />
      <NavLink to="/users" className={({ isActive }) => (isActive ? 'active-link' : 'inactive-link' )} >Go to users page</NavLink>                                            {/* ----- Linked to users page */}
      



    </nav>


    </BrowserRouter>

  )
}

export default App
