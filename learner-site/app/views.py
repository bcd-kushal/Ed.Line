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

from .utils import get_date_time_rn, initials_of_name

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
            CONTEXT = {
                "tab_title": "Home|Ed.Line",
                "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2],    
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
                "tab_title": "Courses|Ed.Line",
                "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2],    
                "courses": 1
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
            lname = form.cleaned_data["lname"]
            email = form.cleaned_data["email"]
            pass1 = form.cleaned_data["pass1"]
            # TIME_RN = get_date_time_rn()

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
            return redirect('/user/profile')
            
            

# @user/profile/
def show_user_profile(req):
    if req.method == "GET":
        if req.user.username == None or req.user.username == "":
            return redirect('/')
        else:
            CONTEXT = {
                "fname": req.user.first_name,
                "tab_title": f"{req.user.first_name} {req.user.last_name}|Ed.Line",
                "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2],    
                "user_profile": 1
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)
    


# @user/enrollments/
def user_enrollments(req):
    if req.method != "GET":
        return send_bad_request()
    else:
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:
            CONTEXT = {
                "tab_title": "Enrollments|Ed.Line",
                "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2],    
                "enrollments": 1
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
                "tab_title": "Settings|Ed.Line",
                "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2],    
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
