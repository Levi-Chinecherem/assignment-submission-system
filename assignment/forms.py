from django import forms
from .models import Comment, Reply, Profile, Assignment, SubmittedAssignment, Discussion, Course, Level, Semester, Department
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AssignmentFilterForm(forms.Form):
    level = forms.ModelChoiceField(queryset=Level.objects.all())
    semester = forms.ModelChoiceField(queryset=Semester.objects.all())
    department = forms.ModelChoiceField(queryset=Department.objects.all())
      
class SubmittedAssignmentForm(forms.ModelForm):
    class Meta:
        model = SubmittedAssignment
        fields = ['document']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Write your comment here...'}),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Write your reply here...'}),
        }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'address', 'short_description', 'full_name', 'is_lecturer']
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
            'short_description': forms.Textarea(attrs={'placeholder': 'Enter a short description about yourself'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'full_name', 'address', 'short_description']
        
class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'course', 'semester', 'level', 'department', 'document']
        
class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['title', 'short_description', 'image', 'long_description', 'outro']