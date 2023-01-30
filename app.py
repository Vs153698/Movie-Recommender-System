import streamlit as st
import pandas as pd
import pickle
import requests

def fetchposter(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=353e45f5dcc0fa83e3de162c63fa0878&language=en-US')
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
def recommended(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list =sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_Movies = []
    recommended_Movies_posters = []
    for i in movie_list:
        # for finding poster
        movie_id = movies.iloc[i[0]].movie_id
        # for recommended movie name
        recommended_Movies.append(movies.iloc[i[0]].title)
        recommended_Movies_posters.append(fetchposter(movie_id))

    return recommended_Movies,recommended_Movies_posters
# using cleaned dataFrame
movies = pickle.load(open('movies.pkl','rb'))
movies_list = movies['title'].values
st.title('Movie Recommender System')
st.form("my-form")
selectedMovieName = st.selectbox(label="Select Movie",options=movies_list)
# using similarity file
similarity = pickle.load(open('similarity.pkl','rb'))
if st.button('Recommend'):
    names,posters = recommended(selectedMovieName)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

