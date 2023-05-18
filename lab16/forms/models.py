from django.db import models

class Teachers(models.Model):
    fullname = models.CharField(max_length=20)
    subjectId = models.IntegerField()

