from django.db import models
from django.contrib.auth.models import User

SEMESTER_CHOICES = [
    ('First', 'First Semester'),
    ('Second', 'Second Semester'),
]

LEVEL_CHOICES = [
    ('100', '100 Level'),
    ('200', '200 Level'),
    ('300', '300 Level'),
    ('400', '400 Level'),
]

class Level(models.Model):
    name = models.CharField(max_length=100, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=100, choices=SEMESTER_CHOICES)

    def __str__(self):
        return self.name


class Course(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    document = models.FileField(upload_to='assignments/')

    def __str__(self):
        return self.title


class Discussion(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    image = models.ImageField(upload_to='discussion/images/', blank=True)
    long_description = models.TextField()
    outro = models.TextField(blank=True)
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discussions')

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile/images/', blank=True)
    address = models.CharField(max_length=200, blank=True)
    short_description = models.TextField(blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    is_lecturer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.discussion.title}"


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user.username} to {self.comment.user.username}"

class SubmittedAssignment(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to='submitted_assignments/')
    is_marked = models.BooleanField(default=False)
    total_score = models.PositiveIntegerField(null=True, blank=True)  # New field for the total score

    def __str__(self):
        return f"{self.assignment.title} submitted by {self.submitted_by.username}"
    
    