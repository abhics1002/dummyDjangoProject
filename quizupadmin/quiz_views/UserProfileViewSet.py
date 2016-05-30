__author__ = 'abhishekbharadwaj'

from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import viewsets, status
from rest_framework.decorators import list_route, detail_route, permission_classes, authentication_classes
from quizupadmin.quiz_response.responses import QuestionResponse, ChallengeQues
from quizupadmin.quiz_utils.json_utils import to_json
from django.http import HttpResponse

class UserViewSet(viewsets.ViewSet):

    def update_profile(self, request):
        pass

