from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(default = "", max_length = 200, unique = True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    name = models.CharField(default = "", max_length = 200, unique = True)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete = models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class User_Info(models.Model):
    name = models.CharField(default="",max_length=100)
    addres = models.CharField(default="",max_length=100)
    email = models.CharField(default="",max_length=100)

    def __str__(self):
        return self.name