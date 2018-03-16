from django.shortcuts import render
from django.http import HttpResponse

from higherguidanceforum.models import Subject, Link, UserProfile, SubjectForum, Question, Student, Teacher
from higherguidanceforum.forms import SubjectForm, LinkForm, UserProfileForm, StudentSignUpForm, TeacherSignUpForm

# Create your views here.

def home(request):
    context_dict = {}
    return render(request, 'higherguidanceforum/home.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': "Here is the about page"}
    return render(request, 'higherguidanceforum/about.html', context=context_dict)

def contact_us(request):
    return render(request, 'contactus.html')

def subject_index(request):
    context_dict = {'Subjects'}
    return render(request, 'higherguidanceforum/subjectindex.html', context=context_dict)


def show_subject(request, subject_name_slug):

    subject_list = Subject.objects.order_by('alphabetical')

    context_dict = {'subjects': subject_list}

    return render(request, 'higherguidanceforum/subjectindex.html', context=context_dict)

def show_resources(request):
    return render(request, 'higherguidanceforum/resources.html')

def submit_page(request):
    return render(request, 'higherguidanceforum/submitlink.html')

def show_forum(request):
    return render(request, 'higherguidanceforum/forum.html')

def submit_question(request):
    return render(request, 'higherguidanceforum/submitquestion.html')

def show_question(request):
    return render(request, 'higherguidanceforum/question.html')

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
            user.save
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile_form.picture = request.FILES['picture']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserProfileForm()
        profile_form = StudentSignUpForm()

    return render(request,
        'higherguidanceforum/registerstudent.html',
        {'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered})

def registerteacher(request):

    registered = False
    if request.method == 'POST':
        user_form = UserProfileForm(data=request.POST)
        profile_form = TeacherSignUpForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save
            profile = profile_form.save(commit=False)
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
        {'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your Scottish Higher Guidance Forum is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password) )
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'higherguidanceforum/login.html', {})

def my_account(request):
    return myaccount.html

def my_submissions(request):
    return submissions.html

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_list(request):
    return users.html

def user(request):
    return user.html

def submission_history(request):
    return submissions.html
