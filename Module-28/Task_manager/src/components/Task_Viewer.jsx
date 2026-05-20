import { useState } from "react"
import ModalForm from "./ModalForm"
import Task_Item from "./Task_Item"
import { saveTaskToLocalStorage, getTasksFromLocalStorage } from "../utils/tasks"


function Task_Viewer() {


  // useState for Modals
  const [isModalOpen, setIsModalOpen] = useState(false)                                  // isModalOpen - true -> Show Modal |  isModalOpen - False -> Son't Show Modal


  const [tasks, setTask] = useState(getTasksFromLocalStorage())                         // tasks - state variable for storing the tasks | setTask - function to update the tasks | getTasksFromLocalStorage() - function to get the tasks from local storage and set it as initial value of tasks




  function closeModal(){
    setIsModalOpen(false)
  }




  function addTask(event){
  
    event.preventDefault()

    const taskTitle = event.target.taskTitle.value                                       // catching the "event" in task variable
    const taskDescription = event.target.taskDescription.value                           // catching the "event" in description variable
    const taskId = tasks.length + 1                                                      // creating a unique id for the task (length of tasks + 1)                 

    
    const taskObj = {                                                               // creating an object for each task
      id: taskId,
      title: taskTitle,
      description: taskDescription,
      isCompleted: false
    }  
    
    
    // console.log("Task Added: ",taskObj)                                                // print in console

    setTask([...tasks, taskObj])                                                      // showing the tasks in list


    saveTaskToLocalStorage([...tasks, taskObj])                                       // saving the tasks in local storage


    closeModal()                                                                      // closing the modal
  }




  function toggleTaskCompletion(id){

    // find the task with the given id with map

    const updatedTasks = tasks.map((task) => {
      if(task.id === id){
        return {...task, isCompleted: !task.isCompleted}                                  // if the task is completed -> make it uncompleted || if the task is uncompleted -> make it completed
      }

      return task;

    });

    setTask(updatedTasks);
    saveTaskToLocalStorage(updatedTasks);

  }




  function deleteTask(id){

    const updatedTasks = tasks.filter((task) => task.id !== id)                         // filtering out the task with the given id; filtering all the tasks without the task which we want to delete

    setTask(updatedTasks)                                                               // updating the tasks in state

    saveTaskToLocalStorage(updatedTasks)                                                // saving the updated tasks in local storage
  }



  






  return (

    <div className="flex flex-col items-center justify-center w-full mt-24">


      {/* On click -> the modal will be opened */}
      <button onClick={()=>setIsModalOpen(true)} className="w-fit px-4 py-2 border-2 rounded-xl bg-amber-500 hover:bg-amber-600 cursor-pointer">
        Add New Task
      </button>
     


      {/* if modal is opened -> show the ModalForm component */}
      {isModalOpen ? <ModalForm closeModal={closeModal} addTask={addTask} /> : null }                       {/* passing parameters */}




      {/* Show Tasks */}
      <div className="my-6 space-y-3">
        {tasks.map((task)=>{

          return <Task_Item key={task.id} task={task} deleteTask={deleteTask} toggleTaskCompletion={toggleTaskCompletion} />

        })}

        
      </div>


    </div>
      
    )
}

export default Task_Viewer