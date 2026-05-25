function TaskItem( { task, deleteTask, toggleTask, openModal } ) {
  
  return (
    <div className="flex justify-between items-center py-2 px-4 w-[400px] overflow-hidden border border-gray-300 rounded-md">
      <div className="flex items-center gap-2">
        <input type="checkbox" checked={task.isCompleted} onChange={()=>toggleTask(task.id)}></input>
        <div>
          <p className={`font-bold ${task.isCompleted ? 'line-through' : ''}`}>{task.title}</p>
          <p className="font-light text-sm">{task.description}</p>
        </div>
      </div>
      <div>
      <button onClick={()=>openModal(task.id)} className="bg-blue-500 text-white cursor-pointer px-2 py-1 rounded">U</button>
      <button onClick={()=>deleteTask(task.id)} className="ml-1 bg-red-500 cursor-pointer text-white px-2 py-1 rounded">D</button>
      </div>
      
      </div>
  )
}

export default TaskItem