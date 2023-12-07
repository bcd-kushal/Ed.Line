
from django.contrib import admin
from django.urls import path, re_path

from app import views as r

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME ROUTING
    path('', r.goto_homepage_or_landing, name='redirections'),
    path('home/', r.homepage, name='dash-homepage'),              # <---- for the signed-in
    path('home/courses/', r.courses, name='home-courses'),              # <---- for the signed-in             # <---- for the signed-in



    # SIGNIN AND LOGIN
    path('signup/', r.signup, name='user-signup'),
    path('login/', r.login, name='user-login'),
    path('logout/', r.logout, name='user-logout'),



    # USER PROFILE
    path('user/', r.goto_user_profile, name='redirect-to-profile'),
    # path('user/profile/', r.show_user_profile, name='show-user'),
    path('user/enrollments/', r.user_enrollments, name='user-enrollments'),              # <---- for the signed-in
    path('user/settings/', r.user_settings, name='user-settings'),              # <---- for the signed-in


    # REST UNDEFINED PATTERNS
    re_path(r'^.*/$', r.bad_route, name='bad-route'),

]
