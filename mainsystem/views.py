import pickle
import numpy as np
from django import template
from django.shortcuts import render
import pandas as pd

model = pickle.load(open('artifacts/model.pkl', 'rb'))
book_names = pickle.load(open('artifacts/books_name.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['img_url']
        poster_url.append(url)

    return poster_url


def recommend_book(book_name, num_recommendations=10):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=num_recommendations)

    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            books_list.append(j)
    return books_list, poster_url

def index(request):
    
    if request.method == 'POST':
        selected_books = request.POST.get('book_name')
        recommended_books, poster_url = recommend_book(selected_books, num_recommendations=40)
        context = {
            
            'book_data': dict(zip(recommended_books, poster_url)),
            'book_names': book_names
                   
                   }
    
        return render(request, 'pages/mainpage.html', context)
    else:
        context = {
            'book_names': book_names,
        }
        return render(request, 'pages/mainpage.html', context)



def mainPage(request):
    return render(request,"pages/mainpage.html",{})