from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField()
    course = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["name", "id"]
    def __str__(self):
        return self.name
