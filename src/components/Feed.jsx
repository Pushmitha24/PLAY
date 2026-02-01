import { useEffect, useState } from "react";
import { api } from "../api";
import PostCard from "./PostCard";

export default function Feed() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    api.get("posts/").then(res => setPosts(res.data));
  }, []);

  return (
    <div>
      {posts.map(post => (
        <PostCard key={post.id} post={post} />
      ))}
    </div>
  );
}
