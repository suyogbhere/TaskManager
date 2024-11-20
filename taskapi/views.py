from django.shortcuts import render
from rest_framework import viewsets
from taskapp.models import Task
from taskapi.serializers import TaskSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer