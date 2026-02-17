import './App.css'
import Courses from './Courses'


function App() {



  /*
  
  ------if else-------
   
  // const isLoggedIn = true;
  const isLoggedIn = false;

  if (isLoggedIn){                      
    return (

    <h1>Welcome</h1>

    )
  } 

  else return(

    <h1>Please Log in</h1>

    )
  */








/*
------Switch Case-------

  const number = 10;


  switch (number) {


    case 10:
      return (
        <h1> The number is TEN </h1>
      )

    case 30:
      return (
        <h1> The number is Thirty </h1>
      )

    case 40:
      return (
        <h1> The number is Forty </h1>
      )

  }

 */










/* 
------------ Operators ----------------


const age = 22;
const gender = 'Male'

return(
  
<div>
{age >=18 && gender == 'Male'  ?  <h1> Can Vote </h1>  : <h1> Age not 18 yet</h1>}
</div>


)



*/














/*
--------- Immediately invoke Function------------


const age = 10
const age2 = '10'

return (
  <div>
  
  {(function() {
    
  return age === age2 ? <p>Access given</p> : <p>Access Denied</p>
  
  })()};

</div>

)


*/











/* 
--------- Component Parameter Passing -----------


const courses = ['C', 'C++', 'Python']


return(
  
<div>

{courses.map((course) => (
  < Courses name={course} />                  // 'name' is the parameter 
  // that is passing the values of the array to 'Courses.jsx' component
)
)
}

</div>


)



*/













/*
-------- Event Listener -------------------
*/



const courses = ['C', 'C++', 'Python']


return(

  <div>

    {courses.map((course) => (
        < Courses name={course} />
      )
    )
    }

  </div>


)



}

export default App
