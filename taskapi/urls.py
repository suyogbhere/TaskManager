from rest_framework.routers import DefaultRouter
from django.urls import path,include
from taskapi import views


router = DefaultRouter()
router.register(r'api',views.TaskViewSet)

urlpatterns =[
    path('',include(router.urls)),
]


#http://127.0.0.1:8000/api/     GET DatA
#http://127.0.0.1:8000/api/     POST data
#http://127.0.0.1:8000/api/<int:id>    retrive single data
#http://127.0.0.1:8000/api/<int:id>    update single data
#http://127.0.0.1:8000/api/<int:id>    Delete single data