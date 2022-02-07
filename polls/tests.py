from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse
from polls.models import Question, Choice, Vote
from django.utils import timezone
from rest_framework.test import RequestsClient
from rest_framework.test import APIRequestFactory

class QuestionModelTests(TestCase):
    def test_create_object(self):
        q = Question(question="Helo...", pub_date=timezone.now())
        q.save()
        q.choices.create(choice_text='test')
    def test_get_list_of_objects(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/polls/')
        assert response.status_code == 200
    def test_change_object(self):
        q = Question(question="Helo...", pub_date=timezone.now())
        q.save()
        t = Question.objects.get(id=1)
        t.question = 'changed'
        t.save()
    def test_filter_object(self):
        q = Question(question="Helo...", pub_date=timezone.now())
        q.save()
        q.choices.create(choice_text='test')
        c =Choice.objects.filter(choice_text='test')
        q = Question.objects.filter(question='Helo...')
      q = Question(question="Helo...", pub_date=timezone.now())
        q.save()
        q.choices.create(choice_text='test')
        c =Choice.objects.filter(choice_text='test')
        q = Question.objects.filter(question='Helo...')
