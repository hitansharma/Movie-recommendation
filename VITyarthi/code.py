import random

movies = {"The Shawshank Redemption": {"genre": ["drama"], "rating": 9.3},
          "The Godfather": {"genre": ["crime", "drama"], "rating": 9.2},
        "The Dark Knight": {"genre": ["action", "thriller"], "rating": 9.0},
        "Pulp Fiction": {"genre": ["crime", "drama"], "rating": 8.9},
        "Forrest Gump": {"genre": ["drama", "romance"], "rating": 8.8},
        "Inception": {"genre": ["action", "sci-fi", "thriller"], "rating": 8.8},
        "The Matrix": {"genre": ["action", "sci-fi"], "rating": 8.7},
        "Interstellar": {"genre": ["sci-fi", "drama"], "rating": 8.6},
        "Goodfellas": {"genre": ["crime", "drama"], "rating": 8.7},
        "Fight Club": {"genre": ["drama", "thriller"], "rating": 8.8},
        "The Silence of the Lambs": {"genre": ["thriller", "crime"], "rating": 8.6},
        "Schindler's List": {"genre": ["drama", "history"], "rating": 9.0},
        "The Lord of the Rings": {"genre": ["fantasy", "adventure"], "rating": 8.9},
        "Star Wars": {"genre": ["sci-fi", "fantasy", "adventure"], "rating": 8.6},
        "Jurassic Park": {"genre": ["sci-fi", "adventure"], "rating": 8.2},
        "Titanic": {"genre": ["drama", "romance"], "rating": 7.9},
        "Avatar": {"genre": ["sci-fi", "adventure"], "rating": 7.9},
        "The Avengers": {"genre": ["action", "adventure"], "rating": 8.0},
        "Toy Story": {"genre": ["animation", "comedy"], "rating": 8.3},
        "Finding Nemo": {"genre": ["animation", "adventure"], "rating": 8.2},
        "The Lion King": {"genre": ["animation", "drama"], "rating": 8.5},
        "Home Alone": {"genre": ["comedy"], "rating": 7.7},
        "The Truman Show": {"genre": ["drama", "comedy"], "rating": 8.2},
        "Gladiator": {"genre": ["action", "drama", "history"], "rating": 8.5},
        "Braveheart": {"genre": ["drama", "history", "action"], "rating": 8.4},}

def get_recommendations(preferred_genres, min_rating=7.5, top_n=5):
    """Recommend movies based on preferred genres and minimum rating."""
    scored = []

    for title, info in movies.items():
        if info["rating"] < min_rating:
            continue
        matches = len(set(preferred_genres) & set(info["genre"]))
        if matches > 0:
            scored.append((title, info["rating"], matches, info["genre"]))

    scored.sort(key=lambda x: (x[2], x[1]), reverse=True)

    return scored[:top_n]

def main():
    print("🎬 Movie Recommendation System")
    print("=" * 40)

    all_genres = sorted(set(g for m in movies.values() for g in m["genre"]))
    print(f"\nAvailable genres: {', '.join(all_genres)}")

    user_input = input("\nEnter your preferred genres (comma-separated): ").strip().lower()
    preferred = [g.strip() for g in user_input.split(",")]

    min_rating = input("Minimum rating (1-10, default 7.5): ").strip()
    min_rating = float(min_rating) if min_rating else 7.5

    recommendations = get_recommendations(preferred, min_rating)

    print(f"\n Top Recommendations for genres: {', '.join(preferred)}")
    print("-" * 40)

    if not recommendations:
        print("No movies found. Try different genres or lower the minimum rating.")
    else:
        for i, (title, rating, matches, genres) in enumerate(recommendations, 1):
            print(f"{i}. {title}")
            print(f"  Rating: {rating} | Genres: {', '.join(genres)}")

if __name__ == "__main__":
    main()
