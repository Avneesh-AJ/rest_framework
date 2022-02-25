from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from api import models


class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=256)
    roll_no=serializers.IntegerField()
    marks=serializers.IntegerField()

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tag
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    tag=TagSerializer(many=True,read_only=True)
    class Meta:
       model=models.Article
       fields= '__all__'


    """def create(self, validated_data):
        return super().create(validated_data)"""

    def create(self, *args,**kwargs):
        print("this is cool")
        return super().create(*args,**kwargs)


    """def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)"""