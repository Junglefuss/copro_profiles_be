from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WorkerSerializer, WorkerLinkSerializer, TeamSerializer, TeamLinkSerializer
from .models import Worker, WorkerLink, Team, TeamLink
# from drf_multiple_model.views import ObjectMultipleModelAPIView

class WorkerView(viewsets.ModelViewSet):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()

class WorkerLinkView(viewsets.ModelViewSet):
    serializer_class = WorkerLinkSerializer
    queryset = WorkerLink.objects.all()

# class WorkerView(ObjectMultipleModelAPIView):
#     querylist = [
#         {'queryset': Worker.objects.all(), 'serializer_class': WorkerSerializer},
#         {'queryset': WorkerLink.objects.all(), 'serializer_class': WorkerLinkSerializer},
#     ]

#     def get(self, request, format=None):
#         return Response("test")


class TeamView(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

class TeamLinkView(viewsets.ModelViewSet):
    serializer_class = TeamLinkSerializer
    queryset = TeamLink.objects.all()