from django import forms
from .models import Question
from django.contrib.auth.models import User
from higherguidanceforum.models import Link, Subject, UserProfile, Student, Teacher

class QuestionPostForm(forms.ModelForm):

    title = forms.CharField(max_length=128,help_text="Please enter the title")
    text = forms.CharField(max_length=1024,help_text="Please enter your question")

    class Meta:
        model = Question
        fields = ('title', 'text',)


class LinkForm(forms.ModelForm):

    title = forms.CharField(max_length=128, help_text="Please enter the title of the page")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        #if url is not empty and doesn't start with 'http://',
        #then prepend with 'http://'
        if url and not url.startswith('http://'):
            url = 'http://'+url
            cleaned_data['url']=url

            return cleaned_data

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Link
        fields = ('title','url',)


class UserProfileForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class StudentSignUpForm(forms.ModelForm):

    subjects = forms.ModelMultipleChoiceField(
            queryset=Subject.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=True
        )

    class Meta:
        model = UserProfile
        fields = ()

    def save(self, subjects):

        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create
        student.usubjects.add(subjects)
        student.save()
        return user


class TeacherSignUpForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ()

    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create
        teacher.save()
        return user