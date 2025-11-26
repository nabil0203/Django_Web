import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"

function Users() {

    const [users, setUsers] = useState([])
    const [isLoading, setIsLoading] = useState(false)
    const navigate = useNavigate();

    async function fetchUsers() {
        setIsLoading(true)
        const r = await fetch('https://fake-json-api.mock.beeceptor.com/users')
        const json= await r.json()
        console.log(json);
        setUsers(json)
        setIsLoading(false)
    }

  return (
    <div>
      <h1>Users Component</h1>
      <button onClick={async () => await fetchUsers()}>Refresh</button>
      {isLoading && <div>Loading...</div>}
        {users.map((user)=><div key={user.id}>{user.name} - {user.email} <button onClick={() => navigate(`/users/${user.id}`)}>View</button></div>)}
    </div>
  )
}

export default Users