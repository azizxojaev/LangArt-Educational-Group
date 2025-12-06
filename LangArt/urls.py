from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('courses/', courses_page, name='courses'),
    path('course-details/', course_details_page, name='course-detail'),
    path('instructors/', instructors_page, name='instructors'),
    path('instructor-details/', instructor_details_page, name='instructor-detail'),
    path('pricing/', pricing_page, name='pricing'),
    path('contact/', contact_page, name='contact'),
]
