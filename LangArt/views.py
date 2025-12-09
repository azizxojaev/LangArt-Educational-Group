from django.shortcuts import render
from .models import *


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

    total_stars = course.how_much_5stars + course.how_much_4stars + course.how_much_3stars + course.how_much_2stars + course.how_much_1stars
    stars_percent = {
        5: round(course.how_much_5stars / total_stars * 100),
        4: round(course.how_much_4stars / total_stars * 100),
        3: round(course.how_much_3stars / total_stars * 100),
        2: round(course.how_much_2stars / total_stars * 100),
        1: round(course.how_much_1stars / total_stars * 100)
    }
    stars_rating = round(((course.how_much_5stars*5) + (course.how_much_4stars*4) + (course.how_much_3stars*3) + (course.how_much_2stars*2) + (course.how_much_1stars*1)) / total_stars, 1)
    full_stars = int(round(stars_rating))
    if stars_rating >= full_stars:
        half_star = 1 if (stars_rating - full_stars) <= 0.5 else 0
    else:
        half_star = 1 if (full_stars - stars_rating) >= 0.5 else 0

    empty_stars = 5 - full_stars - half_star

    context = {
        'course': course,
        'stars_percent': stars_percent,
        'stars_rating': stars_rating,
        'total_stars': total_stars,
        'full_stars': range(full_stars),
        'half_star': half_star,
        'empty_stars': range(empty_stars),
    }

    return render(request, 'course-details.html', context=context)


def instructors_page(request):
    return render(request, 'instructor.html')


def instructor_details_page(request):
    return render(request, 'instructor-details.html')


def pricing_page(request):
    return render(request, 'pricing.html')


def contact_page(request):
    contact = Contact.objects.get(id=1)

    context = {
        'contact': contact
    }

    return render(request, 'contact.html', context=context)