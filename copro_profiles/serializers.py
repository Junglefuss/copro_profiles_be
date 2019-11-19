from rest_framework import serializers
from .models import Worker, WorkerLink, Team, TeamLink
from accounts.serializers import UserSerializerWithToken


class TeamLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamLink
        fields = ["team", "label", "url", "screenshot", "created_date", "updated_date"]


class TeamSerializer(serializers.ModelSerializer):
    team_links = TeamLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = [
            "team_name",
            "logo",
            "team_admin",
            "description",
            "created_date",
            "updated_date",
            "team_links",
        ]


class WorkerLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerLink
        fields = [
            "worker",
            "label",
            "url",
            "screenshot",
        ]


class WorkerSerializer(serializers.ModelSerializer):
    worker_links = WorkerLinkSerializer(many=True, read_only=True)
    user = UserSerializerWithToken(many=False, read_only=True)

    class Meta:
        model = Worker
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "headshot",
            "street",
            "city",
            "state",
            "country",
            "availability",
            "min_hourly_rate",
            "skills",
            "headline",
            "referred_by",
            "references",
            "referred_to",
            "connections",
            "comments",
            "sign_up_date",
            "updated_date",
            "worker_links",
            "user",
        ]

