import { useState } from "react"
import profiles from "./data"
import Gallery from "./components/Gallery"
import Weather from "./components/Weather"

function App() {
    const [search, setSearch] = useState("")  // typed inside the search box
    const [selectedCity, setSelectedCity] = useState("All") // dropdown to select city
    const [sortAZ, setSortAZ] = useState(false) // sort button on/off
    const [darkMode, setDarkMode] = useState(false) // dark mode on/off

    // Unique cities list by set removing duplicates
    // ... spread operator = Set ko array mein convert karo
    const cities = ["All", ...new Set(profiles.map(p => p.city))]

    // Filter + Sort logic
    let filteredProfiles = profiles.filter((profile) => {
        const matchesSearch =
            profile.name.toLowerCase().includes(search.toLowerCase()) ||
            profile.role.toLowerCase().includes(search.toLowerCase()) ||
            profile.city.toLowerCase().includes(search.toLowerCase())

        const matchesCity =
            selectedCity === "All" || profile.city === selectedCity

        return matchesSearch && matchesCity
    })

    // Sort A-Z
    if (sortAZ) {
        filteredProfiles = [...filteredProfiles].sort((a, b) =>
            a.name.localeCompare(b.name)  // localeCompare — strings compare karta hai alphabetically
        )
    }

    // if darkMode = false then className = "app" else className = "app dark"
    return (
        <div className={`app ${darkMode ? "dark" : ""}`}>
            <header className="header">
                <h1>👥 Profile Gallery</h1>
                <p>{filteredProfiles.length} team members</p>

                {/* Weather */}
                <Weather />

                {/* Search Box */}
                <input
                    type="text"
                    className="search-box"
                    placeholder="Search by name, role or city..."
                    value={search} // Input ki value hamesha search state ke equal hai
                    onChange={(e) => setSearch(e.target.value)}
                />

                {/* Controls Row */}
                <div className="controls">
                    {/* City Dropdown */}
                    <select
                        className="city-select"
                        value={selectedCity}
                        onChange={(e) => setSelectedCity(e.target.value)}
                    >
                        {cities.map((city) => (
                            <option key={city} value={city}>
                                📍 {city}
                            </option>
                        ))}
                    </select>

                    {/* Sort Button */}
                    <button
                        className={`sort-btn ${sortAZ ? "active" : ""}`}
                        onClick={() => setSortAZ(!sortAZ)} // !sortAZ — toggle:
                    >
                        {sortAZ ? "A-Z" : "Sort A-Z"}
                    </button>

                    {/* Dark Mode */}
                    <button
                        className="dark-btn"
                        onClick={() => setDarkMode(!darkMode)}
                    >
                        {darkMode ? "☀️ Light" : "🌙 Dark"}
                    </button>
                </div>
            </header>

            {filteredProfiles.length === 0 ? (
                <p className="no-results">
                    No profiles found for "{search}"
                </p>
            ) : (
                <Gallery profiles={filteredProfiles} />
            )}
        </div>
    )
}

export default App