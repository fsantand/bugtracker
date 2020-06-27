from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from apps.project.models import Project

# Create your models here.
class Bug(models.Model):
    class Classification(models.TextChoices):
        CRITICAL = 'CR', ('Critical')
        MEDIUM = 'MD', ('Medium')
        MINOR = 'MN', ('Minor')
        IMPROVEMENT = 'IM', ('Improvement')
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bugs')
    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    bug_number = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    description = models.TextField()
    classification = models.CharField(
        max_length=2,
        choices=Classification.choices,
        default=Classification.MINOR,
    )
    is_open = models.BooleanField(default=True)
    last_edited = models.DateTimeField(auto_now=True)
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'#{self.bug_number} - {self.title} ({self.Classification(self.classification).label})'

    def get_absolute_url(self):
        return reverse("bug-thread", kwargs={"project": self.project.pk ,"bug_number": self.bug_number})

    def get_classification(self):
        return self.Classification(self.classification).label
    

class Comment(models.Model):
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE, related_name='comments')    
    commenter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    comment = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_commented']