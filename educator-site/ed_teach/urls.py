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

    # COURSE
    path('course/analytics/', r.course_analytics, name='analytics'),


    # ADD COURSE
    path('add-course/', r.redirect_to_course_overview, name='course-redirect'),
    path('add-course-overview/', r.add_course_overview, name='add-course'),
    path('add-course-data/', r.add_course_data, name='add-course-data'),


    # EDUCATOR
    path('educator/courses/', r.educator_courses, name='educator-courses'),
    path('educator/profile/', r.educator_profile, name='educator-profile'),
    path('educator/settings/', r.educator_settings, name='educator-settings'),

    
    path('educator/update-pfp/', r.user_pfp, name='profile-pic-update'),
    path('educator/<str:to_edit>/', r.user_edit, name='user-details-edit'),
    
    # path('educator/update-mobile/', r.user_pfp, name='mobile-update'),
    # path('educator/update-email/', r.user_pfp, name='email-update'),
    


    
    path('privacy/', r.privacy, name='privacy'),     
    path('terms/', r.terms, name='terms'),     
    
    path('about-us/', r.about_us, name='about-us'),      
    path('careers/', r.careers, name='careers'),     
    path('history/', r.history, name='history'),      
    path('gallery/', r.gallery, name='gallery'),          
    path('blogs/', r.blogs, name='blogs'),             
    path('contact-us/', r.contact_us, name='contact-us'),  

 
    path('terms/', r.terms, name='terms'),  
    path('testimonials/', r.testimonials, name='testimonials'),  

    path('collaborate/', r.collaborate, name='collaborate'),  
    path('reviews/', r.reviews, name='reviews'),  





    path('user-reviews/', r.goto_reviews, name='goto-reviews'),  
    path('user-review/', r.goto_reviews, name='goto-reviews'), 
    path('user_reviews/', r.goto_reviews, name='goto-reviews'),  
    path('user_review/', r.goto_reviews, name='goto-reviews'),   
    path('review/', r.goto_reviews, name='goto-reviews'),  
    
    # REST UNDEFINED PATTERNS
    re_path(r'^.*/$', r.bad_route, name='bad-route'),

]


urlpatterns += static(settings.MEDIA_URI,document_root=settings.MEDIA_ROOT)