import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample data
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6],
    'movie_id': [101, 102, 103, 101, 104, 101, 103, 105, 102, 103, 104, 105, 106, 107, 108, 106, 109, 110],
    'rating': [5, 4, 3, 5, 2, 4, 5, 3, 2, 4, 5, 3, 5, 4, 4, 4, 5, 3]
}

# Movie names
movies = {
    101: "The Shawshank Redemption",
    102: "The Godfather",
    103: "The Dark Knight",
    104: "Pulp Fiction",
    105: "The Lord of the Rings: The Return of the King",
    106: "Forrest Gump",
    107: "Inception",
    108: "Fight Club",
    109: "The Matrix",
    110: "Goodfellas"
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a pivot table
pivot_table = df.pivot_table(index='user_id', columns='movie_id', values='rating')

# Fill NaN with 0s
pivot_table.fillna(0, inplace=True)

# Compute the cosine similarity matrix
cosine_sim_matrix = cosine_similarity(pivot_table)

# Create a function to recommend movies based on user similarity
def recommend_movies(user_id, num_recommendations=3):
    # Get the index of the user
    user_idx = pivot_table.index.tolist().index(user_id)

    # Compute the similarity scores for the user
    similarity_scores = cosine_sim_matrix[user_idx]

    # Get the indices of the most similar users
    similar_user_indices = similarity_scores.argsort()[::-1][1:]  # exclude the user itself

    # Get the movie ids that the similar users have rated highly
    movie_recommendations = {}
    for idx in similar_user_indices:
        similar_user_id = pivot_table.index[idx]
        recommended_movies = df[(df['user_id'] == similar_user_id) & (df['rating'] >= 4)]['movie_id'].tolist()
        for movie in recommended_movies:
            if movie not in movie_recommendations:
                movie_recommendations[movie] = similarity_scores[idx]
            else:
                movie_recommendations[movie] += similarity_scores[idx]

    # Remove the movies the user has already seen
    user_seen_movies = df[df['user_id'] == user_id]['movie_id'].tolist()
    for movie in user_seen_movies:
        if movie in movie_recommendations:
            del movie_recommendations[movie]

    # Sort the recommendations by their score
    sorted_recommendations = sorted(movie_recommendations.items(), key=lambda x: x[1], reverse=True)

    # Return the top N movie names
    return [movies[movie_id] for movie_id, score in sorted_recommendations[:num_recommendations]]

# Example usage
user_id = 1
recommendations = recommend_movies(user_id, num_recommendations=3)
print(f"Recommended movies for user {user_id}: {recommendations}")
