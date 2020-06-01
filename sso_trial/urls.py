"""sso_trial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings

from initiatives.factories import InitiativeViewFactory
from news.factories import NewsViewFactory, AllNewsViewFactory, AllNewsByTagViewFactory
from .views import ViewWrapper

urlpatterns = [
    path('admin/', admin.site.urls),
    path('initiatives/', ViewWrapper.as_view(view_factory = InitiativeViewFactory), name= 'initiatives'),
    path('initiatives/id/<int:init_id>/', ViewWrapper.as_view(view_factory = InitiativeViewFactory), name='initiative'),
    path('news/id/<int:id>/', ViewWrapper.as_view(view_factory = NewsViewFactory), name ='news'),  
    path('news/tags/<slug:tag>/', ViewWrapper.as_view(view_factory = AllNewsByTagViewFactory), name ='news'),   
    path('news/', ViewWrapper.as_view(view_factory = AllNewsViewFactory), name ='news'),
   
]
