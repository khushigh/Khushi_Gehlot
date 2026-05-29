// import { useState } from "react";
// import WeatherCard from "./components/WeatherCard";
// import "./App.css";

// function App() {

//   const [city, setCity] = useState("");
//   const [weather, setWeather] = useState(null);
//   const [error, setError] = useState("");

//   const getWeather = () => {

//     fetch(`http://127.0.0.1:5000/weather?city=${city}`)
//       .then((response) => response.json())
//       .then((data) => {

//         if (data.error) {
//           setError(data.error);
//           setWeather(null);
//         }

//         else {
//           setWeather(data);
//           setError("");
//         }
//       })

//       .catch(() => {
//         setError("Failed to fetch weather data");
//       });
//   };

//   return (

//     <div className="app">

//       <h1>Weather App</h1>

//       <input
//         type="text"
//         placeholder="Enter city"
//         value={city}
//         onChange={(e) => setCity(e.target.value)}
//       />

//       <button onClick={getWeather}>
//         Search
//       </button>

//       {error && <p>{error}</p>}

//       {weather && <WeatherCard weather={weather} />}

//     </div>
//   );
// }

// export default App;


// Project: Build a small app that fetches from a public API and displays
// results, with loading and error states.
// 4:30–6:00 Practice: Add a search/filter box. Lift state up where needed. Handle
// empty results gracefully.xx