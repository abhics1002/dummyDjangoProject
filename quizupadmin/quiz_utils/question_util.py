__author__ = 'abhishekbharadwaj'
from quizupadmin.models import Quiz
from quizupadmin.quiz_response.responses import QuizVariant
from quizupadmin.quiz_response.responses import HomePageResp, HomeSecItemResp, ImageItem, QuizResp, QuestionResponse
from quizupadmin.models import Quiz, Question

def get_quiz_by_id(quiz_id):
    quiz_obj = Quiz.objects.get(id=quiz_id)
    quiz_resp = QuizResp()
    for q in quiz_obj.question_ids.split(','):
        question = Question.objects.get(id=q)
        ques_resp = QuestionResponse( q=question.ques, q_id=q, a=question.option_a, b=question.option_b, c=question.option_c, d=question.option_d,
                          ans=question.ans, desc=question.description)
        quiz_resp.add_questions(ques_resp)
    return quiz_resp.__dict__

def get_quiz_by_branch(branch):
    return None


def get_quiz_by_subject(subject):
    return None


def get_quizs_by_category(category=None):
    return None


def get_top_quiz_variant():
    quizs = Quiz.objects.all()
    quiz_variant = []
    for q in quizs:
        img = ImageItem("", "test image")
        v = QuizVariant(id=q.id, name=q.name, quiz_name=q.name,
                        branch="", subject="", played_by=q.total_attempts, level="", image=img, no_of_ques=10,
                        slug=q.id, tags="")
        quiz_variant.append(v)
    return quiz_variant

def get_quiz_by_popularity(subject=None):
    return None