import Feed from "./components/Feed";
import Leaderboard from "./components/Leaderboard";

function App() {
  return (
    <div style={{ padding: 20 }}>
      <h1>Community Feed</h1>
      <Leaderboard />
      <Feed />
    </div>
  );
}

export default App;
