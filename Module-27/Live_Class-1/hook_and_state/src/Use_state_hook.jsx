import { useState } from 'react';                           // for useState hook


function Use_state_hook() {


    // --------Without using Hooks and States-------


    // let x = 10;

    // function increment() {
    //     x = x + 1;
    //     console.log(x);
    // }

    // return (
    //     <div>
    //         <p>Increment on click</p>

    //         <p>{x}</p>

    //         <button onClick={increment}>Click Me</button>
    //     </div>
    // )




    // -------Using Hooks and States------


    const [x, setX] = useState(0);                      // useState is a hook 
                                                        //"x" is the variable and "setX" is the function to change the value of x; initial value of x    0; 

    function increment() {                                 // function to increment the value of x by 1 each time
        setX(x + 1);
    }

    function decrement() {                                 // function to decrement the value of x by 1 each time
        setX(x - 1);
    }

    return (
        <div>
            <p>Increment/Decrement on click</p>

            <p>{x}</p>

            <button onClick={increment}>Add</button>
            <button onClick={decrement}>Subtract</button>
        </div>
    )

}

export default Use_state_hook;