import './App.css'
import Change from './Change'
import RefDemo from './RefDemo'
import ImmutDemo from './ImmutDemo'
import Fruits from './Fruits'

function App() {
  return (
    <div>
      <h1>React Hooks & State Management</h1>
      <Change />
      <RefDemo/>  
      <ImmutDemo/>
      <Fruits/>
    </div>
  )
}

export default App