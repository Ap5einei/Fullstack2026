import useCount from './hook/useCount.tsx'

function App() {
  const [count, add, subtract] = useCount(10);

  return (
    <>
     
      <h2>Current Count: {count}</h2>
      <button onClick={add}>Add</button>
      <button onClick={subtract}>Subtract</button>
    </>
  )
}

export default App
