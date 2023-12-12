
from django.contrib import admin
from django.urls import path, re_path

from app import views as r

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME ROUTING
    path('', r.goto_homepage_or_landing, name='redirections'),
    path('home/', r.homepage, name='dash-homepage'),              # <---- for the signed-in
    path('home/courses/', r.courses, name='home-courses'),              # <---- for the signed-in             
    path('home/courses/<str:course_type>/', r.show_specific_course_page, name='home-specific-course' ),       # <---- for the signed-in


    # SIGNIN AND LOGIN
    path('signup/', r.signup, name='user-signup'),
    path('login/', r.login, name='user-login'),
    path('logout/', r.logout, name='user-logout'),



    # USER PROFILE
    path('user/', r.goto_user_profile, name='redirect-to-profile'),
    # path('user/profile/', r.show_user_profile, name='show-user'),
    path('user/my-learning/', r.goto_user_enrollments, name='goto-user-enrollments'), 
    path('user/my-learning/enrolled/', r.user_enrollments, name='user-enrollments'), 
    path('user/my-learning/my-lists/', r.user_lists, name='user-lists'),                  # <---- for the signed-in
    path('user/my-learning/ongoing/', r.user_ongoing, name='user-ongoing'),
    path('user/settings/', r.user_settings, name='user-settings'),              # <---- for the signed-in


    # REST UNDEFINED PATTERNS
    re_path(r'^.*/$', r.bad_route, name='bad-route'),

    # path('home/courses/development/', r.show_specific_course_page, name='home-courses-development'),              # <---- for the signed-in  
    # path('home/courses/business/', r.show_specific_course_page, name='home-courses-business'),              # <---- for the signed-in  
    # path('home/courses/finance-and-accounting/', r.show_specific_course_page, name='home-courses-finance-and-accounting'),              # <---- for the signed-in  
    # path('home/courses/it-and-software/', r.show_specific_course_page, name='home-courses-it-and-software'),              # <---- for the signed-in   
    # path('home/courses/office-productivity/', r.show_specific_course_page, name='home-courses-office-productivity'),              # <---- for the signed-in  
    # path('home/courses/personal-development/', r.show_specific_course_page, name='home-courses-personal-development'),              # <---- for the signed-in  
    # path('home/courses/design/', r.show_specific_course_page, name='home-courses-design'),              # <---- for the signed-in  
    # path('home/courses/marketing/', r.show_specific_course_page, name='home-courses-marketing'),              # <---- for the signed-in   
    # path('home/courses/lifestyle/', r.show_specific_course_page, name='home-courses-lifestyle'),              # <---- for the signed-in  
    # path('home/courses/photography-and-video/', r.show_specific_course_page, name='home-courses-photography-and-video'),              # <---- for the signed-in  
    # path('home/courses/health-and-fitness/', r.show_specific_course_page, name='home-courses-health-and-fitness'),              # <---- for the signed-in  
    # path('home/courses/music/', r.show_specific_course_page, name='home-courses-music'),              # <---- for the signed-in  
    # path('home/courses/teaching-and-academics/', r.show_specific_course_page, name='home-courses-teaching-and-academics'),              # <---- for the signed-in             # <---- for the signed-in
]
