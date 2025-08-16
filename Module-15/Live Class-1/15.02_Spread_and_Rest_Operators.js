// 22:00

// (...) -> this 3 dots works as operator




// Spread
// Spread operator combines the elements of multiple array or oject


let a = [1, 3];
let b = [5, 7];


// let combined = [a, b];                           // this will combine the arrays as array in a big array
let combined = [...a, ...b];                        // this will combine the arrays as elements one by one

console.log(combined);



// main use in copy an array

let x = [1, 3, 9];
let copy = [...x];

copy[2] = 333;


console.log(x);
console.log(copy);




// -------------------------------------------------------------------




// Rest
// Rest operator collects multiple elements into an array
// (opposite of Spread)


function ConvertToArray(...numbers) {
    
    return numbers
}


let arr = ConvertToArray(22, 55, 34, 76, 12);               // taking each element as parameter and returning it as a whole array

console.log(arr)

