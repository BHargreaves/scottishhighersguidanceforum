from django.contrib import admin
from higherguidanceforum.models import Subject, Link, UserProfile, Student, Teacher
# Register your models here.

class ResourceAdmin(admin.ModelAdmin):
    list_display = ()#'title','subject','url')

class SubjectAdmin(admin.ModelAdmin):
    prepopulate_fields = {'slug':('name','views','likes')}

# Register your models here.
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Link, ResourceAdmin)
admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Teacher)