from django.shortcuts import render
from .models import NewsInfo

#this block for api library..
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NewsInfoSerializer

# Create your views here.
def index(request):
    all_items = NewsInfo.objects.all()
    return render(request,'index.html',{'all_items':all_items})

class NewsInfoList(APIView):
    def get(self,request):
        news_data = NewsInfo.objects.all()
        serializer = NewsInfoSerializer(news_data,many=True)
        return Response(serializer.data)

    def post(self):
        pass
