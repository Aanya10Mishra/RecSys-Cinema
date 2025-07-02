import pickle

import pandas as pd
import streamlit as st


# from PIL import Image
# import Pillow
# import requests

#def fetch_poster(movie_id):
   #response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=47c589f2fc1f4ef67b904e15276c2640'.format(movie_id))
   #data = response.json()
   #return "https://image.tmdb.org/t/p/original" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies =[]
    #recommended_movies_posters =[]
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        #recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommendation System')

# Load cute illustration image
# illustration_image = Image.open("C:/Users/Manvi/Downloads/movie1.jpg")   Replace with your image path

# st.sidebar.image(illustration_image, width=200)    Display illustration in sidebar

selected_movie_name = st.selectbox(
'Mention the Name of the Movie:',
movies['title'].values)

if st.button('Recommend'):
   recommendations =  recommend(selected_movie_name)
   for i in recommendations:
      st.write(i)


   #col1, col2, col3 = st.columns(3)

   #with col1:
      # st.header("A cat")
      # st.image("https://static.streamlit.io/examples/cat.jpg")

  # with col2:
      # st.header("A dog")
      # st.image("https://static.streamlit.io/examples/dog.jpg")

  # with col3:
      # st.header("An owl")
      # st.image("https://static.streamlit.io/examples/owl.jpg")