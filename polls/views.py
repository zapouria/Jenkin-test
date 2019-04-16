from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from datetime import datetime

from django.contrib.auth import authenticate

from .models import Question, Choice, Vote
from .serializers import QuestionSerializer, ChoiceSerializer, VoteSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def destroy(self, request, *args, **kwargs):
        question = Question.objects.get(pk=self.kwargs["pk"])
        return super().destroy(request, *args, **kwargs)

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(question_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer

    def post(self, request, *args, **kwargs):
        Question = Question.objects.get(pk=self.kwargs["pk"])
        return super().post(request, *args, **kwargs)


class CreateVote(APIView):
    def post(self, request, pk, choice_pk):
        data = {'choice_id': choice_pk}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, pk, choice_pk):
        data = {'choice_id': choice_pk}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
