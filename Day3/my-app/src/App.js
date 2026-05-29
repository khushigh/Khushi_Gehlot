import Header from "./components/Header";
import Card from "./components/Card";
import Footer from "./components/Footer";

import "./App.css";

function App() {
  return (
    <div>
      <Header />

      <div className="card-container">
        <Card
          title="React"
          description="React is a JavaScript library for UI."
        />

        <Card
          title="Vite"
          description="Vite provides fast development setup."
        />

        <Card
          title="Props"
          description="Props are used to pass data between components."
        />
      </div>

      <Footer />
    </div>
  );
}

export default App;