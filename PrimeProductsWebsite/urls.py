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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.signup, name='signup'),
    #url(r'^login/$', views.login, {'template_name': 'login.html'}, name='login'),
    #url(r'^logout/$', views.logout, {'next_page': 'login'}, name='logout'),

    url(r'^$', views.index, name='index'),
    url(r'^search_query$', views.search_query, name='search_query'),
    url(r'^result_page$', views.result_page, name='result_page'),

    url(r'^product_details$', views.product_details, name='product_details'),
    url(r'^show_product_details$', views.show_product_details, name='show_product_details'),

    url(r'^categories_listing$', views.categories_listing, name='categories_listing'),

    #url(r'^$', views.post_list, name='post_list'),
]
