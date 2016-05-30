__author__ = 'abhishekbharadwaj'


class QuestionResponse(object):
    ques = None
    ques_id = None
    option_a = None
    option_b = None
    option_c = None
    option_d = None
    ans = None
    desc = None

    def __init__(self, q, q_id, a, b, c, d, ans, desc):
        self.ques = q
        self.ques_id = q_id
        self.option_a = a
        self.option_b = b
        self.option_c = c
        self.option_d = d
        self.ans = ans
        self.desc = desc


class QuizResp(object):
    def __init__(self):
        self.quiz = []

    def add_questions(self, ques):
        self.quiz.append(ques)


class ChallengeQues(object):
    def __init__(self):
        self.questions = []

    def add_ques(self, ques):
        self.questions.append(ques)


class AppSectionItem(object):
    pass

class ImageItem(object):
    def __init__(self, image, alt):
        self.image_url = image
        self.width = 700
        self.height = 400
        self.alt = alt

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


class HomeSecItemResp(object):
    id = None
    name = None
    dis_nm = None
    image_item = None
    type = None
    quiz_variant = None

    def __init__(self, id, name, disp_nm, image_item, type):
        self.id = id
        self.name = name
        self.dis_nm = disp_nm
        self.image_item = image_item
        self.type = type
        self.category = None

    def add_image_item(self, image):
        self.image_item = image

    def add_quiz_category(self, category):
        self.quiz_variant = category

class QuizVariant(object):
    id = None
    name = None
    quiz_name = None
    quiz_branch = None
    quiz_subject = None
    played_by = None
    level = None
    image = None
    no_of_ques = None
    slug = None
    tags = None

    def __init__(self, id, name, quiz_name, branch, subject, played_by, level, image, no_of_ques, slug, tags):
        self.id = id
        self.name = name
        self.quiz_name = quiz_name
        self.quiz_branch = branch
        self.quiz_subject = subject
        self.played_by = played_by
        self.level = level
        self.image = image
        self.no_of_ques = no_of_ques
        self.slug = slug
        self.tags = tags

class HomePageResp(object):
    msg = None
    exception = None
    app_home_sec = None
    app_page_name = None
    desclaimer = None

    def __init__(self):
        self.msg = None
        self.exception = None
        self.app_home_sec = []
        self.app_page_name = None
        self.desclaimer = None

    def add_home_section(self, home_sec):
        self.app_home_sec.append(home_sec)

    def add_exception(self, exp):
        self.exception = exp

class VersionCheckResp(object):
    version_code = None
    content = None
    force_update = None
    statusCode = None

    def __init__(self, version_code, content, force_update, status_code):
        self.version_code = version_code
        self.content = content
        self.force_update = force_update
        self.statusCode = status_code