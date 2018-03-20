from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout

from higherguidanceforum.models import Subject, Link, UserProfile
from higherguidanceforum.forms import SubjectForm, LinkForm, UserForm, UserProfileForm



# Create your views here.

def home(request):
    subject_list = Subject.objects.order_by('-likes')[:5]
    links_list = Links.objects.order_by('views')[:5]
    context_Dict = {'subject': subject_list, 'links': links_list}

    response = render(request, 'higherguidanceforum/home.html', context_dict)
    visitor_cookie_handler(request, response)

    return response

def about(request):
    context_dict = {'boldmessage': "Here is the about page"}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'scottishhigherguidanceforum/about.html', context=context_dict)

def contact_us(request):
    return HttpResponse("This will be the contact us page")

def subject_index(request):
    return HttpResponse("This will be the index page")

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
    return render(request, 'scottishhigherguidanceforum/subject.html', context_dict)
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
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save
            profile = profile = profile_form(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
        'scottishhigherguidanceforum/register.html',
        {'user_form': user_form,
        'profile_Form': profile_form,
        'registered': registered})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your Scottish Higher Guidance Forum is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password) )
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'scottishhigherguidanceforum/login.html', {})


def my_account(request):
    return HttpResponse("This is the user account")

def my_submissions(request):
    return HttpResponse("This is the user submissions")

def user_logout(request):
    logout(request)
    return HttpResponse(reverse('index'))


def user_list(request):
    return HttpResponse("This is the list of users")

def user(request):
    return HttpResponse("This is the person's user page")

def submission_history(request):
    return HttpResponse("This is the person's submission history")
