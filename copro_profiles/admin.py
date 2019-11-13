from django.contrib import admin
from .models import Worker, WorkerLink, Team, TeamLink

admin.site.register([Worker, WorkerLink, Team, TeamLink])
