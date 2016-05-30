__author__ = 'abhishekbharadwaj'


from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import viewsets, status
from rest_framework.decorators import list_route, detail_route, permission_classes, authentication_classes
from quizupadmin.quiz_response.responses import QuestionResponse
from quizupadmin.quiz_utils.json_utils import to_json
from django.http import HttpResponse
from quizupadmin.quiz_response.responses import HomePageResp, HomeSecItemResp, ImageItem
from quizupadmin.quiz_utils.question_util import get_quizs_by_category, get_top_quiz_variant, get_quiz_by_popularity

class HomeViewSet(viewsets.ViewSet):

    @list_route(methods=['GET'])
    def get_home_view(self, request):
        img = ImageItem("", "test image")
        home_sec_item = HomeSecItemResp(id=1, name="TopCarousel", disp_nm="TopCarousel", image_item=img, type=1)
        quiz_variant = get_top_quiz_variant()
        home_sec_item.add_quiz_category(quiz_variant)
        home_page = HomePageResp()
        home_page.add_home_section(home_sec_item)

        home_sec2 = HomeSecItemResp(id=2, name="popular quiz", disp_nm="popular quiz", image_item=img, type=2)
        quiz_variant2 = get_top_quiz_variant()
        home_sec2.add_quiz_category(quiz_variant2)
        home_page.add_home_section(home_sec2)

        home_sec3 = HomeSecItemResp(id=3, name="Quiz by category", disp_nm="Quiz by category", image_item=img, type=3)
        quiz_variant3 = get_top_quiz_variant()
        home_sec3.add_quiz_category(quiz_variant3)

        home_page.add_home_section(home_sec3)
        home_page.add_exception(False)

        return HttpResponse(to_json(home_page), content_type="application/json", status=status.HTTP_200_OK)


    def get_side_drawer(self, request):
        pass