import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

movies = pd.read_csv('ml-latest-small/ml-latest-small/movies.csv')
ratings = pd.read_csv('ml-latest-small/ml-latest-small/ratings.csv')


print(movies.head())
print(ratings.head())

movies.dropna(inplace=True)
ratings.dropna(inplace=True)

user_movie_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')

from sklearn.metrics.pairwise import cosine_similarity

user_movie_matrix.fillna(0, inplace=True)

movie_similarity = cosine_similarity(user_movie_matrix.T)

movie_similarity_df = pd.DataFrame(movie_similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

def recommend_movies(movie_id, num_recommendations=5):
    similar_scores = movie_similarity_df[movie_id].sort_values(ascending=False)
    recommended = similar_scores.iloc[1:num_recommendations+1].index
    return movies[movies['movieId'].isin(recommended)]['title']

print(recommend_movies(1))

