import './App.css';
import ControlledForm from './components/ControlledForm';
import Counter from './components/Counter';
import { useState, useEffect } from 'react';


function App() {
  // Toggle
  const [isOn, setIsOn] = useState(false);

  // API Data
  const [users, setUsers] = useState([]);

  useEffect(() => {

    fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      .then((data) => setUsers(data));

  }, []);
  return (
   <><div className="App">
      <Counter />
      <ControlledForm />
    </div>
    <h2>Toggle</h2><button onClick={() => setIsOn(!isOn)}>
        {isOn ? "ON" : "OFF"}
      </button>

      {/* API Fetch */ }
  <h2>Users Data</h2>

  {
    users.map((user) => (
      <p key={user.id}>{user.name}</p>
    ))
  }
  </>
 );
}

export default App;
