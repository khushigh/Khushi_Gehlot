import Card from "./Card"

function Gallery({ profiles }) {
    return (
        <div className="gallery">
            {profiles.map((profile) => (
                // ...profile used to pass all the props in cleaner way
                // as Without spread — tedious = <Card name={profile.name} role={profile.role} city={profile.city} ... />
                <Card key={profile.id} {...profile} />
            ))}
        </div>
    )
}

export default Gallery