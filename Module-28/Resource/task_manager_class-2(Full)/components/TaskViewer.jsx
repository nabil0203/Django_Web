import { useState } from "react";
import ModalForm from "./ModalForm.jsx";
import TaskItem from "./TaskItem.jsx";
import ModalUpdateForm from "./ModalUpdateForm.jsx";
import {
  saveTasksToLocalStorage,
  loadTasksFromLocalStorage,
} from "../utils/tasks.js";

function TaskViewer() {
  const [tasks, setTasks] = useState(loadTasksFromLocalStorage());
  const [taskToBeUpdated, setTaskToBeUpdated] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isUpdateModalOpen, setIsUpdateModalOpen] = useState(false);
  function closeModal() {
    setIsModalOpen(false);
  }
  function toggleTask(id) {
    const updatedTasks = tasks.map((task) => {
      if (task.id === id) {
        return { ...task, isCompleted: !task.isCompleted };
      }
      return task;
    });
    setTasks(updatedTasks);
    saveTasksToLocalStorage(updatedTasks);
  }
  function deleteTask(id) {
    const updatedTasks = tasks.filter((task) => task.id !== id);
    setTasks(updatedTasks);
    saveTasksToLocalStorage(updatedTasks);
  }
  function addTask(event) {
    event.preventDefault();
    const tasktitle = event.target.tasktitle.value;
    const taskdescription = event.target.taskdescription.value;
    const taskid = tasks.length + 1;
    const task = {
      id: taskid,
      title: tasktitle,
      description: taskdescription,
      isCompleted: false,
    };
    console.log("Task Added: ", task);
    setTasks([...tasks, task]);
    saveTasksToLocalStorage([...tasks, task]);
    closeModal();
  }
  function openModal(id) {
    const task = tasks.find((task) => task.id === id);
    setTaskToBeUpdated(task);
    setIsUpdateModalOpen(true);
  }
  function updateTask(event) {
    event.preventDefault();
    const tasktitle = event.target.tasktitle.value;
    const taskdescription = event.target.taskdescription.value;
    const updatedTasks = tasks.map((task) => {
      if (taskToBeUpdated.id === task.id) {
        return { ...task, title: tasktitle, description: taskdescription };
      }
      return task;
    });
    setTasks(updatedTasks);
    saveTasksToLocalStorage(updatedTasks);
    setIsUpdateModalOpen(false);
  }
  return (
    <div className="flex flex-col items-center justify-center w-full mt-12">
      <button
        onClick={() => setIsModalOpen(true)}
        className="px-4 py-2 w-fit border bg-amber-500 hover:bg-amber-600 cursor-pointer"
      >
        Add New Task
      </button>
      <div className="my-6 space-y-3">
        {tasks.map((task) => {
          return (
            <TaskItem
              key={task.id}
              task={task}
              deleteTask={deleteTask}
              toggleTask={toggleTask}
              openModal={openModal}
            />
          );
        })}
      </div>
      {isModalOpen ? (
        <ModalForm closeModal={closeModal} addTask={addTask} />
      ) : (
        <></>
      )}
      {isUpdateModalOpen ? (
        <ModalUpdateForm
          updateTask={updateTask}
          task={taskToBeUpdated}
          closeModal={() => setIsUpdateModalOpen(false)}
        />
      ) : (
        <></>
      )}
    </div>
  );
}

export default TaskViewer;
