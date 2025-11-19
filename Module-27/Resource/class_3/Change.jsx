import { useState } from "react";

function Change() {
  const [x, y] = useState(0);

  function handleClick() {
    y(x + 1);
  }

  function handleClick2() {
    if(x===0)return
    y(x - 1);
  }

  return (
    <div>
      <p>{x}</p>
      <button onClick={handleClick}>Increment</button>
      <button onClick={handleClick2}>Decrement</button>
    </div>
  );
}

export default Change;
