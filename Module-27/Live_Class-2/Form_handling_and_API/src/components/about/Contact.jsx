import { useState } from 'react'

function Contact() {


    const [error, setError] = useState("")                                                          // state to store the error message; first error is empty string

    const [pass, setPass] = useState("")                                                      // state to store the password; first password is empty string

    
    // ----------- Check the password length less than 6 characters------------
    function validatePassword(password) {

        event.preventDefault()                                                          // prevent the default behavior of the form submission 

        if (password.target.pass.value.length < 6) {
            setError("Password must be at least 6 characters long")                      // if the password length is less than 6 characters, set the error message
            return false
        }
        return true

    }



    // ----------- handle the form submission ------------
    function onFinish(event) {                                                  // event -> catching the "pass" input

        event.preventDefault()                                                  // prevent the default behavior of the form submission
        console.log(event.target.pass.value)


        if (validatePassword(event)) {                                                  // before submitting -> calling the "validatePassword" function to check the password length 
            console.log("Form Submitted Successfully")
        }
    }



    return (

        <div>

            <h2>This is the Contact Page</h2>


            <form onSubmit={onFinish}>
                <input type="text" placeholder="Enter Your Name" /> <br />

                <input value={pass} onChange={(e) => setPass(e.target.value)} name="pass" type="password" placeholder="Enter Your Password" /><br />                                {/* ----- name="pass" -> passing the password to checkFunction()    */}
                {error && <p style={{ color: "red" }}>{error}</p>}                                                           {/* ----- if there is an error, display the error message in red color */}
                {pass && pass.length < 6 && <p style={{ color: "orange" }}>Weak Password</p>}                                                   {/* ----- if there is a password and it is valid, display the success message in green color */}

                <button type="submit">Send Message</button>
            </form>


        </div>
    )

}

export default Contact