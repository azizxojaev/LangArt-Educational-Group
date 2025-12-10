from django.shortcuts import render
from .models import *
from .utils import calculate_stars


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
    # Get course object
    course = Course.objects.get(slug=slug)

    # Get stars data
    stars_percent, stars_rating, total_stars, full_stars, half_star, empty_stars = calculate_stars(course)

    # Get reviews
    reviews = course.reviews.all()

    context = {
        'course': course,
        'stars_percent': stars_percent,
        'stars_rating': stars_rating,
        'total_stars': total_stars,
        'full_stars': range(full_stars),
        'half_star': half_star,
        'empty_stars': range(empty_stars),
        'reviews': reviews
    }

    return render(request, 'course-details.html', context=context)


def instructors_page(request):
    teachers = Teacher.objects.all()

    context = {
        'teachers': teachers
    }

    return render(request, 'instructor.html', context=context)


def instructor_details_page(request, slug):
    teacher = Teacher.objects.get(slug=slug)

    context = {
        'teacher': teacher
    }

    return render(request, 'instructor-details.html', context=context)


def pricing_page(request):
    return render(request, 'pricing.html')


def contact_page(request):
    contact = Contact.objects.get(id=1)

    context = {
        'contact': contact
    }

    return render(request, 'contact.html', context=context)