import { Link } from "react-router-dom"
import { useEffect, useState } from "react"


function Home() {

  const [count, setCount] = useState(0)                     // count -> state variable


  useEffect(() => {
    document.title = `Tab Count: ${count}`                       // Whenever count state variable is updated, document title will be updated with the new count value
  }, [count])                                                    // useEffect will be called whenever count state variable is updated



  return (
    <div>

      <h1>This is Home page</h1>


      <button onClick={() => setCount(count+1)}> Count: {count}</button>                             {/* onClick  -> setCount function -> update count state variable */}       


    </div>
  )
}

export default Home