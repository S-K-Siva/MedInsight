from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MyModel
class ImageSerializer(ModelSerializer):
    class Meta:
        model = MyModel
        fields = "__all__"
from rest_framework import viewsets

from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source='creator.username')
    creator_id = serializers.ReadOnlyField(source='creator.id')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = MyModel
        fields = ['id', 'creator', 'creator_id', 'title', 'description', 'image_url']
