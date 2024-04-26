import pickle
import numpy as np
from django import template
from django.shortcuts import render
import pandas as pd

# from django.shortcuts import render
# import numpy as np
# import pickle
# import pandas as pd

def fetch_poster(suggestion, book_pivot, final_rating):
    poster_url = []
    
    for book_id in suggestion:
        name = book_pivot.index[book_id]
        idx = np.where(final_rating['title'] == name)[0][0]
        url = final_rating.iloc[idx]['img_url']
        poster_url.append(url)

    return poster_url

def recommend_book(book_name, book_pivot, model, final_rating, num_recommendations=10):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=num_recommendations)
    
    poster_url = fetch_poster(suggestion[0], book_pivot, final_rating)

    for i in range(len(suggestion[0])):
        books = book_pivot.index[suggestion[0][i]]
        for j in books:
            books_list.append(j)
    
    return books_list, poster_url

def index(request):
    model = pickle.load(open('artifacts/model.pkl', 'rb'))
    book_names = pickle.load(open('artifacts/books_name.pkl', 'rb'))
    final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
    book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))
    
    if request.method == 'POST':
        selected_books = request.POST.get('book_name')
        recommended_books, poster_url = recommend_book(selected_books, book_pivot, model, final_rating, num_recommendations=10)
        context = {
            'book_names': book_names,
            'selected_books': selected_books,
            'recommended_books': recommended_books,
            'poster_url': poster_url,
        }
        return render(request, 'pages/mainpage.html', context)
    else:
        context = {
            'book_names': book_names,
        }
        return render(request, 'pages/mainpage.html', context)









# def fetch_poster(suggestion):
#     poster_url = []
    
#     # Load data
#     final_rating = pd.read_pickle('artifacts/final_rating.pkl')
    
#     for book_id in suggestion:
#         name = final_rating.index[book_id]
#         url = final_rating.loc[name, 'img_url']
#         poster_url.append(url)

#     return poster_url

# def recommend_book(book_name, num_recommendations=10):
#     books_list = []
    
#     # Load data
#     book_pivot = pd.read_pickle('artifacts/book_pivot.pkl')
#     model = pickle.load(open('artifacts/model.pkl', 'rb'))

#     try:
#         book_id = np.where(book_pivot.index == book_name)[0][0]
#         distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=num_recommendations)
        
#         poster_url = fetch_poster(suggestion)
#         poster_dict = {book: url for book, url in zip(book_pivot.index[suggestion[0]], poster_url)}

#         for i in range(len(suggestion)):
#             books = book_pivot.index[suggestion[i]]
#             for j in books:
#                 books_list.append(j)
        
#         return books_list, poster_dict
#     except IndexError:
#         return [], {}

# def index(request):
#     book_names = pd.read_pickle('artifacts/books_name.pkl')
    
#     if request.method == 'POST':
#         selected_books = request.POST.get('book_name')
#         recommended_books, poster_url = recommend_book(selected_books, num_recommendations=10)
        
#         context = {
#             'book_names': book_names,
#             'selected_books': selected_books,
#             'recommended_books': recommended_books,
#             'poster_url': poster_url,
#         }
        
#         return render(request, 'pages/mainpage.html', context)
#     else:
#         context = {
#             'book_names': book_names,
#         }
        
#         return render(request, 'pages/mainpage.html', context)






def mainPage(request):
    return render(request,"pages/mainpage.html",{})