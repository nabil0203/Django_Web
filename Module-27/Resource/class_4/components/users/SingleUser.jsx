import { useState } from "react";
import { useSearchParams, useParams } from "react-router-dom";

function SingleUser() {
    const { id } = useParams();
    const [searchParams] = useSearchParams();
    const searchedWithQuery = searchParams.get('s');
    console.log(searchedWithQuery);
    
    const [user, setUser] = useState(null);
    async function getSingleUser(){
        const r = await fetch(`https://fake-json-api.mock.beeceptor.com/users/${id}`)
        const json= await r.json()
        console.log(json);
        setUser(json);
    }
  return (
    <div>
      <button onClick={async () => await getSingleUser()}>Get User By Id</button>
      {user && <div>{user.name} - {user.email}</div>}
    </div>
  )
}

export default SingleUser