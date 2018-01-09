from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from	.models	import Category
from	.models	import ContactInfo
from	.models	import History
from	.models	import Client
from	.models	import Review
from	.models	import Supermarket
from	.models	import Manufacturer
from	.models	import Product
from	.models	import Favorite
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.core.mail import send_mail

import time, string, re, json

#search = [];

#@login_required
#def home(request):
#    return render(request, 'home.html')

## Fonction qui gére le login/signin
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup_login.html', {'form': form})

## Fonction qui gère le post d'un commentaire sur un produit
@csrf_exempt
def post_comment(request):
    if request.method == "POST":
        b = Review(username = request.POST.get("username", ""),stars = request.POST.get("etoiles", ""),review_text=request.POST.get("commentaire", ""),review_date=time.strftime("%c"),product_name=Product.objects.get(name__iexact=request.POST.get("product_name", "")).name)
        b.save()
        q = []
        q.append({'name':"Votre commentaire a été enregistrer."})
        return render(request, 'thank_you.html', {'product_details' : q})

## Fonction qui retourne la page d'accueil
def index(request):
    return render(request, 'index.html')

def accueil(request):
    return render(request, 'index.html')

## Fonction qui retourne la page de signup/login
def connexion(request):
    return render(request, 'signup_login.html')

## Fonction qui gére le login/signin
def signup_login(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup_login.html', {'form': form})

## Fonctions qui retournent les pages de contact
def contact_form(request):
    return render(request, 'contact_form.html')

def contact(request):
    return render(request, 'contact.html')

## Fonction qui retourne la page du profil
def profile(request):
    q = []
    profile_info = {'username': 'Mehdi Bettiche','image': 'M.png','date':'01-01-0001 - 00:00'}
    q.append(profile_info)
    return render(request, 'profile.html',{'user_information':q})

## Fonction qui retourne les categories
def categories_listing(request):
    category=Category.objects.all()
    q = []
    for c in category:
        categorie = {'categorie':c.name ,'number_of_products':ProductNumber(c.pk)}
        q.append(categorie)   
    return render(request, 'categories_listing.html', {'categories':q})

## Fonction qui gére la liste des favoris <en attente>
def favourite_list(request):
    q = []
    for x in range(1,20):
        favoris = {'name': 'lait produit bebe','date': '01-01-0001 - 00:00'}
        q.append(favoris)
    return render(request, 'favourite_list.html', {'favoris':q})

## Fonction qui retourne les commentaires d'un utilisateur <en attente>
def my_comments(request):
    q = []
    for x in range(1,20):
        comments = {'produit': 'lait produit bebe','date': '01-01-0001 - 00:00'}
        q.append(comments)
    return render(request, 'my_comments.html', {'comments':q})

## Fonction qui gère la recherche d'un produit
@csrf_exempt 
def search_query(request):
    if request.method == "POST":
        query = request.POST.get("produit", "")
        all_entries = Product.objects.filter(name__contains=query )
        q = []
        for p in range(0,len(all_entries)):
            print(all_entries[p].name)
            if request.POST.get("min", "")!="" and request.POST.get("max", "")!="":
                if float(request.POST.get("min", "")) <= float(request.POST.get("max", "")):
                    if float(request.POST.get("min", "")) <=all_entries[p].price<= float(request.POST.get("max", "")):
                        search_query_result ={'name':all_entries[p].name,'image':all_entries[p].image,'price':all_entries[p].price,'supermarket':all_entries[p].supermarket.name,'description':all_entries[p].description,'id':all_entries[p].id}
                        q.append(search_query_result)
            else:
                search_query_result ={'name':all_entries[p].name,'image':all_entries[p].image,'price':all_entries[p].price,'supermarket':all_entries[p].supermarket.name,'description':all_entries[p].description,'id':all_entries[p].id}
                q.append(search_query_result)
        return render(request, 'search_query.html', {'search_query_result' : q,'query':query }) #, 'search' : search

## Fonction qui retourne les details d'un produit particuliers
@csrf_exempt
def show_product_details(request):
    return render(request, 'product_details.html')

## Fonction qui retourne les details d'un produit particuliers
def product_details(request,id):
    obj = Product.objects.get(id=id)
    name_p = obj.name
    q = []
    search_query_result = {'name':obj.name,'image':obj.image,'price':obj.price,'supermarket':obj.supermarket.name,'description':obj.description}
    q.append(search_query_result)
    all_entries = Review.objects.filter(product_name__iexact=obj.name)
    c = []
    for p in range(0,len(all_entries)):
        comments ={'date':all_entries[p].review_date,'name': all_entries[p].username,'image': all_entries[p].username[:1]+".png",'review':all_entries[p].review_text,'stars':all_entries[p].stars}
        c.append(comments)
    return render(request, 'product_details.html', {'product_details' : q, 'reviews':c})

## Fonctions utilisées pour la recherche d'un produit
def ProductNumber(categoryId):
    products=Product.objects.filter(category=categoryId)
    n=len(products)
    return n
def findCheaper(query,minPrix):
    m=int(minPrix)
    pName=''
    products=Product.objects.filter(name__iexact=query)
    for p in products:
        if p.price <=m:
            m=int(p.price) 
            pName=p.name
            print(m)
    print("name is "+pName)
    cheapestProduct=Product.objects.get(name=pName)
    return cheapestProduct
        
## Fonction qui gère l'envoi de mails
@csrf_exempt
def send_mail(request):
    if request.method == "POST":
        print("username est :",request.POST.get("name", ""))
        print("email est :",request.POST.get("email", ""))
        print("comment est :",request.POST.get("message", ""))
        send_mail(
        'PrimeProducts [email de:]'+request.POST.get("name", ""),
        'Message'+request.POST.get("message", ""),
        request.POST.get("email", ""),
        ['mehdibettiche@gmail.com'],
        )
        q.append({'name':"Votre email a bien été envoyé."})
        return render(request, 'thank_you.html', {'product_details' : q})
    






