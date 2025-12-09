from django.shortcuts import render
from .models import Course


def home_page(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')


def courses_page(request):
    courses = Course.objects.all()

    context = {
        'courses': courses
    }

    return render(request, 'course.html', context=context)


def course_details_page(request, slug):
    course = Course.objects.get(slug=slug)

    context = {
        'course': course
    }

    return render(request, 'course-details.html', context=context)


def instructors_page(request):
    return render(request, 'instructor.html')


def instructor_details_page(request):
    return render(request, 'instructor-details.html')


def pricing_page(request):
    return render(request, 'pricing.html')


def contact_page(request):
    return render(request, 'contact.html')