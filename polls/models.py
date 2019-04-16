from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices',on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choice_id = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    vote_date = models.DateTimeField(auto_now=True)
