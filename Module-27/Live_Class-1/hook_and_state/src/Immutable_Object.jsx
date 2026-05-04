
import { useState } from 'react';

function Immutable_Object () {

    const [name, setUser] = useState({                      // user's information is stored in useState as an object
                                                            // useState used bcz the property of this object will be changed again and again
        name: "John",
        address:{
            city: "New York",
            zip: "1001"
        }

    });



    function changeName() {                              // to change any property of the object, we need to use the setUser function
       
        setUser(prev => ({                                // immediately invoked function; used to update the state of the object; prev -> previous state of the object
            ...prev,                                      // ...prev -> (...)spread operator; this is used to copy the previous properties of the object
            name: "Mickey Mouse",                         // we want to change just one property of the object, but "react" needs to know the previous properties of the object to update it correctly; without the previous fields, react wont understand what to update
            address: {
                ...prev.address,
                zip: "2002"
            }
       }))

    }

    return (
        <div>

            <h3>Immutable Object:</h3>

            <p>Name: {name.name}</p>
            <p>City: {name.address.city}</p>
            <p>Zip: {name.address.zip}</p>

            <button onClick={changeName}>Click to Change Name</button>                        {/* 1. by clicking the button, the "name" of the object will be changed  --- */}

        </div>
    )


}


export default Immutable_Object;