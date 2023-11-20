from django.db import models
class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    file = models.CharField(max_length=255)