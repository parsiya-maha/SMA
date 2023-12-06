import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os
warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(r"D:\Parsia Works\python\Project\AI\RecommendationSystem")

def recommendation_system(user_id,rating_path:str,movies_path:str,k=10):
    #loading rating dataset
    ratings = pd.read_csv(rating_path)

    movies = pd.read_csv(movies_path)

    user_freq = ratings[['userId', 'movieId']].groupby(
        'userId').count().reset_index()
    user_freq.columns = ['userId', 'n_ratings']

    # Find Lowest and Highest rated movies:
    mean_rating = ratings.groupby('movieId')[['rating']].mean()
    # Lowest rated movies
    lowest_rated = mean_rating['rating'].idxmin()
    movies.loc[movies['movieId'] == lowest_rated]
    # Highest rated movies
    highest_rated = mean_rating['rating'].idxmax()
    movies.loc[movies['movieId'] == highest_rated]
    # show number of people who rated movies rated movie highest
    ratings[ratings['movieId']==highest_rated]
    # show number of people who rated movies rated movie lowest
    ratings[ratings['movieId']==lowest_rated]
    
    ## the above movies has very low dataset. We will use bayesian average
    movie_stats = ratings.groupby('movieId')[['rating']].agg(['count', 'mean'])
    movie_stats.columns = movie_stats.columns.droplevel()

    # Now, we create user-item matrix using scipy csr matrix
    from scipy.sparse import csr_matrix
    
    def create_matrix(df):
        
        N = len(df['userId'].unique())
        M = len(df['movieId'].unique())
        
        # Map Ids to indices
        user_mapper = dict(zip(np.unique(df["userId"]), list(range(N))))
        movie_mapper = dict(zip(np.unique(df["movieId"]), list(range(M))))
        
        # Map indices to IDs
        user_inv_mapper = dict(zip(list(range(N)), np.unique(df["userId"])))
        movie_inv_mapper = dict(zip(list(range(M)), np.unique(df["movieId"])))
        
        user_index = [user_mapper[i] for i in df['userId']]
        movie_index = [movie_mapper[i] for i in df['movieId']]
    
        X = csr_matrix((df["rating"], (movie_index, user_index)), shape=(M, N))
        
        return X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper
        
    X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper = create_matrix(ratings)

    """
    Find similar movies using KNN
    """
    def find_similar_movies(movie_id, X, k, metric='cosine', show_distance=False):
        
        neighbour_ids = []
        
        movie_ind = movie_mapper[movie_id]
        movie_vec = X[movie_ind]
        k+=1
        kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
        print(30*'-')
        print(type(X))
        print(30*'-')
        kNN.fit(X)
        movie_vec = movie_vec.reshape(1,-1)
        neighbour = kNN.kneighbors(movie_vec, return_distance=show_distance)
        for i in range(0,k):
            n = neighbour.item(i)
            neighbour_ids.append(movie_inv_mapper[n])
        neighbour_ids.pop(0)
        return neighbour_ids
    
    





    def recommend_movies_for_user(user_id, X, user_mapper, movie_mapper, movie_inv_mapper, k=10):
        df1 = ratings[ratings['userId'] == user_id]
        
        if df1.empty:
            return f"User with ID {user_id} does not exist."

        movie_id = df1[df1['rating'] == max(df1['rating'])]['movieId'].iloc[0]
    
        movie_titles = dict(zip(movies['movieId'], movies['title']))
    
        similar_ids = find_similar_movies(movie_id, X, k)
        movie_title = movie_titles.get(movie_id, "Movie not found")
    
        if movie_title == "Movie not found":
            return f"Movie with ID {movie_id} not found."
    
        text = ""
        for i in similar_ids:
            text += str(movie_titles.get(i, "Movie not found")) + "\n"

        return text

    return recommend_movies_for_user(user_id, X, user_mapper, movie_mapper, movie_inv_mapper, k)


#user_id = 150 # Replace with the desired user ID
#print(recommendation_system(user_id, ".\\ratings.csv",".\\movies.csv", k=10))