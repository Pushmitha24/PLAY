# Explainer – Playto Community Feed Challenge

This document explains the key architectural and technical decisions made while building the Community Feed with threaded comments and a 24-hour leaderboard.

---

## 1. The Tree: Modeling Threaded Comments

### Database Modeling

Threaded comments were implemented using an **adjacency list pattern**.

Each `Comment` has:
- a foreign key to `Post`
- a self-referencing foreign key `parent` (nullable)

```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="_
