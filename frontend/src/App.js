import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [weather, setWeather] = useState(null);
  //const [tides, setTides] = useState(null);

  useEffect(() => {
    // Example coordinates (you might want to use geolocation or let users input this)
    const lat = '-33.719276';
    const lon = '18.455871';

    fetch(`http://127.0.0.1:5000/api/weather/${lat}/${lon}`)
      .then(response => response.json())
      .then(data => setWeather(data));

    
  }, []);

  return (
    <div className="App">
      <h1>Surf Quality Prediction App</h1>
      {weather && (
        <div>
          <h2>Weather</h2>
          <p>Temperature: {weather.main.temp}°C</p>
          <p>Wind Speed: {weather.wind.speed} m/s</p>
        </div>
      )}
      {/* {tides && (
        <div>
          <h2>Tides</h2>
           <p>Next high tide: {new Date(tides.heights[0].dt).toLocaleString()}</p>
        </div>
      )} 
      */}
    </div>
  );
}

export default App;