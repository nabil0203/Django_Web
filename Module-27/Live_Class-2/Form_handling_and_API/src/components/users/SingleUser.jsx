import { useState } from "react"
import { useParams } from "react-router-dom"



function SingleUser() {


    const [user, setUser] = useState(null)

    const {id} = useParams()                                     // get specific user id from URL parameters



    async function GetUserById() {

        const r = await fetch(`https://fake-json-api.mock.beeceptor.com/users/${id}`)                       // fetch user data from API using the id from URL parameters
        const json = await r.json()

        console.log(json)
        setUser(json)

    }

    return (
        <div>
            <h1>Single User Details</h1>
            


            <button onClick={GetUserById}>Get user by ID</button>

            {user && (
                <div> 
                    {user.name} - {user.email}
                </div>
            )}
        </div>
    )

}

export default SingleUser