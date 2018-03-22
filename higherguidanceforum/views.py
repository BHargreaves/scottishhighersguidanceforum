from datetime import datetime
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from higherguidanceforum.models import Subject, Link, UserProfile, Question, Answer, Student, Teacher
from higherguidanceforum.forms import LinkForm, UserProfileForm, StudentSignUpForm, TeacherSignUpForm, QuestionPostForm

# Create your views here.

def home(request):
    context_dict = {}
    subject_list = Subject.objects.order_by('views')[:5]
    context_dict = {'subjects': subject_list,}

    #resource_list = Link.object.order_by('views')[:5]
    #context_dict = {'links': resource_list,}

    return render(request, 'higherguidanceforum/home.html', context=context_dict)

def about(request):

    context_dict = {'boldmessage': "Here is the about page"}
    return render(request, 'higherguidanceforum/about.html', context=context_dict)

def contact_us(request):
    return render(request, 'contactus.html')

def subject_index(request):

    request.session.set_test_cookie()
    subject_list = Subject.objects.order_by('name')
    context_dict = {'subjects': subject_list,}

    #context_dict['visits'] = request.session['visits']

    response = render(request, 'higherguidanceforum/subjectindex.html', context_dict)

    visitor_cookie_handler(request, response)

    return response


def show_subject(request, subject_name_slug):

    context_dict = {}

    subject = Subject.objects.get(slug=subject_name_slug)
    context_dict['subject'] = subject

    return render(request, 'higherguidanceforum/subject.html', context=context_dict)


def show_resources(request, subject_name_slug):

    context_dict ={}

    try:
        subject = Subject.objects.get(slug=subject_name_slug)
        links = Link.objects.filter(category=subject)
        context_dict['links'] = links
        context_dict['subject'] = subject

    except Subject.DoesNotExist:
        context_dict['subject'] = None
        context_dict['links'] = None

    return render(request, 'higherguidanceforum/resources.html', context=context_dict)


def submit_page(request, subject_name_slug):

    try:
        subject = Subject.objects.get(slug=subject_name_slug)
    except Subject.DoesNotExist:
        subject = None

    form = LinkForm()
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            if subject:
                link = form.save(commit=False)
                link.category = subject
                link.views = 0
                link.save()
                return show_resources(request, subject_name_slug)
            else:
                print(form.errors)

    context_dict = {'form': form, 'subject': subject}

    return render(request, 'higherguidanceforum/submitlink.html', context_dict)


def show_forum(request, subject_name_slug):

    context_dict ={}

    try:
        subject = Subject.objects.get(slug=subject_name_slug)
        questions = Question.objects.filter(category=subject)

        context_dict['question'] = questions
        context_dict['subject'] = subject

    except Subject.DoesNotExist:
        context_dict['subject'] = None
        context_dict['questions'] = None

    return render(request, 'higherguidanceforum/forum.html', context=context_dict)


def submit_question(request, subject_name_slug):

    try:
        subject = Subject.objects.get(slug=subject_name_slug)
    except Subject.DoesNotExist:
        subject = None


    form = QuestionPostForm()
    if request.method == "POST":
        form = QuestionPostForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.category = subject
            question.author = request.user
            question.published_date = timezone.now()
            question.save()
            return show_forum(request, subject_name_slug)
    else:
        form = QuestionPostForm()

    context_dict = {'form': form, 'subject': subject}

    return render(request, 'higherguidanceforum/submitquestion.html', context_dict)


def show_question(request, question_slug_name):

    context_dict ={}

    try:
        question = Question.objects.get(slug=question_slug_name)
        answers = Answer.objects.filter(category=question)
        context_dict['answers'] = answers
        context_dict['question'] = question

    except Subject.DoesNotExist:
        context_dict['question'] = None
        context_dict['answers'] = None

    return render(request, 'higherguidanceforum/question.html', context=context_dict)


def submit_answer(request):
    return render(request, 'higherguidanceforum/submitanswer.html')


def register(request):
    return render(request, 'higherguidanceforum/register.html')


def registerstudent(request):

    registered = False
    if request.method == 'POST':
        user_form = UserProfileForm(data=request.POST)
        profile_form = StudentSignUpForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserProfileForm()
        profile_form = StudentSignUpForm()

    return render(request,
        'higherguidanceforum/registerstudent.html',
        {'profile_form': profile_form,
        'user_form' : user_form,
        'registered': registered})


def registerteacher(request):

    registered = False
    if request.method == 'POST':
        user_form = UserProfileForm(data=request.POST)
        profile_form = TeacherSignUpForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save()
            profile.user = user

            if 'picture' in request.FILES:
                profile_form.picture = request.FILES['picture']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserProfileForm()
        profile_form = TeacherSignUpForm()

    return render(request,
        'higherguidanceforum/registerteacher.html',
        {'profile_form': profile_form,
        'user_form' : user_form,
        'registered': registered})



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/scottishhighersguidanceforum/')
            else:
                return HttpResponse("Your Scottish Higher Guidance Forum is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password) )
            return render(request, 'higherguidanceforum/invalidlogin.html',{})
    else:
        return render(request, 'higherguidanceforum/login.html', {})

def my_account(request):
     return render(request, 'higherguidanceforum/myaccount.html')

def my_submissions(request):
    return render(request, 'higherguidanceforum/submissions.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/scottishhighersguidanceforum/')


def user_list(request):
     return render(request, 'higherguidanceforum/users.html')

def user(request):
     return render(request, 'higherguidanceforum/user.html')

def submission_history(request):
     return render(request, 'higherguidanceforum/submissionhistory.html')

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request, response):
    visits = int(request.COOKIES.get('visits', '1'))
    last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        response.set_cookie['last_visit'] = str(datetime.now())
    else:
        visits = 1
        response.set_cookie('last_visit', last_visit_cookie)
    response.set_cookie('visits', visits)

def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")