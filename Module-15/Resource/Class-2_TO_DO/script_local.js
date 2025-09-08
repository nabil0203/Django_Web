// TODO App JavaScript
class TodoApp {
    constructor() {
        this.todos = this.loadTodos();
        this.todoForm = document.getElementById('todoForm');
        this.todoInput = document.getElementById('todoInput');
        this.todoList = document.getElementById('todoList');
        this.taskCount = document.getElementById('taskCount');
        this.emptyState = document.getElementById('emptyState');

        this.initEventListeners();
        this.render();
    }

    // Initialize event listeners
    initEventListeners() {
        this.todoForm.addEventListener('submit', (e) => {
            e.preventDefault();
            this.addTodo();
        });
    }

    // Add a new todo
    addTodo() {
        const text = this.todoInput.value.trim();

        if (!text) return;

        const newTodo = {
            id: Date.now().toString(),
            text: text,
            completed: false,
            createdAt: new Date().toISOString()
        };

        this.todos.unshift(newTodo);
        this.todoInput.value = '';
        this.saveTodos();
        this.render();
    }

    // Toggle todo completion status
    toggleTodo(id) {
        this.todos = this.todos.map(todo =>
            todo.id === id ? { ...todo, completed: !todo.completed } : todo
        );
        this.saveTodos();
        this.render();
    }

    // Delete a todo
    deleteTodo(id) {
        this.todos = this.todos.filter(todo => todo.id !== id);
        this.saveTodos();
        this.render();
    }

    // Save todos to localStorage
    saveTodos() {
        localStorage.setItem('todos', JSON.stringify(this.todos));
    }

    // Load todos from localStorage
    loadTodos() {
        const saved = localStorage.getItem('todos');
        return saved ? JSON.parse(saved) : [];
    }

    // Update task count display
    updateTaskCount() {
        const total = this.todos.length;
        const completed = this.todos.filter(todo => todo.completed).length;
        const remaining = total - completed;

        let countText;
        if (total === 0) {
            countText = 'No tasks';
        } else if (total === 1) {
            countText = remaining === 0 ? '1 task completed' : '1 task';
        } else {
            countText = remaining === 0
                ? `${total} tasks completed`
                : `${remaining} of ${total} tasks`;
        }

        this.taskCount.textContent = countText;
    }

    // Create todo item HTML
    createTodoElement(todo) {
        const li = document.createElement('li');
        li.className = `todo-item ${todo.completed ? 'completed' : ''}`;
        li.setAttribute('role', 'listitem');

        li.innerHTML = `
            <div class="todo-checkbox ${todo.completed ? 'checked' : ''}" 
                 onclick="app.toggleTodo('${todo.id}')"
                 role="checkbox"
                 aria-checked="${todo.completed}"
                 tabindex="0">
            </div>
            <span class="todo-text">${this.escapeHtml(todo.text)}</span>
            <button class="delete-btn" 
                    onclick="app.deleteTodo('${todo.id}')"
                    aria-label="Delete task"
                    title="Delete task">
                ×
            </button>
        `;

        // Add keyboard support for checkbox
        const checkbox = li.querySelector('.todo-checkbox');
        checkbox.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.toggleTodo(todo.id);
            }
        });

        return li;
    }

    // Escape HTML to prevent XSS
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // Render the todo list
    render() {
        // Clear current list
        this.todoList.innerHTML = '';

        // Update task count
        this.updateTaskCount();

        // Show/hide empty state
        if (this.todos.length === 0) {
            this.emptyState.classList.remove('hidden');
        } else {
            this.emptyState.classList.add('hidden');

            // Render todos
            this.todos.forEach(todo => {
                const todoElement = this.createTodoElement(todo);
                this.todoList.appendChild(todoElement);
            });
        }
    }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.app = new TodoApp();
});

// Add some helpful keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // Focus input when pressing 'n' (new task)
    if (e.key === 'n' && !e.ctrlKey && !e.metaKey && e.target.tagName !== 'INPUT') {
        e.preventDefault();
        document.getElementById('todoInput').focus();
    }
});