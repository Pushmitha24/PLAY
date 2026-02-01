import { useEffect, useState } from "react";
import { api } from "../api";

export default function Leaderboard() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    api.get("leaderboard/").then(res => setUsers(res.data));
  }, []);

  return (
    <div>
      <h3>🏆 Top Users (Last 24h)</h3>
      {users.map((u, i) => (
        <p key={i}>
          {u.user__username}: {u.total_karma}
        </p>
      ))}
    </div>
  );
}
