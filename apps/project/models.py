from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short_description = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    administrators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='projects'
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner}/{self.name}'

    def get_absolute_url(self):
        return reverse("project", kwargs={"pk": self.pk})

    def get_open_bugs(self):
        return self.bugs.filter(is_open = True)

    def get_closed_bugs(self):
        return self.bugs.filter(is_open = False)

    def get_bug_num(self):
        return self.bugs.count() + 1
    