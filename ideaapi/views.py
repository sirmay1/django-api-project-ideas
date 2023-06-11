from django.shortcuts import render
from rest_framework import viewsets
from .models import Idea
from .serializers import IdeaSerializer


class IdeaView(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

# Create your views here.
