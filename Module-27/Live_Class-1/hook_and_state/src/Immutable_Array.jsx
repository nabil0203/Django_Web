
import { useState } from 'react';

function Immutable_Array() {


    const [fruits, setFruits] = useState(["apple", "banana", "cherry"]);                    //1. we have to add a new fruit to this array; as this is immutable in react we cannot directly change the array;





    function addFruit(event) {                                             //5. function to add new fruit in the array

        event.preventDefault();                                           //6. to prevent the default behavior of the form; this will prevent the page from refreshing when we submit the form
        const newFruit = event.target.newFruit.value;                     // to get the value of the input field; event.target -> form element; newFruit -> name of the input field

        setFruits(prev => [...prev, newFruit]);                           // to update the state of the array; ...prev -> (...)spread operator; this is used to copy the previous elements of the array; newFruit -> new fruit to be added
    }







    function deleteFruit(fruitToDelete) {                                                            //7. function to delete a fruit from the array
        const updatedFruits = fruits.filter((fruit) => fruit !== fruitToDelete);                     //8. to create a new array with the fruit to be deleted removed; filter() method is used to create a new array with all elements that pass the test implemented by the provided function
                                                                                                     //9. in this case, we are checking if the fruit is not equal to the fruit to be deleted; if it is not equal, it will be included in the new array; if it is equal, it will be excluded from the new array
        setFruits(updatedFruits);

    }




    return (
        <div>
            <h3>Immutable Array:</h3>


            {/* 2. printing the fruits in array using map */}
            {fruits.map((fruit) => (
                <div style={{ display: "flex", alignItems: "center" }}>

                    <p>{fruit}</p>

                    <button onClick={() => deleteFruit(fruit)}>                                     {/* 3. each fruit will have delete button; */}
                        Delete                                                                      {/* this immediately invoked function will call the deleteFruit function with the fruit to be deleted as an argument;  */}
                    </button>                                                                       {/* we are using an arrow function here to pass the argument to the "deleteFruit" function; if we directly call deleteFruit(fruit), it will be called immediately when the full component renders, which is not what we want; we want it to be called only when the button is clicked  */}
                                                                                                    {/* when we click the delete button, the deleteFruit function will be called with the fruit to be deleted as an argument*/}
                       
                
                </div>
            ))}



            {/*-----add new fruit in form-----*/}

            <form onSubmit={addFruit}>

                <input name="newFruit" type="text" placeholder='Enter Fruit Name' />                 {/* 4. input field to enter new fruit name; name attribute is used to get the value of the input field in the addFruit function */}
                <button type="submit">Add Fruit</button>

            </form>

        </div>
    )

}

export default Immutable_Array;