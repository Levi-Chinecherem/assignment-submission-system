from django.urls import path
from . import views

urlpatterns = [
    # Home view
    path('', views.home, name='home'),

    # User authentication URLs
    path('signup/', views.user_signup, name='user_signup'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),

    # User profile view
    path('view_profile/', views.view_profile, name='view_profile'),

    # Assignment-related URLs
    path('list_assignments/', views.list_assignments, name='list_assignments'),
    path('view_assignment/<int:assignment_id>/', views.view_assignment, name='view_assignment'),
    path('submit_assignment/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),
    path('view_all_my_marked_assignments/', views.view_all_my_marked_assignments, name='view_all_my_marked_assignments'),

    # Discussion-related URLs
    path('list_all_discussions/', views.list_all_discussions, name='list_all_discussions'),
    path('view_discussion/<int:discussion_id>/', views.view_discussion, name='view_discussion'),
    path('comment/<int:discussion_id>/', views.post_comment, name='comment_on_discussion'),
    path('reply/<int:comment_id>/', views.post_reply, name='reply_to_comment'),

    # Lecturer-specific URLs
    path('post_assignment/', views.add_assignment, name='post_assignment'),
    path('delete_assignment/<int:assignment_id>/', views.delete_assignment, name='delete_assignment'),
    path('post_discussion/', views.add_discussion, name='post_discussion'),
    path('delete_discussion/<int:discussion_id>/', views.delete_discussion, name='delete_discussion'),
    path('view_all_marked_assignments/', views.view_all_marked_assignments, name='view_all_marked_assignments'),
    path('view_all_submitted_assignments/', views.view_all_submitted_assignments, name='view_all_submitted_assignments'),
    path('mark_assignment/<int:assignment_id>/', views.mark_assignment, name='mark_assignment'),

    # Course view URL
    path('view_courses/', views.view_courses, name='view_courses'),
]
