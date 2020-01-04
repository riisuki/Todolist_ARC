from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=50)
    desc = models.CharField(max_length=300, default="",blank=True,null=True)
    due = models.DateTimeField(blank=True,null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text