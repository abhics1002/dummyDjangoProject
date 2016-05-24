from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib import admin
from rest_framework import routers
from myadmin import views
from myadmin.quiz_views.QuestionsViewSet import QuestionsViewSet
from myadmin.quiz_views.HomeViewSet import HomeViewSet
from myadmin.quiz_views.QuizViewSet import QuizViewSet
from myadmin.quiz_views import quizviews

router = routers.SimpleRouter()
router.register(r'questions', QuestionsViewSet, base_name='questions')
router.register(r'app', HomeViewSet, base_name='app')
router.register(r'quiz', QuizViewSet, base_name='quiz')

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myadmin.views.login', name='login'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'api/app/(?P<id>\d+)/version/$', quizviews.check_version, name='check_version')
)
