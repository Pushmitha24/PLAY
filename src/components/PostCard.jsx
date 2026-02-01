import { api } from "../api";
import CommentTree from "./CommentTree";

export default function PostCard({ post }) {
  const likePost = () => {
    api.post(`posts/${post.id}/like/`);
  };

  return (
    <div style={{ border: "1px solid #ccc", margin: 10, padding: 10 }}>
      <p>{post.content}</p>
      <button onClick={likePost}>👍 Like Post</button>

      <CommentTree comments={post.comments} />
    </div>
  );
}
