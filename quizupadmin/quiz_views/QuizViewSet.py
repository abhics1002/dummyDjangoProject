__author__ = 'abhishekbharadwaj'

from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import viewsets, status
from rest_framework.decorators import list_route, detail_route, permission_classes, authentication_classes
from quizupadmin.quiz_response.responses import QuestionResponse, ChallengeQues
from quizupadmin.quiz_utils.json_utils import to_json
from django.http import HttpResponse
from quizupadmin.quiz_utils import question_util

class QuizViewSet(viewsets.ViewSet):

    @list_route(methods=['POST'])
    def get_quiz(self, request):
        quiz_id = request.data['quiz_id']
        resp = question_util.get_quiz_by_id(quiz_id)
        return HttpResponse(to_json(resp), content_type="application/json", status=status.HTTP_200_OK)


    def get_quiz_analysis(self, request):
        pass