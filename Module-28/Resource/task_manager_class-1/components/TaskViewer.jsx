import { useState } from 'react';
import ModalForm from './ModalForm.jsx';
import TaskItem from './TaskItem.jsx';

function TaskViewer() {
    const [tasks, setTasks] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false);
    function closeModal(){
        setIsModalOpen(false);
    }
    function addTask(event){
        event.preventDefault();
        const tasktitle = event.target.tasktitle.value
        const taskdescription = event.target.taskdescription.value
        const taskid = tasks.length + 1;
        const task = {
            id: taskid,
            title: tasktitle,
            description: taskdescription
        }
        console.log("Task Added: ", task);
        setTasks([...tasks, task]);
        closeModal();
    }
  return (
    <div className="flex flex-col items-center justify-center w-full mt-12">
      <button onClick={()=>setIsModalOpen(true)} className="px-4 py-2 w-fit border bg-amber-500 hover:bg-amber-600 cursor-pointer">Add New Task</button>
        <div className='my-6 space-y-3'>
            {tasks.map((task)=>{
                return <TaskItem key={task.id} task={task}/>
            })}
        </div>
        {isModalOpen ? <ModalForm closeModal={closeModal} addTask={addTask} /> : <></>}
    </div>
  );
}

export default TaskViewer;