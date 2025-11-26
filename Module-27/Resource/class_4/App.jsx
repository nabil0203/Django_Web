import './App.css'
import { BrowserRouter, Routes, Route, NavLink } from 'react-router-dom'
import Home from './components/home/Home'
import About from './components/about/About'
import Users from './components/users/Users'
import SingleUser from './components/users/SingleUser'

function App() {

  return (
    <BrowserRouter>
      <div>
        <nav>
          <NavLink to='/'>Home</NavLink>
          <NavLink to='/users'>Users</NavLink>
          <NavLink className={({ isActive }) => (isActive ? 'active-link' : 'inactive-link')} to='/about'>About</NavLink>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About/>} />
          <Route path="/users" element={<Users/>} />
          <Route path="/users/:id" element={<SingleUser />} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}

export default App
