from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.FileField(upload_to='resumes/')
    extracted_text=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume-{self.user.username}"

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.position} - {self.company}"

class MatchResult(models.Model):
    resume=models.ForeignKey(Resume,on_delete=models.CASCADE)
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    match_score=models.FloatField()
    missing_skills=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
# Create your models here.
