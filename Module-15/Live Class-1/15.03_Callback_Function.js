// 45:20


// we can send a function as a parameter of another function




function sayGoodbye() {
    console.log("Goodbye!");
}


function greet(name, sayGoodbye) {
    console.log("Hello, " + name);
    sayGoodbye();                                   // calling the function which was sent as parameter

}

greet("Alice", sayGoodbye);                         // calling 'greet' with 2 parameter; i)'Alice' as a string & ii)'sayGoodbye' as a function
