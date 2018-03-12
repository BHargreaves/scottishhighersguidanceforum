from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context_dict = {}
    #return HttpResponse("This will be the home page")   #comment out/ delete to try fix the template errors
    return render(request, 'higherguidanceforum/home.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': "Here is the about page"}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'higherguidanceforum/about.html', context=context_dict)

def contact_us(request):
    return contactus.html

def subject_index(request):
    return subjectindex.html

def show_subject(request, subject_name_slug):
    context_dict = {}

    try:
        subject = Subject.objects.get(slug=category_name_slug)
        links = Links.objects.filter(category=category)
        context_dict['links'] = links
        context_dict['subject'] = subject

    except Subject.DoesNotExist:
        context_dict['subject'] = None
        context_dict['links'] = None
    return render(request, 'scottishhigherguidanceforum/subject.html', context_dict)
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
    return submitasnwer.html

def register(request):
    registered = False
    if request.method == 'POST':
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

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
        'scottishhigherguidanceforum/register.html',
        {'user_form': user_form,
        'profile_Form': profile_form,
        'registered': register})



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