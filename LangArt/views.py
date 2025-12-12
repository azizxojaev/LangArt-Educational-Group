from django.shortcuts import render
from .models import *
from .utils import calculate_stars, send_message


def home_page(request):
    contact = Contact.objects.get(id=1)
    context = {
        'contact': contact
    }

    return render(request, 'index.html', context=context)

def about_page(request):
    teachers = Teacher.objects.order_by('-students')[:4]
    contact = Contact.objects.get(id=1)

    context = {
        'teachers': teachers,
        'contact': contact
    }

    return render(request, 'about.html', context=context)


def courses_page(request):
    courses = Course.objects.all()
    contact = Contact.objects.get(id=1)

    context = {
        'courses': courses,
        'contact': contact
    }

    return render(request, 'course.html', context=context)


def course_details_page(request, slug):
    contact = Contact.objects.get(id=1)
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
        'reviews': reviews,
        'contact': contact
    }

    return render(request, 'course-details.html', context=context)


def instructors_page(request):
    teachers = Teacher.objects.all()
    contact = Contact.objects.get(id=1)

    context = {
        'teachers': teachers,
        'contact': contact
    }

    return render(request, 'instructor.html', context=context)


def instructor_details_page(request, slug):
    teacher = Teacher.objects.get(slug=slug)
    contact = Contact.objects.get(id=1)

    context = {
        'teacher': teacher,
        'contact': contact
    }

    return render(request, 'instructor-details.html', context=context)


def pricing_page(request):
    courses = Course.objects.all()
    contact = Contact.objects.get(id=1)

    context = {
        'courses': courses,
        'contact': contact
    }

    return render(request, 'pricing.html', context=context)


def contact_page(request):
    contact = Contact.objects.get(id=1)
    courses = Course.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        course = request.POST.get("courses")
        level = request.POST.get("levels")
        message = request.POST.get("message")

        send_message(f"Name: {name}\nPhone Number: {phone}\nEmail: {email}\nCourse: {course}\nLevel: {level}\nMessage: {message}")

    context = {
        'contact': contact,
        'courses': courses
    }

    return render(request, 'contact.html', context=context)