from django.db import models


# Create your models here.
class List(models.Model):
    date = models.DateField(auto_now_add=False)

    def __str__(self):
        return str(self.date)


class Thing(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    lst = models.ForeignKey(List, on_delete=models.CASCADE)
    done = False

    def __str__(self):
        return self.title
