import pandas as pd
import streamlit as st
import pickle
import requests

def fetch_poster(book_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(book_id)
    data = requests.get(url)
    data = data.json()

    return data


def recommend(book):
     index = books[books['Title'] == book].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

     recommended_book_name = []
     recommended_book_posters = []

     for i in distances[1:5]:
          book_id = books.iloc[i[0]].book_id

          recommended_book_name.append(books.iloc[i[0]].Title)
          recommended_book_posters.append(books.iloc[i[0]].Image)

     return recommended_book_name ,recommended_book_posters



similarity = pickle.load(open('similarity_new.pkl','rb'))
books = pickle.load(open('book_dic_new_im.pkl','rb'))
books = pd.DataFrame(books)




st.title("Top 4 recommended books")
book_list = books['Title'].values
selected_book = st.selectbox(
    "Type or select a Title from the dropdown",
    book_list
)
if st.button('Recommend'):
     recommended_book_name, recommended_book_posters = recommend(selected_book)
     col1, col2, col3, col4 = st.columns(4)
     with col1:
          st.text(recommended_book_name[0])
          st.image(recommended_book_posters[0])
     with col2:
          st.text(recommended_book_name[1])
          st.image(recommended_book_posters[1])

     with col3:
          st.text(recommended_book_name[2])
          st.image(recommended_book_posters[2])
     with col4:
          st.text(recommended_book_name[3])
          st.image(recommended_book_posters[3])
