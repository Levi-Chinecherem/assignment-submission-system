from django.contrib import admin
from .models import Profile, Level, Department, Semester, Course, Assignment, Discussion, Comment, Reply, SubmittedAssignment


# Customizing the Profile model in the admin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'is_lecturer']
    list_filter = ['is_lecturer']
    search_fields = ['user__username', 'full_name']
    ordering = ['user__username']

# Register ProfileAdmin as the admin for the Profile model
admin.site.register(Profile, ProfileAdmin)

# Customizing the other models in the admin
class LevelAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Level, LevelAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Department, DepartmentAdmin)

class SemesterAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Semester, SemesterAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'title', 'level', 'department', 'semester']

admin.site.register(Course, CourseAdmin)

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'semester', 'level', 'lecturer', 'department']

admin.site.register(Assignment, AssignmentAdmin)

class DiscussionAdmin(admin.ModelAdmin):
    list_display = ['title', 'lecturer']

admin.site.register(Discussion, DiscussionAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['discussion', 'user']

admin.site.register(Comment, CommentAdmin)

class ReplyAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user']

admin.site.register(Reply, ReplyAdmin)

class SubmittedAssignmentAdmin(admin.ModelAdmin):
    list_display = ['assignment', 'submitted_by', 'is_marked', 'total_score']

admin.site.register(SubmittedAssignment, SubmittedAssignmentAdmin)
