function ModalForm({ closeModal, addTask }){

    return(

        <div className="h-screen w-screen fixed top-0 left-0 flex justify-center items-center bg-amber-100 bg-opacity-40">
            
            <div className="relative w-1/4 h-fit p-4 bg-gray-100 rounded-md shadow-2xl border">

                <div className="absolute right-2 top-2 cursor-pointer border px-2 py-1 rounded-md" onClick={()=>closeModal()}> X </div>                                       {/*  By clicking "X" -> close Modal will be called */}

                
                <p className="font-bold text-2xl">Add New Task</p>

                <form onSubmit={addTask} className="py-12 px-6">                                                                                                            {/* arrow function not needed bcz no parameter is passing; this will work after clicking the button*/}

                    <input type="text" name="taskTitle" placeholder="Task Title" className="w-full px-3 py-2 border rounded-xl"/>
                    <textarea name="taskDescription" placeholder="Task Description" className="w-full mt-3 px-3 py-2 border rounded-xl"></textarea>

                    <input type="submit" value="Add Task" className="w-full mt-4 px-4 py-2 bg-amber-500 hover:bg-amber-600 border rounded-xl" />

                </form>

                


            </div>


        </div>

    )
}

export default ModalForm