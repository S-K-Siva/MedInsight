from django.shortcuts import render
from .forms import ImageForm
from .source import generate_insight

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .serializers import ImageSerializer
from rest_framework import permissions, viewsets
from rest_framework.parsers import MultiPartParser, FormParser

# @api_view(['GET'])
# def getInsight(request,imageURL):
#     generate_insight(imageURL)

# def createInsight(request):
#     form = ImageForm()
#     if request.method == "POST":
#         form = ImageForm(request.POST,request.FILES)
#         image_url = str(request.FILES.get('image_url'))
#         if form.is_valid():
#             form.save()
        
#     return render(request,'index.html',{'form':form})
from .models import MyModel
from .serializers import MyModelSerializer,ImageSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

class ImageUpload(APIView):
    def post(self,request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(generate_insight(request.data.image_url))
    
        
