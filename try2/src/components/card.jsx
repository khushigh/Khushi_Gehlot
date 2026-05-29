import { useState } from "react"

function Card({ name, role, city, image, skills }) {
    const [clicked, setClicked] = useState(false)

    return (
        <div className="card">
            <img src={image} alt={name} className="card-image" />
            <div className="card-body">
                <h2 className="card-name">{name}</h2>
                <p className="card-role">{role}</p>
                <p className="card-city">📍 {city}</p>
                <div className="card-skills">
                    {skills.map((skill, index) => (       // Har skill ke liye ek span
                        <span key={index} className="skill-tag">
                            {skill}
                        </span>
                    ))}
                </div>
                <button
                    className={`view-btn ${clicked ? "clicked" : ""}`} // if clicked = false: className = "view-btn" else className = view-btn clicked
 
                    onClick={() => setClicked(!clicked)}
                >
                    {clicked ? "Added!" : "View Profile"}
                </button>
            </div>
        </div>
    )
}

export default Card