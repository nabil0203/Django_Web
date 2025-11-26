import Contact from "./Contact"
import { useState, useMemo } from "react"

function About(){
    const [arr, setArr] = useState(['dsa'])
    const l = useMemo(()=>arr.length, [arr])
    return (
        <div>
            This is an about page

            <Contact />

            {l}
        </div>
    )
}

export default About