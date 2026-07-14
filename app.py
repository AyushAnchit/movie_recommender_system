import streamlit as st
import pickle
import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from a local .env file (if it exists)
load_dotenv()

# Secure API Key loading: checks Streamlit Secrets, then environment variables, then falls back to a default key
try:
    TMDB_API_KEY = st.secrets.get("TMDB_API_KEY", os.environ.get("TMDB_API_KEY", "8265bd1679663a7ea12ac168da84d2e8"))
except Exception:
    TMDB_API_KEY = os.environ.get("TMDB_API_KEY", "8265bd1679663a7ea12ac168da84d2e8")

movies_dic=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_dic)
similarity=pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    try:
        response = requests.get(url, timeout=2)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path.lstrip('/')
    except Exception as e:
        pass
    # Return a high-quality placeholder poster image if fetching fails
    return "https://images.unsplash.com/photo-1594909122845-11baa439b7bf?q=80&w=500&auto=format&fit=crop"

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters

st.title('Movie Recommender System')
option = st.selectbox('select your movie',movies['title'].values)

if st.button("Recommend"):
    names,posters= recommend(option)
    
    col1,col2,col3,col4,col5 =st.columns(5)
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



