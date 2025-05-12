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
      <h1>Python project .....</h1>
      <h2>i am sonali</h2>
   
   
    </>
  )
}

export default App
