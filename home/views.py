
from django.shortcuts import render


def home_page(request):
    return render(request, 'home/index.html')


def about_page(request):
    return render(request, 'home/about.html')


def students_page(request):
    students = [
        {"name": "Sangeerthan", "mark": 85},
        {"name": "Kamal", "mark": 72},
        {"name": "Nimal", "mark": 91},
    ]

    return render(
        request,
        'home/students.html',
        {'students': students}
    )
