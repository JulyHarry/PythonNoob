import datetime

from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.CharField(max_length=18, primary_key=True)
    username = models.CharField(max_length=50, null=False, blank=False)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    introduction = models.TextField()

    def __str__(self):
        return self.username


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='anonymous')
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
