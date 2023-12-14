import json
import time
import threading


from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate as default_authenticate, login as LoginUser, logout as LogoutUser
from django.contrib.auth.models import User as RegisteredUsers
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt

from .utils import *
from .side_data import *
from .dashboard_data import *
from .courses import all_courses



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from datetime import datetime

from .forms import LoginForm, SignupForm

MOBILE = ""

ATLAS_URI = ""


def helper():
    global MOBILE
    time.sleep(1.5)
    MOBILE = ""


# ###############################################################################################################
        # ########## HOME ROUTING ############################################################################### 
# ###############################################################################################################

# @/
def goto_homepage_or_landing(req):
    global MOBILE 

    if req.method == "POST":
        if(req.POST.get("landing_mobile")):
            MOBILE=req.POST.get("landing_mobile")

            # run this in thread
            thread1 = threading.Thread(target=helper)
            thread1.start()

            if RegisteredUsers.objects.filter(username=req.POST.get("landing_mobile")).exists():
                return redirect('/login/')
            else:
                return redirect('/signup/')
        
        else:
            return send_bad_request(req)
        
    # -----------------------------------------------------------------
    elif req.method == "GET":
        # depending upon if user is logged-in or not, we route:
        #       user exists: src/dashboard/home.html
        #       no user:     src/landing/landing.html

        if req.user.username == None or req.user.username == '':
            CONTEXT = {
                "tab_title": "Ed.Line - Your Right, Our Website"
            }
            return render(req,"src/landing/landing.html",CONTEXT)
        else:
            return redirect('home/')

    # -----------------------------------------------------------------
    else: 
        return send_bad_request(req)




# @home/
def homepage(req):
    if req.method not in ["GET","POST"]:
        return send_bad_request(req)
    
    # -----------------------------------------------------------------
    else:
        # depending upon if user is logged-in or not, we route:
        #       user exists: src/dashboard/home.html
        #       no user:     src/home/landing.html

        if req.user.username == None or req.user.username == '':
            return redirect('/')
        else:
            SLIDERS = slider_pics(req.user.username,req.user.first_name)

            CONTEXT = {
                "tab_title": "Home|Ed.Line",
                "full_name": req.user.first_name + " " + req.user.last_name,
                "join_date": req.user.date_joined,
                "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2],    

                "slider_pics": SLIDERS,
                "slider_pics_total": len(SLIDERS),

                "dash_relearn": get_start_learning(req.user.username,req.user.first_name),
                "dash_quick_links": get_quick_links(req.user.username,req.user.first_name),
                "dash_top_pick": get_top_pick(req.user.username,req.user.first_name),
                "dash_course_ribbons": fetch_dashboard_ribbons(req.user.username,req.user.first_name),
                "homepage": 1
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)









# @home/courses/
def courses(req):
    if req.method != "GET":
        return send_bad_request()
    else:
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:
            CONTEXT = {
                "fname": req.user.first_name,
                "full_name": req.user.first_name + " " + req.user.last_name,
                "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2],    
                "join_date": req.user.date_joined,
                "tab_title": "Courses|Ed.Line",
                "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2],    
                "courses": 1
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)





