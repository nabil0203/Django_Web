
/*

function Courses( {name} ){                     // name is the parameter that is catching the value from 'App.jsx'

    return(

        <div>

        Name: {name}                            //returning the value to the 'App.jsx'

        </div>  

    )

}

export default Courses


*/










// event listener

function Courses( { name } ){

    function handleEnroll() {
        alert(`You have enrolled in ${name} course.`)
    }
    

    return (
        <div className="border p-4 bg-gray-50 rounded-sm my-4 flex justify-between items-center">
            <span>Name: {name}</span>
            
            <button onClick={handleEnroll} className="bg-red-500 text-white p-2">Enroll</button>
        </div>
    
    )
}

export default Courses