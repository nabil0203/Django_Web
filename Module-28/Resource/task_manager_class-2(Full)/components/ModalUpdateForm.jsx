function ModalUpdateForm( {closeModal, task, updateTask} ) {
  return (
    <div className="h-screen w-screen bg-gray-200 bg-opacity-5 fixed top-0 left-0 flex justify-center items-center">
        <div className="relative w-1/4 p-4 h-fit bg-gray-100 rounded-md shadow-2xl">
            <div className="absolute right-2 top-2 cursor-pointer text-gray-600" onClick={()=>closeModal()}>X</div>
            <p className="font-bold">Update Task</p>
            <form onSubmit={updateTask} className="py-12">
                <input defaultValue={task.title} name="tasktitle" type="text" placeholder="Task Title" className="w-full px-4 py-2 border rounded-md"/>
                <textarea defaultValue={task.description} name="taskdescription" placeholder="Task Description" className="w-full mt-4 px-4 py-2 border rounded-md"></textarea>
                <input type="submit" value="Update Task" className="w-full mt-4 px-4 py-2 bg-amber-500 hover:bg-amber-600 cursor-pointer rounded-md text-white font-semibold"/>
            </form>
        </div>
    </div>
  )
}

export default ModalUpdateForm