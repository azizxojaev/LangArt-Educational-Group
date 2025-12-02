from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('2/', home_page2, name='home2'),
    path('3/', home_page3, name='home3'),
    path('4/', home_page4, name='home4'),
    path('5/', home_page5, name='home5'),
    path('6/', home_page6, name='home6'),
    path('about/', about_page, name='about'),
    path('courses/', courses_page, name='courses'),
    path('course-details/', course_details_page, name='course-detail'),
    path('instructors/', instructors_page, name='instructors'),
    path('instructor-details/', instructor_details_page, name='instructor-detail'),
    path('pricing/', pricing_page, name='pricing'),
    path('contact/', contact_page, name='contact'),
]
