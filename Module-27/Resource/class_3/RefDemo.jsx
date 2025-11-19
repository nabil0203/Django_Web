import { useRef } from "react";

function RefDemo() {
  const textRef = useRef(null);

function handleClick() {
    // textRef.current.innerText = "Text changed!";
    textRef.current.innerHTML = "<strong>HTML changed!</strong>";
    textRef.current.style.color = "red"
}

  return <div>
    <p ref={textRef}>Original text content</p>
    <button onClick={handleClick}>Change Text</button>
  </div>;
}

export default RefDemo;