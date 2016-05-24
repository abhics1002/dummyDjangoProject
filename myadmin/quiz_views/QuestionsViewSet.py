__author__ = 'abhishekbharadwaj'

from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import viewsets, status
from rest_framework.decorators import list_route, detail_route, permission_classes, authentication_classes
from myadmin.quiz_response.responses import QuestionResponse, ChallengeQues
from myadmin.quiz_utils.json_utils import to_json
from django.http import HttpResponse

class QuestionsViewSet(viewsets.ViewSet):

    @list_route(methods=['POST'])
    def get_questions(self, request):
        resp = QuestionResponse("test","test", "test", "test", "test", "test", "test")
        return HttpResponse(to_json(resp), content_type="application/json", status=status.HTTP_200_OK)

    @list_route(methods=['POST'])
    def get_challenge(self, request):
        Q1 = QuestionResponse("test1","test2", "test2", "test4", "test5", "test6", "test7")
        Q2 = QuestionResponse("test1","test2", "test3", "test4", "test5", "test6", "test7")
        Q3 = QuestionResponse("test","test", "test", "test", "test", "test", "test")
        Q4 = QuestionResponse("test","test", "test", "test", "test", "test", "test")
        Q5 = QuestionResponse("test","test", "test", "test", "test", "test", "test")

        challenge = ChallengeQues()
        challenge.add_ques(Q1)
        challenge.add_ques(Q2)
        challenge.add_ques(Q3)
        challenge.add_ques(Q4)
        challenge.add_ques(Q5)

        return HttpResponse(to_json(challenge), content_type="application/json", status=status.HTTP_200_OK)
