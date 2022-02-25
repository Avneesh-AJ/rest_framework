from django.urls import  path
from api import views


urlpatterns=[
    path('user/',views.usersApi,name="user"),
    path('article/',views.articleApi,name="article"),
     path('createarticle/',views.createArticleApi,name="createarticle")
]