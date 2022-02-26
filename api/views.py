
import json
from urllib import request, response
from rest_framework.response import Response
#from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)

from api import serializers,models

class ArticleListView(ListCreateAPIView):
    #queryset=models.Article.objects.all()
    serializer_class= serializers.ArticleSerializer

    def get_queryset(self):
        query={}
        for key, value in self.request.GET.items():
            query["{}__icontains".format(key)]=value
        return models.Article.objects.filter(**query)

class ArticleDetailView(RetrieveUpdateAPIView):
    queryset=models.Article.objects.all()
    serializer_class= serializers.ArticleSerializer


    def post(self,request,pk):
        return Response(request.body)


# Create your views here.
"""class Student():
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks


@api_view()
def articleApi(request):

    articles=models.Article.objects.all()
    response=serializers.ArticleSerializer(articles,many=True)
    return Response(response.data)


@api_view(["POST"])
def createArticleApi(request):
    body=json.loads(request.body)
    response=serializers.ArticleSerializer(data=body)
    #print(body)
    if response.is_valid():
        inst=response.save()
        response=serializers.ArticleSerializer(inst)
        return Response(response.data)

    return Response(response.error)


@api_view()
def usersApi(request):

    student1=Student("avneesh",1,100)
    student2=Student("abhay",2,99)
    student3=Student("gaurav",3,98)
    response= serializers.StudentSerializer([
        student1,
        student2,
        student3
        ],many=True)
    return Response(response.data)"""