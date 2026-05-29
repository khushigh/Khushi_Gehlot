import ProfileCard from "./ProfileCard";
import profiles from "../data/profiles";

function ProfileList() {
  return (
    <div className="gallery">
      {profiles.map((profile) => (
        <ProfileCard
          key={profile.id}
          name={profile.name}
          role={profile.role}
          image={profile.image}
        />
      ))}
    </div>
  );
}

export default ProfileList;