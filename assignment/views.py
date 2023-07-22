from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Course, Assignment, Discussion, Profile, SubmittedAssignment, Comment, Reply
from .forms import AssignmentForm, AssignmentFilterForm, DiscussionForm, UserSignUpForm, UserProfileForm, CommentForm, ReplyForm
from django.http import JsonResponse
from django.template.loader import render_to_string


def home(request):
    # Retrieve assignments and discussions to display on the home page
    assignments = Assignment.objects.all()
    discussions = Discussion.objects.all()
    return render(request, 'home.html', {'assignments': assignments, 'discussions': discussions})

@login_required
def view_profile(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('view_profile')

    else:
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'view_profile.html', {'profile_form': profile_form})

@login_required
def view_courses(request):
    if request.method == 'POST':
        level = request.POST.get('level')
        department = request.POST.get('department')
        semester = request.POST.get('semester')

        # Get the student's profile
        student_profile = Profile.objects.get(user=request.user)

        # Get all the courses that match the selected level, department, and semester
        courses = student_profile.courses.filter(level=level, department=department, semester=semester)

        # Prepare the courses as HTML
        courses_html = '<h2>Your Courses</h2><ul>'
        for course in courses:
            courses_html += f'<li>{course.title} - {course.code}</li>'
        courses_html += '</ul>'

        # Return the courses as JSON response
        return JsonResponse({'courses_html': courses_html})

    return render(request, 'view_courses.html')


# Custom function to check if a user is a lecturer
def is_lecturer(user):
    return user.profile.is_lecturer


# DISCUSSION
@login_required
@user_passes_test(is_lecturer)  # Only lecturers can access this view
def add_discussion(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST, request.FILES)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.lecturer = request.user
            discussion.save()
            messages.success(request, 'Discussion added successfully!')
            return redirect('home')
    else:
        form = DiscussionForm()
    return render(request, 'post_discussion.html', {'form': form})

@login_required
def list_all_discussions(request):
    discussions = Discussion.objects.all()
    return render(request, 'list_all_discussions.html', {'discussions': discussions})

@login_required
def view_discussion(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)
    comments = Comment.objects.filter(discussion=discussion)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.discussion = discussion
            comment.user = request.user
            comment.save()

            # Render the comment template and return as JSON response
            comment_html = render_to_string('comment.html', {'comment': comment})
            return JsonResponse({'comment_html': comment_html})
    else:
        form = CommentForm()

    return render(request, 'view_discussion.html', {
        'discussion': discussion,
        'comments': comments,
        'comment_form': form
    })

# Implement delete_discussion view
@login_required
@user_passes_test(is_lecturer)
def delete_discussion(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)

    if request.method == 'POST' and request.user == discussion.lecturer:
        discussion.delete()
        return redirect('home')

    return render(request, 'delete_discussion.html', {'discussion': discussion})


