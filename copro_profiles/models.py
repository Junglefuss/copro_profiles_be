from django.db import models
from django.contrib.auth.models import User


class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="user", to_field="id"
    )
    # worker_id = models.ForeignKey(
    #     User, on_delete=models.CASCADE, blank=True, default=""
    # )
    phone = models.CharField(max_length=20)
    headshot = models.ImageField(
        upload_to="staticfiles/admin/img/worker_images/", blank=True
    )
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="USA")
    AVAILABILITY = [
        ("FTR", "Full-time, Regular hours"),
        ("FTI", "Full-time, Irregular hours (nights, weekends)"),
        ("PTR", "Part-time, Regular hours (most nights, weekends)"),
        ("PTI", "Part-time, Irregular hours (here and there)"),
        ("NA", "Not Currently Available, Just staying informed"),
    ]
    availability = models.CharField(
        max_length=3, choices=AVAILABILITY, default="FTR")
    min_hourly_rate = models.IntegerField()
    skills = models.TextField(max_length=500)
    headline = models.CharField(max_length=255)
    referred_by = models.CharField(max_length=255)
    references = models.TextField(max_length=1000)
    referred_to = models.TextField(max_length=500, blank=True)
    connections = models.ManyToManyField("self", blank=True)
    # teams = models.ManyToManyField("Team", related_name="workers")
    comments = models.TextField(max_length=500, blank=True)
    sign_up_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} of {self.city}, {self.state} ({self.country}): {self.headline}"


class WorkerLink(models.Model):
    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name="worker_links"
    )
    label = models.CharField(max_length=100)
    url = models.URLField(max_length=1000)
    screenshot = models.ImageField(
        upload_to="staticfiles/admin/img/link_screenshots", blank=True
    )
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.worker}'s link labeled {self.label}: {self.url}"


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    logo = models.ImageField(
        upload_to="staticfiles/admin/img/team_logos/", blank=True)
    team_admin = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name="teams"
    )
    description = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.team_name}: {self.description} (Admin:{self.team_admin})"


class TeamLink(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="team_links")
    label = models.CharField(max_length=100)
    url = models.TextField(max_length=1000)
    screenshot = models.ImageField(
        upload_to="staticfiles/admin/img/link_screenshots", blank=True
    )
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.team}'s link labeled {self.label}: {self.url}"
