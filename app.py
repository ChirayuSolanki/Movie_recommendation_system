import streamlit as st
import pickle
def recommend(movie):
    index = movies_list[movies_list['title'] == movie].index[0]
    distance = similarity[index]
    movies_list1 = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movie = []
    for i in movies_list1:
        recommend_movie.append(movies_list.iloc[i[0]].title)
    return recommend_movie

movies_list = pickle.load(open('movie_list.pkl','rb'))
movies = movies_list['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie recommender sysytem')

import streamlit as st

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies)

st.write('You selected:', selected_movie_name)

if st.button('Reccommend'):
    recommended = recommend(selected_movie_name)
    for i in recommended:
        st.write(i)
