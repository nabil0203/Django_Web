

// creating object for each item as array
const todo = [
    {
        id: 1,
        title: "Learn JS",
        completed: false,
    },
    {
        id: 2,
        title: "Building Project",
        completed: true,
    },
    {
        id: 3,
        title: "Learn fundamentals",
        completed: false,
    },
    {
        id: 4,
        title: "DSA",
        completed: false,
    },
];




// DOM
const todoList = document.getElementById("todoList");                   // getting the 'ul' from html
const task = document.getElementById("taskCount");                      // getting the 'task count'
const todoInput = document.getElementById("todoInput");                 // getting the 'user input' from the html input field
const todoForm = document.getElementById("todoForm");                   // getting the full form not the button; bcz When we will click the button, the full form will be submitted
                                                                        // so, we have added an event listener on the form below





function showToDoList() {


    // making the list empty bcz we have a list in html that we don't want in the output
    todoList.innerHTML = "";


    // using loop to get each object of 'todo' one by one
    for (const todoItem of todo) {

        const item = `
                <li class="todo-item">
                    <div class="todo-checkbox ${todoItem.completed ? 'checked' : ''}"></div>                            <!-- if completed then it is checked  -->
                    <span class="todo-text">${todoItem.title}</span>                                                    <!--each title print -->
                    <button class="delete-btn">x</button>
                </li>
            `
        todoList.innerHTML = item + todoList.innerHTML;                                                               // adding with the previous items each time
    }



    // task count part
    task.innerHTML = todo.length + " Tasks";                            // the length of the array = number of tasks


}




// calling the function
showToDoList();




// event listener
todoForm.addEventListener("submit", e => {

    e.preventDefault();                             // this line is used to prevent loading the full page


    const val = todoInput.value;                    // when the button is clicked, here we are getting the element that is caught by DOM and storing it in a variable


    // now pushing in the array as an object
    todo.push({

        id : todo.length + 1,
        title: val,
        completed: false,

    });


    // calling the function to add in the array
    showToDoList();



    // when the button is clicked this will make the input field empty
    todoInput.value = "";                   


})


