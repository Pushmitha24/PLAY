# Playto – Community Feed Prototype
(Threaded Comments + 24h Leaderboard)

---

## 📌 Project Overview

This project is a full-stack **community feed system** built as part of a technical challenge.
It demonstrates handling of:

- Threaded (nested) comments
- Likes on posts and comments
- Karma-based leaderboard
- Rolling 24-hour aggregation
- Concurrency-safe backend logic
- React + Django REST integration

The goal was **correctness, clarity, and real-world backend reasoning**, not UI polish.

---

## 🚀 Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- SQLite

### Frontend
- React
- Axios

---

## ✨ Features Implemented

- Community posts feed
- Unlimited nested (threaded) comments
- Like system for posts and comments
- Karma tracking
- 24-hour rolling leaderboard
- Safe concurrent likes (no duplicates)
- Frontend ↔ backend integration

---

## 📁 Project Structure

```
playto_backend/
├── community/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── playto_backend/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── README.md

playto-frontend/
├── src/
│   ├── components/
│   │   ├── Feed.jsx
│   │   ├── PostCard.jsx
│   │   ├── CommentTree.jsx
│   │   └── Leaderboard.jsx
│   ├── api.js
│   └── App.js
└── package.json
```

---

## ⚙️ How to Run the Project

### Backend Setup

```bash
cd playto_backend
python -m venv venv
venv\Scripts\activate
pip install django djangorestframework
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Backend runs at:
```
http://127.0.0.1:8000
```

---

### Frontend Setup

```bash
cd playto-frontend
npm install
npm start
```

Frontend runs at:
```
http://localhost:3000
```

---

## 🧵 Threaded Comments – Design Explanation

Threaded comments are implemented using a self-referencing foreign key.

Each comment belongs to a post and may optionally reference another comment as its parent,
allowing unlimited nesting without recursive database queries.

---

## ❤️ Likes & Concurrency Safety

- Post Like → **+5 karma**
- Comment Like → **+1 karma**

Concurrency is handled using database-level uniqueness constraints and atomic transactions
to prevent duplicate likes and race conditions.

---

## 🏆 Leaderboard Logic (Last 24 Hours)

The leaderboard is calculated dynamically from a `KarmaTransaction` table.
Only karma earned within the last 24 hours is included.

This avoids cached counters and ensures accurate, real-time rankings.

---

## 🔐 Authentication Note

Authentication was intentionally excluded to focus on backend design and correctness.
Likes are attributed to a default user for demonstration purposes.

In a production system, this would be replaced with token-based authentication (JWT).

---

## 🧪 How to Test

1. Create users, posts, and comments via Django Admin
2. Open the frontend
3. Like posts and comments
4. Observe leaderboard updates

---

## ✅ Project Status

✔ Backend complete  
✔ Frontend complete  
✔ Threaded comments working  
✔ Leaderboard correct  
✔ Ready for evaluation  

---

**Project is complete and ready for review.**
