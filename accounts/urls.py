from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    # Authentication
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # Core Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Academic & Features (Updated to match sidebar)
    path('grades/', views.grades_view, name='grades'),
    path('subjects/', views.subjects_view, name='subjects'), # New
    path('messages/', views.messages_view, name='messages'),
    path('activities/', views.activities_view, name='activities'),
    path('deadlines/', views.deadlines_view, name='deadlines'), # New
    path('scores/', views.scores_view, name='scores'), # New (Quiz & Exam Scores)
    path('attendance/', views.attendance_view, name='attendance'), # New
    
    # Feedback & Settings
    path('feedback/', views.feedback_view, name='feedback'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
    path('profile/', views.profile_view, name='profile'),
    
    # Admin
    path('admin/', admin.site.urls),
]