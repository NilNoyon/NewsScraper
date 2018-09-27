from django.urls import path
from newscrawlerapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.index,name='index'),
    path('newsapi',views.NewsInfoList.as_view()),
]
