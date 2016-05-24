from django.contrib import admin
from myadmin.models import UserProfileModel, UserDetails, AppSectionConfig, AppSection, Branch, Subjects, Articles, Video, RelatedReads,Question, QuestionDetails, Quiz, QuizResponse, Challenge_quiz
# Register your models here.
admin.site.register(UserProfileModel)
admin.site.register(UserDetails)
# admin.site.register(AppSectionConfig)
# admin.site.register(AppSection)
# admin.site.register(Branch)
# admin.site.register(Subjects)
# admin.site.register(Articles)
# admin.site.register(RelatedReads)
admin.site.register(Question)
admin.site.register(QuestionDetails)
# admin.site.register(Quiz)
# admin.site.register(QuizResponse)
# admin.site.register(Challenge_quiz)
