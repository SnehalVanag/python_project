import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import MarketingDashboard from './Marketing/MarketingDashboard'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
    <MarketingDashboard />
      </div>
     
   
   
    </>
  )
}

export default App
