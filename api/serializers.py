from unittest.util import _MAX_LENGTH
from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=256)
    roll_no=serializers.IntegerField()
    marks=serializers.IntegerField()