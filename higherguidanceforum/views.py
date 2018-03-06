from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This will be the home page")

def about(request):
    return HttpResponse("This will be the about page")

def contact_us(request):
    return HttpResponse("This will be the contact us page")

def subject_index(request):
    return HttpResponse("This will be the subject index page")

def show_subject(request):
    return HttpResponse("This will be a specific subject page")

def show_resources(request):
    return HttpResponse("This will be a subject resource page")

def submit_page(request):
    return HttpResponse("This will be where you can submit resources")

def show_forum(request):
    return HttpResponse("This will be the subject forum page")

def submit_question(request):
    return HttpResponse("This will be where you can submit a question")

def show_question(request):
    return HttpResponse("This will be where you can look at a question")

def submit_answer(request):
    return HttpResponse("This will be where you can answer a question")

def register(request):
    registered = False
    if request.method == 'POST'
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True

        else:
            printer(user_form.errors, profile_Form.errors)

    else
    return HttpResponse("This will be where you can register")

def user_login(request):
    return HttpResponse("This is the login form")

def my_account(request):
    return HttpResponse("This is the user account")

def my_submissions(request):
    return HttpResponse("This is the user's submission history")

def user_logout(request):
    return HttpResponse("The is the logout screen")

def user_list(request):
    return HttpResponse("This is the list of users")

def user(request):
    return HttpResponse("This is the person's user page")

def submission_history(request):
    return HttpResponse("This is the person's submission history")