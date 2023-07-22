from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Course, Assignment, Discussion, Comment, Reply, SubmittedAssignment

User = get_user_model()

class AssignmentSubmissionTests(TestCase):
    def setUp(self):
        # Create a test user with is_lecturer set to True
        self.lecturer_user = User.objects.create_user(username='lecturer1', email='lecturer1@example.com', password='password', is_lecturer=True)

        # Create a test user with is_lecturer set to False (student)
        self.student_user = User.objects.create_user(username='student1', email='student1@example.com', password='password', is_lecturer=False)

        # Create some test courses
        self.level_100 = Course.objects.create(code='CSE101', title='Introduction to Computer Science', level='100', department='Computer Science', semester='First')
        self.level_200 = Course.objects.create(code='MATH201', title='Calculus II', level='200', department='Mathematics', semester='Second')

        # Create some test assignments
        self.assignment1 = Assignment.objects.create(title='Assignment 1', course=self.level_100, semester=self.level_100.semester, level=self.level_100.level, lecturer=self.lecturer_user, department=self.level_100.department)
        self.assignment2 = Assignment.objects.create(title='Assignment 2', course=self.level_200, semester=self.level_200.semester, level=self.level_200.level, lecturer=self.lecturer_user, department=self.level_200.department)

        # Create some test discussions
        self.discussion1 = Discussion.objects.create(title='Discussion 1', short_description='This is a discussion.', long_description='Long description for discussion 1.', outro='Discussion 1 outro', lecturer=self.lecturer_user)
        self.discussion2 = Discussion.objects.create(title='Discussion 2', short_description='This is another discussion.', long_description='Long description for discussion 2.', outro='Discussion 2 outro', lecturer=self.lecturer_user)

    def test_assignment_submission(self):
        # Test submitting an assignment by a student
        self.client.login(username='student1', password='password')
        submission_url = reverse('submit_assignment', args=[self.assignment1.id])
        response = self.client.post(submission_url, {'document': 'path/to/submission.pdf'})
        self.assertEqual(response.status_code, 302)  # 302 is the status code for a redirect
        self.assertEqual(SubmittedAssignment.objects.count(), 1)
        submitted_assignment = SubmittedAssignment.objects.first()
        self.assertEqual(submitted_assignment.assignment, self.assignment1)
        self.assertEqual(submitted_assignment.submitted_by, self.student_user)
        self.assertFalse(submitted_assignment.is_marked)
        self.assertIsNone(submitted_assignment.total_score)

    def test_assignment_marking(self):
        # Test marking an assignment by a lecturer
        self.client.login(username='lecturer1', password='password')
        marking_url = reverse('mark_assignment', args=[self.assignment1.id])
        response = self.client.post(marking_url, {'total_score': 90})
        self.assertEqual(response.status_code, 302)  # 302 is the status code for a redirect
        marked_assignment = SubmittedAssignment.objects.get(assignment=self.assignment1, submitted_by=self.student_user)
        self.assertTrue(marked_assignment.is_marked)
        self.assertEqual(marked_assignment.total_score, 90)

    def test_discussion_comment_and_reply(self):
        # Test posting a comment on a discussion by a student
        self.client.login(username='student1', password='password')
        comment_url = reverse('post_comment', args=[self.discussion1.id])
        response = self.client.post(comment_url, {'text': 'This is a comment.'})
        self.assertEqual(response.status_code, 302)  # 302 is the status code for a redirect
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.first()
        self.assertEqual(comment.discussion, self.discussion1)
        self.assertEqual(comment.user, self.student_user)
        self.assertEqual(comment.text, 'This is a comment.')

        # Test replying to a comment on a discussion by a lecturer
        self.client.login(username='lecturer1', password='password')
        reply_url = reverse('post_reply', args=[comment.id])
        response = self.client.post(reply_url, {'text': 'This is a reply.'})
        self.assertEqual(response.status_code, 302)  # 302 is the status code for a redirect
        self.assertEqual(Reply.objects.count(), 1)
        reply = Reply.objects.first()
        self.assertEqual(reply.comment, comment)
        self.assertEqual(reply.user, self.lecturer_user)
        self.assertEqual(reply.text, 'This is a reply.')
