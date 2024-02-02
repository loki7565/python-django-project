"""
URL configuration for humanhood project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from joincommunity import views as jc
from blogs import views as bl
from talk import views as tk
from about import views as ab
from purchase import views as ps
from search import views as sr
from signupform import views as sign
# from header import views as hd
# from footer import views as ft

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('joinpage/', jc.joincommunity, name='joincommunity'),
    path('blogpage/', bl.blogs, name='blogs'),
    path('talkpage/', tk.talk, name='talk'),
    path('aboutpage/', ab.about, name='about'),
    path('purchasepage/', ps.purchase, name='purchase'),
    path('searchpage/', sr.search, name='search'),
    path('signup/', sign.signupform, name='signupform'),
    path('entry', sign.signup_data_entry, name='signup_data_entry'),
    # path('headerpage/', hd.header, name='header'),
    # path('footerpage/', ft.footer, name='footer'),
]
