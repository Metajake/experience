from django.db import models

class Experience(models.Model):
    experienceDate = models.DateTimeField("Date Experienced", auto_now=True)
    type = models.CharField(max_length=50)
    description = models.TextField()
    user = models.CharField(max_length=100)
    def __str__(self):
        return self.description
