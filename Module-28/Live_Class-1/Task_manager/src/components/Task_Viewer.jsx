import { useState } from "react"
import ModalForm from "./ModalForm"
import TaskItem from "./TaskItem"


function Task_Viewer() {


  // useState for Modals
  const [isModalOpen, setIsModalOpen] = useState(false)                       // isModalOpen - true -> Show Modal |  isModalOpen - False -> Son't Show Modal


  const [tasks, setTask] = useState([])                                       // initially empty array for the tasks


  function closeModal(){
    setIsModalOpen(false)
  }


  function addTask(event){
  
    event.preventDefault()

    const taskTitle = event.target.taskTitle.value                                       // catching the "event" in task variable
    const taskDescription = event.target.taskDescription.value                           // catching the "event" in description variable
    const taskId = tasks.length + 1

    
    const taskObj = {                                                               // creating an object for the task
      id: taskId,
      title: taskTitle,
      description: taskDescription
    }  
    
    
    console.log("Task Added: ",taskObj)                                           // print in console

    setTask([...tasks, taskObj])                                                  // showing the tasks in list


    setIsModalOpen(false)                                                         // closing the modal
  }




  return (

    <div className="flex flex-col items-center justify-center w-full mt-24">


      {/* On click -> the modal will be opened */}
      <button onClick={()=>setIsModalOpen(true)} className="w-fit px-4 py-2 border-2 rounded-xl bg-amber-500 hover:bg-amber-600 cursor-pointer">
        Add New Task
      </button>
     


      {/* if modal is opened -> show the ModalForm component */}
      {isModalOpen && <ModalForm closeModal={closeModal} addTask={addTask} />}                    {/* passing parameters */}




      {/* Show Tasks */}
      <div className="my-6 space-y-3">
        {tasks.map((task)=>{
          return <TaskItem key={task.id} task={task} />
        })}

        
      </div>


    </div>
      
    )
}

export default Task_Viewer