@login_required
def post_comment(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.discussion = discussion
            comment.user = request.user
            comment.save()

            # Render the comment template and return as JSON response
            comment_html = render_to_string('comment.html', {'comment': comment})
            return JsonResponse({'comment_html': comment_html})
    else:
        form = CommentForm()

    return JsonResponse({'error': 'Invalid request.'})  # Return an error response if not a POST request


@login_required
def post_reply(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = comment
            reply.user = request.user
            reply.save()

            # Render the reply template and return as JSON response
            reply_html = render_to_string('reply.html', {'reply': reply})
            return JsonResponse({'reply_html': reply_html})
    else:
        form = ReplyForm()

    return render(request, 'post_reply.html', {
        'comment': comment,
        'reply_form': form
    })

    
    
# ASSIGNMENT
@login_required
@user_passes_test(is_lecturer)  # Only lecturers can access this view
def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.lecturer = request.user
            assignment.save()
            messages.success(request, 'Assignment uploaded successfully!')
            return redirect('home')
    else:
        form = AssignmentForm()
    return render(request, 'post_assignment.html', {'form': form})

@login_required
@user_passes_test(is_lecturer)
def view_all_submitted_assignments(request):
    submitted_assignments = SubmittedAssignment.objects.filter(submitted_by=request.user)
    return render(request, 'view_all_submitted_assignments.html', {
        'submitted_assignments': submitted_assignments,
    })

@login_required
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == 'POST':
        form = SubmittedAssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            submitted_assignment = form.save(commit=False)
            submitted_assignment.assignment = assignment
            submitted_assignment.student = request.user
            submitted_assignment.save()
            messages.success(request, 'Assignment submitted successfully!')
            return redirect('home')
    else:
        form = SubmittedAssignmentForm()
    return render(request, 'submit_assignment.html', {'form': form, 'assignment': assignment})

@login_required
def view_assignment(request, assignment_id):
    # Retrieve the assignment using the assignment_id or return a 404 error if not found
    assignment = get_object_or_404(Assignment, id=assignment_id)

    return render(request, 'view_assignment.html', {'assignment': assignment})

@login_required
def list_assignments(request):
    levels = Course.objects.values_list('level', flat=True).distinct()
    semesters = Course.objects.values_list('semester', flat=True).distinct()
    departments = Course.objects.values_list('department', flat=True).distinct()

    if request.method == 'POST':
        form = AssignmentFilterForm(request.POST)
        if form.is_valid():
            level = form.cleaned_data['level']
            semester = form.cleaned_data['semester']
            department = form.cleaned_data['department']

            assignments = Assignment.objects.filter(course__level=level, course__semester=semester, course__department=department)
        else:
            assignments = Assignment.objects.all()
    else:
        assignments = Assignment.objects.all()
        form = AssignmentFilterForm()

    context = {
        'assignments': assignments,
        'levels': levels,
        'semesters': semesters,
        'departments': departments,
        'form': form,
    }
    return render(request, 'list_assignments.html', context)

   
@login_required
@user_passes_test(is_lecturer)  # Only lecturers can access this view
def view_submitted_assignments(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if not request.user == assignment.lecturer:
        return redirect('home')

    submitted_assignments = SubmittedAssignment.objects.filter(assignment=assignment)
    return render(request, 'view_submitted_assignments.html', {'submitted_assignments': submitted_assignments})


# Implement delete_assignment view
@login_required
@user_passes_test(is_lecturer)
def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)

    if request.method == 'POST' and request.user == assignment.lecturer:
        assignment.delete()
        return redirect('home')

    return render(request, 'delete_assignment.html', {'assignment': assignment})


@login_required
@user_passes_test(is_lecturer)
def mark_assignment(request, assignment_id):
    submitted_assignment = get_object_or_404(SubmittedAssignment, id=assignment_id)

    if request.method == 'POST':
        total_score = request.POST.get('total_score')
        if total_score:
            submitted_assignment.total_score = int(total_score)
            submitted_assignment.is_marked = True
            submitted_assignment.save()
            return redirect('view_all_marked_assignments')

    return render(request, 'mark_assignment.html', {'submitted_assignment': submitted_assignment})


@login_required
@user_passes_test(is_lecturer)  # Only lecturers can access this view
def view_all_marked_assignments(request):
    if not request.user.profile.is_lecturer:
        return redirect('home')

    marked_assignments = SubmittedAssignment.objects.filter(assignment__lecturer=request.user, is_marked=True)
    unmarked_assignments = SubmittedAssignment.objects.filter(assignment__lecturer=request.user, is_marked=False)
    return render(request, 'view_all_marked_assignments.html', {
        'marked_assignments': marked_assignments,
        'unmarked_assignments': unmarked_assignments
    })

@login_required
def view_all_my_marked_assignments(request):
    if request.user.profile.is_lecturer:
        return redirect('home')

    marked_assignments = SubmittedAssignment.objects.filter(assignment__lecturer=request.user, is_marked=True)
    unmarked_assignments = SubmittedAssignment.objects.filter(assignment__lecturer=request.user, is_marked=False)
    return render(request, 'view_all_my_marked_assignments.html', {
        'marked_assignments': marked_assignments,
        'unmarked_assignments': unmarked_assignments
    })
    
    
# AUTHENTICATIONS
def user_signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserSignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')
