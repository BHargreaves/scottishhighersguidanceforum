from django import forms
from django.contrib.auth.models import User
from higherguidanceforum.models import Link, Subject, UserProfile, Student, Teacher

class SubjectForm(forms.ModelForm):

    name = forms.CharField(max_length=128,help_text="Please enter the subject name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Subject
        fields = ('name',)

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
        fields = ('title',)

        excluse = ('category')



class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class StudentSignUpForm(UserProfileForm):
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserProfileForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        #user.save()
        student = Student.objects.create(user=user)
        student.subjects.add(*self.cleaned_data.get('subjects'))
        student.save()
        return user

class TeacherSignUpForm(UserProfileForm):

    class Meta(UserProfileForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user