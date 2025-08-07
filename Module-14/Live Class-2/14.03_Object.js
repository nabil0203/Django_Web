// 34:00

// Object of JS is same as Dictionary of Python by syntax


const Student = {
    first_name: "John",
    age: 30,
    nationality: "Bangladeshi",
    city: "Dhaka",
}


console.log(Student);                                   // accessing full object
console.log(Student["first_name"]);                     // accessing 1 element
console.log(Student.age);                               // accessing 1 element



Student.first_name = "Trump";                       // updating 1 value
console.log(Student);


delete Student.age;                             // using delete keyword to delete 1 property of the object
console.log(Student);

