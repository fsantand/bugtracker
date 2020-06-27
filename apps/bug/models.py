from django.db import models
from django.conf import settings
from apps.project.models import Project

# Create your models here.
class Bug(models.Model):
    class Classification(models.TextChoices):
        CRITICAL = 'CR', ('Critical',)
        MEDIUM = 'MD', ('Medium',)
        MINOR = 'MN', ('Minor',)
        IMPROVEMENT = 'IM', ('Improvement',)
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bugs')
    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    classification = models.CharField(
        max_length=2,
        choices=Classification.choices,
        default=Classification.MINOR,
    )
    last_edited = models.DateTimeField(auto_now=True)
    date_reported = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE, related_name='comments')    
    commenter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    comment = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)