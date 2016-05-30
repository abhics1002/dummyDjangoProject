from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib import admin
from rest_framework import routers
from quizupadmin import views
from quizupadmin.quiz_views.QuestionsViewSet import QuestionsViewSet
from quizupadmin.quiz_views.HomeViewSet import HomeViewSet
from quizupadmin.quiz_views.QuizViewSet import QuizViewSet
from quizupadmin.quiz_views import quizviews

router = routers.SimpleRouter()
router.register(r'questions', QuestionsViewSet, base_name='questions')
router.register(r'app', HomeViewSet, base_name='app')
router.register(r'quiz', QuizViewSet, base_name='quiz')

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'quizupadmin.views.login', name='login'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'api/app/(?P<id>\d+)/version/$', quizviews.check_version, name='check_version')
)
