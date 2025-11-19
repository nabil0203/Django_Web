import { useState } from "react";

function Fruits() {
  const [fruits, setFruits] = useState(["Mango", "Banana", "Orange"]);

  function handleAddFruit(event) {
    event.preventDefault();
    const newFruit = event.target.newfruit.value;
    setFruits([...fruits, newFruit]);
  }

  function handleDeleteFruit(fruitToDelete) {
    const updatedFruits = fruits.filter((fruit) => fruit !== fruitToDelete);
    setFruits(updatedFruits);
  }

  return (
    <div>
      <p>Fruits Component</p>
      {fruits.map((fruit) => (
        <div style={{ display: "flex", alignItems: "center" }}>
          <p>{fruit}</p>
          <button onClick={() => handleDeleteFruit(fruit)}>Delete</button>
        </div>
      ))}
      <form onSubmit={handleAddFruit}>
        <input name="newfruit" type="text" placeholder="Enter fruit name" />
        <button type="submit">Add Fruit</button>
      </form>
    </div>
  );
}

export default Fruits;
