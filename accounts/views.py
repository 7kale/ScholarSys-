from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserForm, ProfileForm

# --- Authentication Views (Register, Login, Logout remain the same) ---

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        major = request.POST.get('major', '').strip()
        student_id = request.POST.get('student_id', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        if not username or not password:
            messages.error(request, "Username and password are required!")
            return render(request, 'accounts/register.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'accounts/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'accounts/register.html')

        user = User.objects.create_user(username=username, password=password, email=email)
        # set names
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # create profile
        profile, _ = Profile.objects.get_or_create(user=user)
        profile.major = major
        profile.student_id = student_id
        profile.save()

        messages.success(request, "Account created! You can now login.")
        return redirect('login')

    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, "Please enter username and password")
            return render(request, 'accounts/login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('login')

# --- Main Dashboard View ---

def dashboard_view(request):
    # Sample data to match your screenshots
    # Include profile info when user is authenticated
    profile_full = {}
    user = request.user
    if user.is_authenticated:
        profile, _ = Profile.objects.get_or_create(user=user)
        full_name = user.get_full_name() or f"{user.first_name} {user.last_name}".strip() or user.username
        profile_full = {
            'full_name': full_name,
            'major': profile.major or 'Bachelor in Information Systems',
            'email': user.email or '',
            'student_id': profile.student_id or '',
        }

    context = {
        'gpa': '3.70',
        'attendance_rate': '94%',
        'pending_assignments': 4,
        'faculty_messages_count': 4,
        'recent_activities': [
            {'name': 'Math Assignment Chapter 5', 'subject': 'Mathematics', 'deadline': 'Feb 16, 2026', 'status': 'ONGOING'},
            {'name': 'Physics Lab Report', 'subject': 'Physics', 'deadline': 'Feb 14, 2026', 'status': 'MISSING'},
            {'name': 'Literature Essay', 'subject': 'English Literature', 'deadline': 'Feb 13, 2026', 'status': 'COMPLETED'},
        ],
        'semester_performance': [
            {'subject': 'MATHEMATICS', 'grade': 'A', 'percentage': '92%'},
            {'subject': 'PHYSICS', 'grade': 'B+', 'percentage': '87%'},
            {'subject': 'CHEMISTRY', 'grade': 'A-', 'percentage': '90%'},
            {'subject': 'ENGLISH LITERATURE', 'grade': 'A', 'percentage': '95%'},
            {'subject': 'HISTORY', 'grade': 'B', 'percentage': '83%'},
        ]
    }

    # merge profile keys into context for template convenience
    context.update(profile_full)
    return render(request, 'accounts/dashboard.html', context)

# --- Sidebar Features ---

def grades_view(request):
    return render(request, 'accounts/grades.html')

def subjects_view(request):
    # Added to fix AttributeError
    return render(request, 'accounts/subjects.html')

def messages_view(request):
    teachers = ['Mr. Smith', 'Ms. Dela Cruz', 'Prof. Michael Chen']
    context = {'teachers': teachers}
    return render(request, 'accounts/messages.html', context)

def activities_view(request):
    activities = [
        {'name': 'Math Homework 1', 'deadline': 'Feb 12, 2026', 'status': 'Submitted ✅'},
        {'name': 'Science Lab Report', 'deadline': 'Feb 10, 2026', 'status': 'Missing ❌'},
        {'name': 'English Essay', 'deadline': 'Feb 15, 2026', 'status': 'Pending ⏳'}
    ]
    context = {'activities': activities}
    return render(request, 'accounts/activities.html', context)

def deadlines_view(request):
    # Added to fix AttributeError
    return render(request, 'accounts/deadlines.html')

def scores_view(request):
    # Added to fix AttributeError (Quiz & Exam Scores)
    return render(request, 'accounts/scores.html')

def attendance_view(request):
    # Added to fix AttributeError
    return render(request, 'accounts/attendance.html')

def feedback_view(request):
    feedbacks = [
        'Mr. Smith: "Great participation in class!"',
        'Ms. Dela Cruz: "Need to improve essay structure."',
        'Prof. Santos: "Excellent project work!"'
    ]
    context = {'feedbacks': feedbacks}
    return render(request, 'accounts/feedback.html', context)

def profile_view(request):
    user = request.user

    full_name = None
    email = None
    major = None
    student_id = None

    if user.is_authenticated:
        full_name = user.get_full_name() or f"{user.first_name} {user.last_name}".strip() or user.username
        email = user.email

        # Ensure profile exists
        profile, _ = Profile.objects.get_or_create(user=user)
        major = profile.major
        student_id = profile.student_id

    context = {
        'full_name': full_name or 'Lyka Leanna Paguagan',
        'major': major or 'Bachelor in Information Systems',
        'email': email or 'leannalean7@gmail.com',
        'student_id': student_id or '0461-1',
    }

    return render(request, 'accounts/profile.html', context)



@login_required
def profile_edit_view(request):
    user = request.user
    profile, _ = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        uform = UserForm(request.POST, instance=user)
        pform = ProfileForm(request.POST, instance=profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        uform = UserForm(instance=user)
        pform = ProfileForm(instance=profile)

    # include profile data so the sidebar shows name and id
    full_name = user.get_full_name() or f"{user.first_name} {user.last_name}".strip() or user.username
    context = {
        'uform': uform,
        'pform': pform,
        'full_name': full_name,
        'student_id': profile.student_id or '',
        'major': profile.major or '',
        'email': user.email or '',
    }
    return render(request, 'accounts/profile_edit.html', context)