from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


from app import views as r



urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME ROUTING
    path('', r.goto_homepage_or_landing, name='redirections'),
    path('home/', r.homepage, name='dash-homepage'),

    # SIGNIN AND LOGIN
    path('signup/', r.signup, name='user-signup'),
    path('login/', r.login, name='user-login'),
    path('logout/', r.logout, name='user-logout'),

    #ADD COURSE
    path('add-pfp/', r.user_pfp, name='add-pfp'),
    path('add-course/', r.add_course, name='add-course'),



    
    # REST UNDEFINED PATTERNS
    re_path(r'^.*/$', r.bad_route, name='bad-route'),

]


urlpatterns += static(settings.MEDIA_URI,document_root=settings.MEDIA_ROOT)