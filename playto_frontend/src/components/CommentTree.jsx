import { api } from "../api";

export default function CommentTree({ comments }) {
  return comments.map(comment => (
    <div key={comment.id} style={{ marginLeft: 20 }}>
      <p>{comment.content}</p>
      <button onClick={() => api.post(`comments/${comment.id}/like/`)}>
        👍 Like Comment
      </button>

      {comment.replies && (
        <CommentTree comments={comment.replies} />
      )}
    </div>
  ));
}
