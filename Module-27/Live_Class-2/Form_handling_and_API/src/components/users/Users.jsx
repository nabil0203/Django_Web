import { useState } from "react"
import { useNavigate } from "react-router-dom"


function Users() {


    const [users, setUsers] = useState([])                                      // state to hold users data
    const [isLoading, setLoading] = useState(false)                             // state to track loading status                        
    

    const navigate = useNavigate()                                              // hook to navigate to single user details page


    // Async/Await function to fetch users data from API
    async function fetchUsers() {
        setLoading(true)
        
        const r = await fetch('https://fake-json-api.mock.beeceptor.com/users')
        const json = await r.json()
        // console.log(json)
        setUsers(json)

        setLoading(false)
    }




    // ------Promises to fetch users data from API
    // ------Not recommended----------- 

    // function fetchUsers() {
    //     setLoading(true)
        
    //     fetch('https://fake-json-api.mock.beeceptor.com/users')                                                    // fetch data from URL
    //         .then(r => r.json())                                                                                    // Converting response to JSON format
    //         . then(setUsers)                                                                                          // Setting data in state

    //     setLoading(false)
    // }



  return (
    <div>
        <h1>Users Component</h1>

        <button onClick={fetchUsers}>Fetch Users </button>                          {/* fetch users on button click */}


        {isLoading && <p>Loading...</p>}                                            {/* loading state */}


        {users.map(user => (
            <div key={user.id}> 
                
                {user.name} - {user.email}                                                                   {/* render all users */}
                
                <button onClick={() => navigate(`/users/${user.id}`)}>View Details</button>                            {/* button to view details of specific user, functionality to be implemented in SingleUser component */}

            </div>
        ))}

    </div>
  )
}

export default Users