let todos = [
    // {
    //     id: 1,
    //     title: "Learn Javascript",
    //     completed: false,
    // },
    // {
    //     id: 2,
    //     title: "Build a Project",
    //     completed: true,
    // },
    // {
    //     id: 3,
    //     title: "Practice Coding",
    //     completed: false,
    // },
    // {
    //     id: 4,
    //     title: "Practice Python",
    //     completed: false,
    // },
]


const todoListEl = document.getElementById("todoList");
const taskCountEl = document.getElementById("taskCount");
const todoInputEl = document.getElementById("todoInput");
const todoFormEl = document.getElementById("todoForm");

function showTodoList() {
    todoListEl.innerHTML = "";

    taskCountEl.innerHTML = todos.length + " tasks";

    for (const todoItem of todos) {
        const item = `
        <li class="todo-item ${todoItem.completed ? 'completed' : ''}">
            <div class="todo-checkbox ${todoItem.completed ? 'checked' : ''}"></div>
            <span class="todo-text">${todoItem.todo}</span>
            <button class="delete-btn">x</button>
        </li>
    `
        todoListEl.innerHTML = item + todoListEl.innerHTML;
    }
}

showTodoList();

todoFormEl.addEventListener("submit", e => {
    e.preventDefault();

    const val = todoInputEl.value;

    const o = {
        todo: val,
        completed: false,
        userId: 5,
    }

    fetch("https://dummyjson.com/todos/add", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(o),
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });

    todos.push(o);

    showTodoList();

    todoInputEl.value = "";
});


fetch("https://dummyjson.com/todos")
    .then(response => response.json())
    .then(data => {
        console.log(data);
        todos = data.todos;
        showTodoList();
    })
    .catch(error => {
        console.error(error);
        alert("Something is wrong!");
    });


// const a = x => x * 2

// a(2)

// const b = a

// b(2)
