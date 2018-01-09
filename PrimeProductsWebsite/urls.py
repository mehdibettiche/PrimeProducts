"""fouille_opinions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from . import views as userAuth_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    ## Les urls accessibles du site web PrimeProducts
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'signup_login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'signup'}, name='logout'),
    url(r'^signup/$', userAuth_views.signup, name='signup'),
    url(r'^accueil$', views.accueil, name='accueil'),
    url(r'^search_query$', views.search_query, name='search_query'),
    url(r'^product_details/(?P<id>\d+)/$', views.product_details, name='product_details'),
    url(r'^show_product_details$', views.show_product_details, name='show_product_details'),
    url(r'^categories_listing$', views.categories_listing, name='categories_listing'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^favourite_list$', views.favourite_list, name='favourite_list'),
    url(r'^contact_form$', views.contact_form, name='contact_form'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^my_comments$', views.my_comments, name='my_comments'),
    url(r'^connexion$', views.connexion, name='connexion'),
    url(r'^post_comment$', views.post_comment, name='post_comment'),
    url(r'^send_mail$', views.send_mail, name='send_mail'),
]
