from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #    '기본url을 제거한 나머지','처리하게할 함수 이름'
]

