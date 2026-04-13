import streamlit as st
import pickle
import pandas as pd

# Load data
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

st.set_page_config(page_title="Movie Recommender", layout="centered")

st.title("🎬 Movie Recommendation System")

movie_list = movies["title"].values
selected_movie = st.selectbox("Select a movie", movie_list)


def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    
    distances = similarity.iloc[index]
    
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended = []
    
    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)
        
    return recommended


if st.button("Recommend 🎬"):
    results = recommend(selected_movie)
    
    st.subheader("Top Recommendations:")
    
    for movie in results:
        st.write(f"👉 {movie}")