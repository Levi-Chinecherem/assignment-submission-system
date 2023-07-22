from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('view_courses/', views.view_courses, name='view_courses'),
    path('add_assignment/', views.add_assignment, name='add_assignment'),
    path('add_discussion/', views.add_discussion, name='add_discussion'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('view_discussion/<int:discussion_id>/', views.view_discussion, name='view_discussion'),
    path('post_comment/<int:discussion_id>/', views.post_comment, name='post_comment'),
    path('post_reply/<int:comment_id>/', views.post_reply, name='post_reply'),
    path('submit_assignment/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),
    path('view_submitted_assignments/<int:assignment_id>/', views.view_submitted_assignments, name='view_submitted_assignments'),
    path('mark_assignment/<int:submitted_assignment_id>/', views.mark_assignment, name='mark_assignment'),
    path('view_all_marked_assignments/', views.view_all_marked_assignments, name='view_all_marked_assignments'),
]