# @home/courses/*
def show_specific_course_page(req,course_type):
    print(course_type)
    if req.method != "GET":
        return send_bad_request()
    else:
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:


            subcourses = all_courses()


            CONTEXT = {
                "fname": req.user.first_name,
                "tab_title": f"{course_type}|Courses|Ed.Line",
                "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2],    
                "full_name": req.user.first_name + " " + req.user.last_name,
                "join_date": req.user.date_joined,
                
                "subcourse_names": subcourses[course_type],
                "popular_courses": [
                    {
                        "title":"NextJS: The Complete Guide",
                        "thumbnail": "https://img-b.udemycdn.com/course/240x135/3873464_403c_3.jpg",
                        "language": "EN",
                        "courseType": "DEVELOPMENT",
                        "rating": "4.4",
                        "total_ratings": "6.6K",
                        "educator_name": "Rudra Kumar Mishra",
                        "educator_pfp": "https://static.uacdn.net/thumbnail/user/default.png?q=75&auto=format%2Ccompress&w=256",
                        "footer_course_details": "210 lectures • 4 PDFs • 2 Tests"
                    },
                    
                    {
                        "title":"TypeScript and JavaScript: A Deep Dive",
                        "thumbnail": "https://img-c.udemycdn.com/course/240x135/986406_89c5_3.jpg",
                        "language": "EN",
                        "courseType": "Development",
                        "rating": "4.2",
                        "total_ratings": "2.1K",
                        "educator_name": "Kushal Kumar",
                        "educator_pfp": "https://static.uacdn.net/thumbnail/user/default.png?q=75&auto=format%2Ccompress&w=256",
                        "footer_course_details": "426 lectures • 23 PDFs • 56 Tests"
                    },
                    
                    {
                        "title":"Machine Learning A-Z: AI, Python + ChatGPT Bonus",
                        "thumbnail": "https://img-c.udemycdn.com/course/240x135/950390_270f_3.jpg",
                        "language": "ES",
                        "courseType": "DEVELOPMENT",
                        "rating": "4.5",
                        "total_ratings": "178K",
                        "educator_name": "Kyle Perkins",
                        "educator_pfp": "https://static.uacdn.net/thumbnail/user/default.png?q=75&auto=format%2Ccompress&w=256",
                        "footer_course_details": "82 lectures • 1 PDF"
                    },
                    
                    {
                        "title":"Complete C# Unity Game Developer 2D",
                        "thumbnail": "https://img-c.udemycdn.com/course/240x135/2514486_c4e0.jpg",
                        "language": "EN",
                        "courseType": "Development",
                        "rating": "4.7",
                        "total_ratings": "101K",
                        "educator_name": "Gary Pettie",
                        "educator_pfp": "https://static.uacdn.net/thumbnail/user/default.png?q=75&auto=format%2Ccompress&w=256",
                        "footer_course_details": "103 lectures • 9 Tests"
                    },
                    
                    {
                        "title":"Networking in a Gist",
                        "thumbnail": "https://img-c.udemycdn.com/course/240x135/751094_fb27_2.jpg",
                        "language": "EN",
                        "courseType": "Development",
                        "rating": "4.6",
                        "total_ratings": "369",
                        "educator_name": "Rudra Kumar Mishra",
                        "educator_pfp": "https://static.uacdn.net/thumbnail/user/default.png?q=75&auto=format%2Ccompress&w=256",
                        "footer_course_details": "26 lectures • 1 Tests"
                    }
                ],
                "specific_course": format_change_title(course_type),
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)



# ###############################################################################################################
        # ########## LOGIN LOGOUT SIGNUP ######################################################################## 
# ###############################################################################################################

# @login/
def login(req):
    global MOBILE 

    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            mobile = form.cleaned_data["username"]
            # mail = form.cleaned_data["email_or_mobile"]
            password = form.cleaned_data["password"]


            # print(f"mail={mail} | pass={login_password}")
            # print(f"LOGGED IN :/> full name={mobile} | pass={password}")

            
            # logout user before logging in
            LogoutUser(req)


            user_exists = default_authenticate(req,username=mobile,password=password)

            if user_exists is not None:
                LoginUser(req,user_exists)
                return redirect('/home/')
            else:
                return redirect('/login/')
        
        else: 
            return redirect('/login/')
    # -----------------------------------------------------------------
    
    elif req.method == "GET":
        if req.user.username == None or req.user.username == "":
            CONTEXT = {
                "tab_title": "LogIn|Ed.Line",
                "login": 1,
                "given_mobile": MOBILE,
                "LF": LoginForm()
            }
            return render(req,"src/auth/_base_structure.html",CONTEXT)
        else:
            return redirect('/home/')

    # -----------------------------------------------------------------
    else:
        return send_bad_request(req)
    

# @logout/
def logout(req):
    if req.method in ["GET","POST"]:
        if req.user.username == None or req.user.username == "":
            return redirect('')
        else:
            LogoutUser(req)
            return redirect('/login/')
        
    # elif req.method == "GET":
    #     if req.user.username == None or req.user.username == "":
    #         return redirect('')
    #     else: 

        
    # -----------------------------------------------------------------
    else:
        return send_bad_request(req)



# @signup/
def signup(req):
    global MOBILE 

    if req.method == "POST":
        form = SignupForm(req.POST)
        if form.is_valid():

            # first get all the data from signup form ---------------
            phone = form.cleaned_data["user"]
            fname = form.cleaned_data["fname"]
            email = form.cleaned_data["email"]
            pass1 = form.cleaned_data["pass1"]
            # TIME_RN = get_date_time_rn()

            print("--------------------------------------------")
            user_names = fname.split()
            lname = user_names[1] if len(user_names)>1 else ""
            fname = user_names[0]

            print("fname:",fname,"| lname:",lname)

            LogoutUser(req)

            # check if this User already exists or not
            if RegisteredUsers.objects.filter(username=phone).exists():
                return redirect('/login/')
            if RegisteredUsers.objects.filter(email=email).exists():
                return redirect('/login/')
            


            # next create a new user from User models   
            registered_user = RegisteredUsers.objects.create_user(
                                                            username=phone,
                                                            first_name=fname,
                                                            last_name=lname,
                                                            email=email,
                                                            password=pass1,
                                                            is_superuser=False,
                                                            date_joined=datetime.now()
                                                        )
            
            LoginUser(req, registered_user)





            print(f"FULL NAME: {fname} {lname} | PASSWORD: {pass1} | EMAIL ID: {email}")
            return redirect('/home/')


        else:
            return redirect('/signup/')

    
    # -----------------------------------------------------------------
    elif req.method == "GET":
        if req.user.username == None or req.user.username == "":
            # print("\n##########################... ", MOBILE)
            CONTEXT = {
                "tab_title": "SignUp|Ed.Line",
                "signup": 1,
                "given_mobile": MOBILE,
                "SF": SignupForm()
            }
            return render(req,"src/auth/_base_structure.html",CONTEXT)
        else:
            return redirect("/home/")

    # -----------------------------------------------------------------
    else:
        return send_bad_request(req)





