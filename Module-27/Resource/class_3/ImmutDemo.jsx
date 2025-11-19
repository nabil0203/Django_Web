import { useState } from "react";

function ImmutDemo() {
const [user, setUser] = useState({
    name: "Alice",
    address: {
      city: "Wonderland",
      zip: "12345"
    }
  });

  const [fruits, setFruits] = useState(["Apple", "Banana", "Cherry"]);

  function handleChangeName() {
    const newUser = {
        ...user,
        name: "Bob"
    }
    setUser(newUser);
    // setUser(prev => ({
    //   ...prev,
    //   name: "Bob"
    // }));
  }

  return <div>
    Immutability Demo Component
    <p>Name: {user.name}</p>
    <p>City: {user.address.city}</p>
    <p>Zip: {user.address.zip}</p>

    <button onClick={handleChangeName}>Change Name</button>
</div>
}

export default ImmutDemo;