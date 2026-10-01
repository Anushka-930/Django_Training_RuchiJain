from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import TestResult

QUESTIONS = [
    {
        'question': 'What does HTML stand for?',
        'options': ['Hyper Text Markup Language', 'High Text Machine Language', 'Home Tool Markup Language', 'Hyperlink Text Management Language'],
        'answer': 0,
    },
    {
        'question': 'Which language is used to style web pages?',
        'options': ['Python', 'CSS', 'SQL', 'Django'],
        'answer': 1,
    },
    {
        'question': 'Which command starts a Django development server?',
        'options': ['python manage.py runserver', 'django start server', 'python django server', 'manage.py launch'],
        'answer': 0,
    },
    {
        'question': 'Which database is used by this project by default?',
        'options': ['MySQL', 'MongoDB', 'SQLite', 'Oracle'],
        'answer': 2,
    },
    {
        'question': 'Which Django file usually contains page routes?',
        'options': ['models.py', 'urls.py', 'admin.py', 'apps.py'],
        'answer': 1,
    },
]

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        name = request.POST.get('name', '').strip()

        if not username or not password:
            return render(request, 'signup.html', {'error': 'Username and password are required.'})
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'That username is already registered.'})

        User.objects.create_user(username=username, password=password, first_name=name)
        return redirect('login')
    return render(request, 'signup.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {'username': request.user.username})

@login_required(login_url='login')
def test(request, test_id):
    question_count = min(max(test_id, 1), len(QUESTIONS))
    questions = QUESTIONS[:question_count]

    if request.method == 'POST':
        score = sum(
            request.POST.get(f'answer_{index}') == str(question['answer'])
            for index, question in enumerate(questions)
        )
        TestResult.objects.create(
            user=request.user,
            attempt=question_count,
            right=score,
            wrong=question_count - score,
            points=score,
        )
        return render(request, 'test.html', {
            'questions': questions,
            'score': score,
            'submitted': True,
        })

    return render(request, 'test.html', {'questions': questions})

@login_required(login_url='login')
def history(request):
    results = TestResult.objects.filter(user=request.user)
    return render(request, 'history.html', {
        'username': request.user.username,
        'results': results,
        'total_tests': results.count(),
        'total_points': sum(result.points for result in results),
    })

def logout(request):
    auth_logout(request)
    return redirect('login')