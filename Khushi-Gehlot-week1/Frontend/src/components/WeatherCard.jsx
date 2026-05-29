import  "./WeatherCard.css";
function WeatherCard({ weather }) {

  return (
    <>
    <div className="card" >

      <h2>{weather.city}</h2>

      <p>
        <strong>Temperature:</strong> {weather.temperature} °C
      </p>

      <p>
        <strong>Humidity:</strong> {weather.humidity}%
      </p>

      <p>
        <strong>Wind Speed:</strong> {weather.wind_speed} m/s
      </p>

    </div>
    </>
  );
}

export default WeatherCard;