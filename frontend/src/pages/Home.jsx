import Navbar from "../components/Navbar";
import PromptBox from "../components/PromptBox";

function Home() {
  return (
    <>
      <Navbar />

      <div className="container">

        <div className="card">

          <h1 className="title">
            StratOS
          </h1>

          <p className="subtitle">
            Enterprise Strategy Intelligence Platform
          </p>

          <PromptBox />

        </div>

      </div>
    </>
  );
}

export default Home;