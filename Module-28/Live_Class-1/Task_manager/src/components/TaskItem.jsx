function TaskItem({ task }) {

    return (
        <div className="py-2 px-4 w-100 overflow-hidden border border-gray-300 rounded-md">
            
            <p className="font-bold">{task.title}</p>
            <p className="font-normal text-sm">{task.description}</p>

            
        </div>

    )

}

export default TaskItem