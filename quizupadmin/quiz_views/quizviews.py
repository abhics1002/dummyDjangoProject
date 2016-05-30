__author__ = 'abhishekbharadwaj'
from quizupadmin.quiz_response.responses import VersionCheckResp
from rest_framework import viewsets, status
from django.http import HttpResponse
from quizupadmin.quiz_utils.json_utils import to_json

def check_version(request, id):
    version_resp = VersionCheckResp(version_code=1, content="", force_update=False, status_code=200)
    return HttpResponse(to_json(version_resp), content_type="application/json", status=status.HTTP_200_OK)