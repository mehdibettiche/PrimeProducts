from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse, JsonResponse
from django.http import HttpResponseRedirect

#import json
import string
import re

import json

# Create your views here.
'''
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
'''

search = [];

def index(request):
    return render(request, 'index.html')

def accueil(request):
    global search
    search = []
    return render(request, 'index.html')

def connexion(request):
    return render(request, 'signup_login.html')

def signup(request):
    return render(request, 'signup_login.html')

def contact_form(request):
    return render(request, 'contact_form.html')

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    q = []
    profile_info = {'username': 'Mehdi Bettiche','image': 'M.png','date':'01-01-0001 - 00:00'}
    q.append(profile_info)
    return render(request, 'profile.html',{'user_information':q})

def categories_listing(request):
    q = []
    for x in range(1,20):
        categorie = {'categorie': 'Alimentaire','number_of_products': 100+x}
        q.append(categorie)
    return render(request, 'categories_listing.html', {'categories':q})

def favourite_list(request):
    q = []
    for x in range(1,20):
        favoris = {'name': 'lait produit bebe','date': '01-01-0001 - 00:00'}
        q.append(favoris)
    return render(request, 'favourite_list.html', {'favoris':q})

def my_comments(request):
    q = []
    for x in range(1,20):
        comments = {'produit': 'lait produit bebe','date': '01-01-0001 - 00:00'}
        q.append(comments)
    return render(request, 'my_comments.html', {'comments':q})

@csrf_exempt 
def search_query(request):
    #print("------------STARTING------------")
    if request.method == "POST":
        print("IT IS : ")
        print(request.POST)
        print("AND body: ")
        print(request.body)
        global search 
        search = json.loads(request.body)
    return JsonResponse({'status': True})

def result_page(request):
    global search
    print()
    print('The search is :',search)
    q = []
    for x in range(1,10):
        search_query_result = {'name': 'lait produit bebe','image': 'product-testing.png','price': 200+x,'supermarket': 'lidl','description':'produit lait pour bebe 2 3 ans'}
        q.append(search_query_result)
    return render(request, 'search_query.html', {'search_query_result' : q,'query':'lait bebe', 'search' : search})

@csrf_exempt
def show_product_details(request):
    return render(request, 'product_details.html')

#
#
def product_details(request):
    q = []
    search_query_result = {'name': 'I am a potatoe','image': 'product-testing.png','price': 200,'supermarket': 'lidl','description':'produit lait pour bebe 2 3 ans'}
    q.append(search_query_result)

    c = []
    for x in range(1,10):
        reviews = {'user_id':x,'date':'01-01-0001 - 00:00','username': 'testtest','image': 'product-testing.png','review':'this thing is not okay it is somehow really bad','stars':0+x}
        c.append(reviews)

    return render(request, 'product_details.html', {'product_details' : q, 'reviews':c})
