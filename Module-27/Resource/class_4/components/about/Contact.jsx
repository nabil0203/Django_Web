import { useState } from "react"

function Contact(){

    const [error, setError] = useState("")
    const [pass, setPass] = useState("")

    function validate(event){
        event.preventDefault()
        if(event.target.pass.value.length < 6){
            setError("Password must be at least 6 characters long")
            return false
        }
        return true
    }

    function onFinish(event){
        event.preventDefault()
        console.log(event.target.pass.value)
        if(validate(event)){
            alert("Form submitted successfully")
            setError("")
        }
    }
    
    return (
        <div>
            <form onSubmit={onFinish}>
                <input type="text" placeholder="Your Name" /><br/>
                <input value={pass} onChange={(e) => setPass(e.target.value)} name="pass" type="password" placeholder="Your Password" /><br/>
                {error && <span style={{color: 'red'}}>{error}</span>}<br/>
                {pass && pass.length < 6 && <span style={{color: 'orange'}}>Password is weak</span>}<br/>
                <textarea placeholder="Your Message"></textarea><br/>
                <button type="submit">Send</button>
            </form>
        </div>
    )
}

export default Contact