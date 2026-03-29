# 🎬 Movie Recommendation System

A simple Python-based movie recommendation system that suggests movies based on your preferred genres and minimum rating threshold.

## Author 

Hitansh Sharma

GitHub:

## Features

- 25 pre-loaded popular movies across multiple genres
- Filter movies by one or more preferred genres
- Set a minimum IMDb-style rating threshold
- Results ranked by genre relevance and rating
- Lightweight — no external dependencies required

---

## Requirements

- Python 3.6 or higher
- No third-party libraries needed

---

## Getting Started

### 1. Clone or Download

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

Or simply download `code.py` directly.

### 2. Run the Script

```bash
python code.py
```

## Usage

When you run the script, it will prompt you for:

1. **Preferred genres** — enter one or more genres separated by commas
2. **Minimum rating** — a number between 1 and 10 (default: 7.5)

### Example

```
🎬 Movie Recommendation System
========================================

Available genres: action, adventure, animation, comedy, crime, drama, fantasy, history, romance, sci-fi, thriller

Enter your preferred genres (comma-separated): action, sci-fi
Minimum rating (1-10, default 7.5): 8.0

🍿 Top Recommendations for genres: action, sci-fi
----------------------------------------
1. Inception
   ⭐ Rating: 8.8 | Genres: action, sci-fi, thriller

2. The Dark Knight
   ⭐ Rating: 9.0 | Genres: action, thriller

3. The Matrix
   ⭐ Rating: 8.7 | Genres: action, sci-fi

4. Interstellar
   ⭐ Rating: 8.6 | Genres: sci-fi, drama

5. The Avengers
   ⭐ Rating: 8.0 | Genres: action, adventure
```

---

## Available Genres

| Genre     | Genre    | Genre   |
|-----------|----------|---------|
| action    | comedy   | history |
| adventure | crime    | romance |
| animation | drama    | sci-fi  |
| fantasy   | thriller |         |

---

## How It Works

1. The system holds a dictionary of movies, each with associated genres and a rating.
2. When you enter preferred genres, it finds all movies that match **at least one** genre.
3. Movies are ranked by:
   - **Genre match count** (more matches = higher priority)
   - **Rating** (higher rating = higher priority among equal matches)
4. The top 5 results are displayed by default.

---

## Extending the Movie Database

To add more movies, edit the `movies` dictionary in `code.py`:

```python
movies = {
    "Your Movie Title": {"genre": ["action", "drama"], "rating": 8.5},
    # ... more movies
}
```

## Project Structure

```
movie-recommender/
│
└── code.py       # Main script with movie database and recommendation logic
└── README.md       # Project documentation