# ------------ UTILS --------------------------------------------------





# ###############################################################################################################
        # ########## USER AREA  ############################################################### 
# ###############################################################################################################

# @user/
def goto_user_profile(req):
    if req.method != "GET":
        return send_bad_request()
    else:
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:
            return redirect('/user/settings/')
            
            

# @user/settings/
# def show_user_settings(req):
#     if req.method == "GET":
#         if req.user.username == None or req.user.username == "":
#             return redirect('/')
#         else:
#             CONTEXT = {
#                 "fname": req.user.first_name,
#                 "tab_title": f"{req.user.first_name} {req.user.last_name}|Ed.Line",
#                 "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2],    
#                 "settings": 1
#             }
#             return render(req,"src/home/_base_structure.html",CONTEXT)
    



# @user/my-learning/
def goto_user_enrollments(req):
    if req.method != "GET":
        return send_bad_request()
    else:
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:
            return redirect('/user/my-learning/enrolled/')




# @user/my-learning/enrolled/
def user_enrollments(req):
    if req.method != "GET":
        return send_bad_request()
    else:
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:
            CONTEXT = {
                "tab_title": f"{req.user.first_name}'s Enrollments | Ed.Line",
                "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2],  
                "full_name": req.user.first_name + " " + req.user.last_name,
                "join_date": req.user.date_joined,

                "user_enrolled": get_all_user_enrollments(req.user.username,req.user.first_name),  
                "enrollments": 1
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)








# @user/my-learning/my-lists/
def user_lists(req):
    if req.method != "GET":
        return send_bad_request()
    else:
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:

            LIST_DATA_DICT = get_user_created_list_data(req.user.username, req.user.first_name)


            CONTEXT = {
                "tab_title": f"{req.user.first_name}'s Lists: My Learning | Ed.Line",
                "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2],  
                "full_name": req.user.first_name + " " + req.user.last_name,
                "join_date": req.user.date_joined,  

                "user_made_lists": LIST_DATA_DICT,
                "user_lists": 1
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)
        








# @user/my-learning/ongoing/
def user_ongoing(req):
    if req.method != "GET":
        return send_bad_request()
    else:
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:

            LIST_DATA_DICT = get_user_ongoing_courses(req.user.username, req.user.first_name)

            print("-------------------------------->",req.user.first_name," |", req.user.last_name)

            CONTEXT = {
                "tab_title": f"{req.user.first_name}'s Ongoing Courses | Ed.Line",
                "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2],  
                "full_name": req.user.first_name + " " + req.user.last_name,
                "join_date": req.user.date_joined,  

                "user_ongoing": LIST_DATA_DICT,
                "user_ongoing_tag": 1
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)
        









   

# @user/settings/
def user_settings(req):
    if req.method != "GET":
        return send_bad_request()
    else:
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:
            CONTEXT = {
                "fname": req.user.first_name,
                "tab_title": f"{req.user.first_name} {req.user.last_name} | Ed.Line",
                "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2], 
                "full_name": req.user.first_name + " " + req.user.last_name,
                "join_date": req.user.date_joined,   
                "settings": 1
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)






# =======================================================================
# =======================================================================

def send_bad_request(req):
    CONTEXT = {
            "tab_title": "Page unaccessible...",
            "bad_request": 1
        }
    return render(req,"src/error/error_page.html",CONTEXT)


def bad_route(req):
    CONTEXT = {
            "tab_title": "Page unaccessible...",
            "bad_route": 1
        }
    return render(req,"src/error/error_page.html",CONTEXT)










# =======================================================================
# =======================================================================




# @/careers/
def careers(req):
    return render(req,'src/others/others.html',{
        "tab_title": "Careers: Ed.Line",
        "company_data": careers_edline()
    })




# @/about-us/
def about_us(req):
    return render(req,'src/others/others.html',{
        "tab_title": "About Us: Ed.Line",
        "company_data": about_edline()
    })






# @/terms/
def terms(req):
    return render(req,'src/others/others.html',{
        "tab_title": "Terms: Ed.Line",
        "company_data": terms_edline()
    })




# @/privacy/
def privacy(req):
    return render(req,'src/others/others.html',{
        "tab_title": "Privacy: Ed.Line",
        "company_data": privacy_edline()
    })



