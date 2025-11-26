import { Link } from "react-router-dom"
import { useState, useEffect } from "react"

function Home() {
  const [count, setCount] = useState(0)

  useEffect(()=>{
    document.title = `Count is ${count}`
  },[])

  useEffect(()=>{
    document.title = `Count is ${count}`
  })

  useEffect(()=>{
    document.title = `Count is ${count}`
  },[count])

  // useEffect(()=>{
  //   const t=setTimeout(search,300);
  //   return()=>clearTimeout(t)
  // })

  return (
    <div>
      <h1>Welcome to the Home Page</h1>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>
    </div>
  )
}

export default Home