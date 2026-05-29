function ProfileCard({ name, role, image }) {
  return (
    <div className="card">
      <img src={image} alt={name} />

      <h2>{name}</h2>

      <p>{role}</p>

      <button>View Profile</button>
    </div>
  );
}

export default ProfileCard;