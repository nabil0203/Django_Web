


//  JSON.stringify() - converting object to string
// 

export function saveTaskToLocalStorage(tasks){
  localStorage.setItem("tasks", JSON.stringify(tasks))
}




// JSON.parse() - converting string to object
// localStorage.getItem("tasks") - getting the tasks from local storage
// || [] - if there is no task in local storage then set it to empty array

export function getTasksFromLocalStorage(){
  return JSON.parse(localStorage.getItem("tasks")) || []
}

