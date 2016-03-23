from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect

# Create your views here.

def login(request):
    return render(request, 'index.html')

# @user_passes_test(email_check, login_url='/')
def index(request):
    context = RequestContext(request, {'user', request.user})
    return render_to_response('spacex/dashboard.html', context_instance=context)


def email_check(user):
    if user is not None and user.email.endswith('gmail.com'):
        return True
    else:
        return False