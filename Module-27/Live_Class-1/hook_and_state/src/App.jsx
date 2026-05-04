import './App.css'
import Use_state_hook from './Use_state_hook'
import Use_ref_hook from './Use_ref_hook'
import Immutable_Object from './Immutable_Object'
import Immutable_Array from './Immutable_Array'


function App() {

  return (
    <>
    <div>


      <h1>use State Hook</h1>
      <Use_state_hook />



      <h1>use Ref Hook</h1>
      <Use_ref_hook />

      

      <h1>Immutable Object</h1>
      <Immutable_Object />



      <h1>Immutable Array</h1>
      <Immutable_Array />

    </div>
    </>
  )
}

export default App
