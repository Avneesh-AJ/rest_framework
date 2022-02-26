from django.urls import  path
from api import views


urlpatterns=[

    path('articles/',views.ArticleListView.as_view(),name="article"),
    path('articles/<int:pk>',views.ArticleDetailView.as_view())

]

"""path('user/',views.usersApi,name="user"),
    path('article/',views.articleApi,name="article"),
    path('createarticle/',views.createArticleApi,name="createarticle")"""