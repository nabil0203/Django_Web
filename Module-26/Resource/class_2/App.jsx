import './App.css'
import Course from './Course'
import CourseCard from './CourseCard'

function App() {

  const age = 10
  const age2 = '10'
  const courses = ['React', 'Vue', 'Angular']

  function handleFormSubmit(event) {
    event.preventDefault()
    alert('Form submitted!, with name ' + event.target.username.value + ' and email ' + event.target.email.value)
  }

  return (
    <div className="App">
      <h1>Welcome to React Class 2</h1>
      {(function() {
        return age === age2 ? <Course /> : <p>Access Denied</p>
      })()}
      {courses.map((course) => (
        <CourseCard name={course}/>
      ))}

      <form onSubmit={handleFormSubmit}>
        <input name='username' type="text" placeholder="Enter your name" className="border p-2 m-2"/>
        <input name='email' type="email" placeholder="Enter your email" className="border p-2 m-2"/>
        <button type="submit" className="bg-blue-500 text-white p-2 m-2">Submit</button>
      </form>
    </div>
  )
}

export default App
