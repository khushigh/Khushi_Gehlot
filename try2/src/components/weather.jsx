import { useState, useEffect } from "react"
// weather, loading, error store karne ke liye
// component mount hone pe API call karne ke liye

function Weather() {
    const [weather, setWeather] = useState(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)

    useEffect(() => {
        fetchWeather()
    }, [])

    async function fetchWeather() {
        try {
            setLoading(true)
            const response = await fetch(
                "https://api.open-meteo.com/v1/forecast?latitude=28.6&longitude=77.2&current_weather=true"
            )
            if (!response.ok) throw new Error("Failed!")
            const data = await response.json()
            setWeather(data.current_weather)
            setError(null)
        } catch (err) {
            setError("Could not load weather!")
        } finally {
            setLoading(false)
        }
    }

    if (loading) return (
        <div className="weather-widget">Loading weather...</div>
    )

    if (error) return (
        <div className="weather-widget error-box">❌ {error}</div>
    )

    return (
        <div className="weather-widget">
            <span>📍 Delhi</span>
            <span>🌡️ {weather.temperature}°C</span>
            <span>💨 {weather.windspeed} km/h</span>
            <span>{weather.is_day ? "☀️ Day" : "🌙 Night"}</span>
        </div>
    )
}

export default Weather