import { useRef } from "react";

function Use_ref_hook() {

    const textRef = useRef(null);                                   // 1. textRef is a reference; initial value is null;


    function handleClick() {

    // textRef.current.innerText = "Button Clicked";                                       // 3. on button click, the text content of the <p> is changed to "Button Clicked" using textRef.current 
       textRef.current.innerHTML = "<strong> Button Clicked </strong>";                    // 3. on button click, the text content of the <p> is changed to "Button Clicked" in bold using textRef.current
       textRef.current.style.color = "red";                                                // 4. on button click, the text color of the <p> is  also changed to red using textRef.current.style.color

    }
   

    return (
        <div>

            <p ref={textRef}>Use Ref Hook Text content</p>                      {/* 2. textRef is attached to the <p> ; it can be accessed using textRef.current */}

            <button onClick={handleClick}>Click Here</button>

        </div>
    )
}

export default Use_ref_hook;
