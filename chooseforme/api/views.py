from django.shortcuts import render
from rest_framework import generics, status
from .serializers import AnswersSerializer, ChooseSerializer
from .models import Answers
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class AnswersView(generics.ListAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer

class ChooseView(APIView):
    serializer_class = ChooseSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            mainGenre = serializer.data.get('mainGenre')
            secGenre = serializer.data.get('secGenre')
            yearOfRelease = serializer.data.get('yearOfRelease')
            host = self.request.session.session_key
            queryset = Answers.objects.filter(host=host)
            if queryset.exists():
                answers = queryset[0]
                answers.mainGenre = mainGenre
                answers.secGenre = secGenre
                answers.yearOfRelease = yearOfRelease
                answers.save(update_fields=['mainGenre', 'secGenre', 'yearOfRelease'])
            else:
                answers = Answers(host=host, mainGenre=mainGenre, secGenre=secGenre, yearOfRelease=yearOfRelease)
                answers.save()
            
            return Response(AnswersSerializer(answers).data, status=status.HTTP_201_CREATED)