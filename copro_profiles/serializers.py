from rest_framework import serializers
from .models import Worker, WorkerLink, Team, TeamLink


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"


class WorkerLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerLink
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamLink
        fields = "__all__"
