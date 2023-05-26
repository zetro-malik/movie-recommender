import streamlit as st 
import pickle
import requests

def fetct_poster(movie_id) :
    response=  requests.get("https://api.themoviedb.org/3/movie/{}?api_key=652bd4c5edb084547f1b296663171b5f&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data["poster_path"]
def recommend(movie):
    movie_index = movies_list[movies_list['title']==movie].index[0]
    distances = similarity[movie_index]
    movies = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies:
        movie_id=movies_list.iloc[i[0]].movie_id
        #fetch post from API
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movies_poster.append(fetct_poster(movie_id))
       
    return recommended_movies,recommended_movies_poster


movies_list = pickle.load(open("movies.pkl",'rb'))
movies_lst = movies_list['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))



st.title("Movie Recommender System")

selected_movieName = st.selectbox(
'How would you like to be Contacte?',
movies_lst
)


if st.button('Recommend'):
    name,posters = recommend(selected_movieName)

    col1, col2, col3,col4, col5 = st.columns(5)
    with col1:
        st.write(name[0])
        st.image(posters[0])

    with col2:
        st.write(name[1])
        st.image(posters[1])

    with col3:
        st.write(name[2])
        st.image(posters[2])

    with col4:
        st.write(name[3])
        st.image(posters[3])
    with col5:
        st.write(name[4])
        st.image(posters[4])