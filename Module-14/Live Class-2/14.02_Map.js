// 27:10

// map gives every item of an array one by one


// example-1
const numbers = [4, 9, 16, 25];                 
 
const newArr = numbers.map(Math.sqrt);          // taking each element of the numbers array by map and using 'Math.sqrt' to square root them

console.log(newArr);







// example-2
const arr1 = [65, 44, 12, 4];

function double_function(num) {
  return num * 2;
}

const double_number = arr1.map(double_function);            // 'arr1'-array is passing it's each element by map into the 'double_function'. Then storing in 'double_number' one by one.

console.log(double_number);





// example-3
// same concept as example-2
// used arrow function instead of regular function



const arr2 = [65, 44, 12, 4];

// function double_function1(num) {
//   return num * 2;
// }

const double_number2 = arr2.map(arr2 => arr2 * 2);                // arrow function

console.log(double_number2);


