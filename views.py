# resume/views.py

from django.shortcuts import render, redirect

def home(request):
    """
    Renders the main resume builder form.
    """
    return render(request, 'index.html')

def generate_resume(request):
    """
    Handles form submission and renders the resume template directly.
    """
    if request.method == 'POST':
        # Retrieve form data in a structured way using list comprehensions
        resume_data = {
            'name': request.POST.get('name', ''),
            'about': request.POST.get('about', ''),
            'email': request.POST.get('email', ''),
            'phone': request.POST.get('phone', ''),
            'linkedin': request.POST.get('linkedin', ''),
            'github': request.POST.get('github', ''),
            'skills': [request.POST.get(f'skill{i}', '') for i in range(1, 6) if request.POST.get(f'skill{i}')],
            'languages': [request.POST.get(f'lang{i}', '') for i in range(1, 4) if request.POST.get(f'lang{i}')],
            'education': [
                {'degree': request.POST.get(f'degree{i}'), 'college': request.POST.get(f'college{i}'), 'year': request.POST.get(f'year{i}')}
                for i in range(1, 4) if request.POST.get(f'degree{i}')
            ],
            'projects': [
                {'title': request.POST.get(f'project{i}'), 'duration': request.POST.get(f'durat{i}'), 'description': request.POST.get(f'desc{i}')}
                for i in range(1, 3) if request.POST.get(f'project{i}')
            ],
            'experience': [
                {'company': request.POST.get(f'company{i}'), 'post': request.POST.get(f'post{i}'), 'duration': request.POST.get(f'duration{i}'), 'description': request.POST.get(f'lin{i}')}
                for i in range(1, 4) if request.POST.get(f'company{i}')
            ],
            'achievements': [request.POST.get(f'achieve{i}', '') for i in range(1, 4) if request.POST.get(f'achieve{i}')],
        }
        
        # Render the resume template directly with the form data
        return render(request, 'resume_template.html', resume_data)

    return redirect('home')