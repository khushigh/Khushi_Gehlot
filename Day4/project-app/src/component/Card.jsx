
import { useState } from "react"

function Card({ name, role, city, image, skills }) {
    const [clicked, setClicked] = useState(false)

    return (
        <div className="card">
            <img src={image} alt={name} className="card-image" />
            <div className="card-body">
                <h2 className="card-name">{name}</h2>
                <p className="card-role">{role}</p>
                <p className="card-city"> {city}</p>
                
                
            </div>
        </div>
    )
}

export default Card