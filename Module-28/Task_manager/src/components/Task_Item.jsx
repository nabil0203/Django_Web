import { useState } from "react";
import ModalUpdateForm from "./ModalUpdateForm";


function Task_Item({ task, deleteTask, toggleTaskCompletion }){


    const [isUpdateModalOpen, setIsUpdateModalOpen] = useState(false);


    return (
        <div className="flex justify-between py-2 px-4 w-100 overflow-hidden border border-gray-300 rounded-md">
            
            <div className="flex items-center gap-4">

                <input type="checkbox" checked={task.isCompleted} onChange={() => toggleTaskCompletion(task.id)} ></input>                                              {/*------ when task is completed, show check mark ------*/}
                <div>
                    <p className={`font-bold ${task.isCompleted ? 'line-through' : ''}`}> {task.title} </p>

                    <p className="font-normal text-sm">{task.description}</p>
                </div>

            </div>

            <div className="flex gap-2">
                <button onClick={()=>setIsUpdateModalOpen(true)} className="bg-blue-400 hover:bg-blue-500 text-white px-3 py-1 rounded-xl cursor-pointer">
                    Edit
                </button>

                <button onClick={() => deleteTask(task.id)} className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded-xl cursor-pointer">
                    Delete
                </button>


               {isUpdateModalOpen ? <ModalUpdateForm task={task} closeModal={() => setIsUpdateModalOpen(false)} /> : null}                                  {/*   if isUpdateModalOpen is true -> show ModalUpdateForm component */}


            </div>
        </div>

    )

}

export default Task_Item