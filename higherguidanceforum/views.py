from django.shortcuts import render
from django.http import HttpResponse

from higherguidanceforum.models import Subject, Link, UserProfile
from higherguidanceforum.forms import SubjectForm, LinkForm, UserForm, UserProfileForm

# Create your views here.

def home(request):
    context_dict = {}
    return render(request, 'higherguidanceforum/home.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': "Here is the about page"}
    return render(request, 'higherguidanceforum/about.html', context=context_dict)

def contact_us(request):
    return contactus.html

def subject_index(request):
    context_dict = {'boldmessage': "Here is the subject index page"}
    return render(request, 'higherguidanceforum/subjectindex.html', context=context_dict)


def show_subject(request, subject_name_slug):
    context_dict = {}

    try:
        subject = Subject.objects.get(slug=subject_name_slug)
        links = Link.objects.filter(category=subject)
        context_dict['links'] = links
        context_dict['subject'] = subject

    except Subject.DoesNotExist:
        context_dict['subject'] = None
        context_dict['links'] = None
    return render(request, 'higherguidanceforum/subject.html', context_dict)
    return HttpResponse("This will be a specific subject page")

def show_resources(request):
    return resources.html

def submit_page(request):
    return submitlink.html

def show_forum(request):
    return forum.html

def submit_question(request):
    return submitquestion.html

def show_question(request):
    return question.html

def submit_answer(request):
    return submitanswer.html

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

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
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
        'higherguidanceforum/register.html',
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
