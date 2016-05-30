from __future__ import unicode_literals

# Create your models here.
__author__ = 'abhishekbharadwaj'
from django.db import models
from django.contrib.auth.models import User


class UserProfileModel(models.Model):
    class Meta:
        db_table = "user_profile"

    email = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)

class UserDetails(models.Model):
    class Meta:
        db_table = "user_details"

    user = models.ForeignKey(User)
    email = models.CharField(max_length=255)
    dob = models.DateField()
    interests = models.BigIntegerField()


class AppSectionConfig(models.Model):
    class Meta:
        db_table = "app_section_config"

    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

class AppSection(models.Model):
    class Meta:
        db_table = "app_sections"

    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    app_section = models.ForeignKey(AppSectionConfig)

class Interests(models.Model):
    pass


class Branch(models.Model):
    class Meta:
        db_table = "branchs"
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)


class Subjects(models.Model):
    class Meta:
        db_table = "subjects"

    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch)

class Articles(models.Model):
    class Meta:
        db_table = "articles"
    name = models.CharField(max_length=255)
    url = models.TextField()
    category = models.ForeignKey(Subjects)

class Video(models.Model):
    class Meta:
        db_table = "videos"
    name = models.CharField(max_length=255)
    url = models.TextField()
    category = models.ForeignKey(Subjects)

class RelatedReads(models.Model):
    class Meta:
        db_table = "related_reads"

    name = models.CharField(max_length=255)
    article = models.ForeignKey(Articles, null=True)
    video = models.ForeignKey(Video, null=True)




class Question(models.Model):
    class Meta:
        db_table = "questions"

    ques = models.TextField()
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField()
    option_d = models.TextField()
    ans = models.TextField()
    correct_option = models.CharField(max_length=10, blank=True)
    description = models.TextField()
    related = models.ForeignKey(RelatedReads, null=True)
    ques_id = models.BigIntegerField(unique=True, null=False)
    time_created = models.DateTimeField(auto_now=True)
    time_updated = models.DateTimeField(auto_now=True)
    relevent_score = models.IntegerField()
    category_id = models.ForeignKey(Subjects)
    branch = models.ForeignKey(Branch)




class QuestionDetails(models.Model):
    class Meta:
        db_table = "question_details"

    total_attempt = models.IntegerField()
    success_attempt = models.IntegerField()
    failure_attempt = models.IntegerField()
    difficulty = models.CharField(max_length=255)
    avg_time = models.IntegerField()


class Quiz(models.Model):
    class Meta:
        db_table = "quizs"
    name = models.CharField(max_length=255)
    quiz_id = models.BigIntegerField()
    question_ids = models.TextField()
    total_attempts = models.IntegerField()
    relevency = models.IntegerField()
    tags = models.TextField()
    category_id = models.ForeignKey(Subjects)
    branch = models.ForeignKey(Branch)
    time_created = models.DateTimeField(auto_now=True)
    time_updated = models.DateTimeField(auto_now=True)
    difficulty = models.CharField(max_length=255, blank=True)


class QuizResponse():
    class Meta:
        db_table = "quiz_response"
    quiz = models.ForeignKey(Quiz)
    user = models.ForeignKey(User)
    ans = models.TextField(max_length=255)
    time_taken = models.IntegerField()
    correct_ques = models.IntegerField()
    incorrect_ques = models.IntegerField()
    score = models.IntegerField()
    time_created =models.DateTimeField(auto_now=True)



class Challenge_quiz(models.Model):
    class Meta:
        db_table = "challenge_quizs"

    quiz = models.ForeignKey(Quiz)
    user_id1 = models.IntegerField(db_index=True)
    user_id2 = models.IntegerField(db_index=True)
    device1 = models.TextField()
    device2 = models.TextField()
    time_created = models.DateTimeField(auto_now=True)
