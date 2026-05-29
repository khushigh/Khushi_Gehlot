import { useState } from "react"
import profiles from "./data"
import Gallery from "./component/Gallery"


function App() {
  const [search, setSearch] = useState("")
  const [selectedrole, setSelectedrole] = useState("All")
  const [sortAZ, setSortAZ] = useState(false)

  const roles = ["All", ...new Set(profiles.map(p => p.role))]


  let filteredProfiles = profiles.filter((profile) => {
    const matchesSearch =
      profile.name.toLowerCase().includes(search.toLowerCase())

    const matchesrole =
      selectedrole === "All" || profile.role === selectedrole

    return matchesSearch && matchesrole
  })
  return (
    <div className="app">
      <header className="header">
        <h1> Profile List</h1>



        <div className="controls">

          <select
            className="role-select"
            value={selectedrole}
            onChange={(e) => setSelectedrole(e.target.value)}
          >
            {roles.map((role) => (
              <option key={role} value={role}>
                {role}
              </option>
            ))}
          </select>
          <input
            type="text"
            className="search-box"
            placeholder="Search by name"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />


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