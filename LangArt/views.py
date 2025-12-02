from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html')


def home_page2(request):
    return render(request, 'index-2.html')


def home_page3(request):
    return render(request, 'index-3.html')


def home_page4(request):
    return render(request, 'index-4.html')


def home_page5(request):
    return render(request, 'index-5.html')


def home_page6(request):
    return render(request, 'index-6.html')


def about_page(request):
    return render(request, 'about.html')


def courses_page(request):
    return render(request, 'course.html')


def course_details_page(request):
    return render(request, 'course-details.html')


def instructors_page(request):
    return render(request, 'instructor.html')


def instructor_details_page(request):
    return render(request, 'instructor-details.html')


def pricing_page(request):
    return render(request, 'pricing.html')


def contact_page(request):
    return render(request, 'contact.html')