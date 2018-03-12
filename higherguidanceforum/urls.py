from django.conf.urls import url
from higherguidanceforum import views

urlpatterns = [

    #HOMEPAGE
    url(r'^$', views.home, name='home'),

    #ABOUT
    url(r'^about/', views.about, name='about'),
    url(r'^about/contact-us/', views.contact_us, name='contact_us'),

    #SUBJECTS
    #The subject index page, hopefully ranked by popularity
    url(r'^subjectindex/', views.subject_index, name='subjectindex'),

    #The url for each individual subject
    url(r'^subjectindex/(?P<subject_name_slug>[\w\-]+)/$', views.show_subject, name='show_subject'),

    #The resource page for a subject
    url(r'^subjectindex/(?P<subject_name_slug>[\w-]+)/resources/', views.show_resources, name='show_resources'),
    url(r'^subjectindex/(?P<subject_name_slug>[\w\-]+)/resources/submit/$', views.submit_page, name='submit_page'),

    #The forum page for a subject
    url(r'^subjectindex/(?P<subject_name_slug>[\w\-]+)/forum/', views.show_forum, name='show_forum'),
    url(r'^subjectindex/(?P<subject_name_slug>[\w\-]+)/forum/submit/', views.submit_question, name='submit_question'),
    url(r'^subjectindex/(?P<subject_name_slug>[\w\-]+)/forum/(?P<question_name_slug>[\w\-]+)/', views.show_question, name='show_question'),
    url(r'^subjectindex/(?P<subject_name_slug>[\w\-]+)/forum/(?P<question_name_slug>[\w\-]+)/submitanswer/', views.submit_answer, name='submit_answer'),

    #REGISTRATION
    url(r'^register/$', views.register, name='register'),

    #LOGIN
    url(r'^login/$', views.user_login, name='login'),
    url(r'^login/myaccount/', views.my_account, name='my_account'),
    url(r'^login/myaccount/mysubmissions/', views.my_submissions, name='my_submissions'),
    url(r'^logout/$', views.user_logout, name='logout'),

    #USERS
    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^users/(?P<username_slug>[\w\-]+)/', views.user, name='user'),
    url(r'^users/(?P<username_slug>[\w\-]+)/submissions', views.submission_history, name='submission_history'),
]