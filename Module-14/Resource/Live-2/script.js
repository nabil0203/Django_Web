// const shoppingList = ["milk", "bread", "egg"];
// console.log(shoppingList);

// shoppingList.push("butter");

// console.log(shoppingList);

// shoppingList.pop();
// shoppingList.pop();

// console.log(shoppingList);


// function dbl(item) {
//     return item * 3
// }

// const quantities = [2, 4, 3];

// const doubledQuantities = quantities.map(item => item * 2);
// const doubledQuantities = quantities.map(dbl);
// console.log(doubledQuantities);

// Objects
// student = {
//     name: "Rohan",
//     age: 22,
//     nationality: "Bangladeshi",
//     city: "Rangpur",
// }
// console.log(student);
// console.log(student["city"])
// console.log(student.name)

// student.name = "Mr Rohan"
// console.log(student);

// delete student.age;
// console.log(student);



// DOM - Document Object Model

// console.log(document);
// console.log(
//     document.querySelectorAll(".cls")
// );

// const hahahaItem = document.querySelector(".cls");
// console.log(hahahaItem);

// console.log(hahahaItem.textContent)
// console.log(hahahaItem.innerHTML)




// const abcDiv = document.querySelector("#abc");
// console.log(abcDiv);

// console.log(abcDiv.textContent)
// console.log(abcDiv.innerHTML)

// abcDiv.textContent = "Hihihi"
// console.log(abcDiv)

// abcDiv.innerHTML = "<h1>Hihihi</h1>"



// const hiDiv = document.querySelector("h1");
// console.log(hiDiv);

// hiDiv.addEventListener("mouseover", e => {
//     hiDiv.textContent = "Bye";
// });

// hiDiv.addEventListener("mouseleave", (e) => {
//     // hiDiv.textContent = "Hi";
//     e.target.textContent = "Hi";
// });




function nice() {
    console.log(new Date())
}

console.log("Started...")

// const tId = setTimeout(nice, 1000 * 1);

// clearTimeout(tId);

// document.querySelector("button").addEventListener("click", (e) => {
//     clearTimeout(tId);
// })

// const iId = setInterval(nice, 1000 * 1);
// // clearInterval(iId);

// document.querySelector("button").addEventListener("click", (e) => {
//     clearInterval(iId);
// })

