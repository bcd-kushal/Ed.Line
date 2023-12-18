from django.shortcuts import render

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


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from datetime import datetime

from .forms import *
from .footer import *
from .utils import *
from .models import *



MOBILE = ""

ATLAS_URI = ""

FOOTER_LINKS = {
    "LINKS": footer_data(),
    "SOCIALS": footer_socials()
}

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
                "tab_title": "Ed.Teach - The Next Wave"
            }
            return render(req,"src/landing/landing2.html",CONTEXT)
        else:
            return redirect('home/')

    # -----------------------------------------------------------------
    else: 
        return send_bad_request(req)







# @/home/
def homepage(req):
    global FOOTER_LINKS

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
                "tab_title": "Home|Ed.Teach",
                "full_name": req.user.first_name + " " + req.user.last_name,
                "join_date": req.user.date_joined,
                "username": initials_of_name(req.user.first_name+" "+req.user.last_name)[0:2],    

                "footer": FOOTER_LINKS["LINKS"],
                "social": FOOTER_LINKS["SOCIALS"],

                "picform": ProfilePicForm(),

                "homepage": 1
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)












# ###############################################################################################################
        # ########## AUTH ROUTING ############################################################################### 
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
                "tab_title": "LogIn|Ed.Teach",
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
                "tab_title": "SignUp|Ed.Teach",
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









# ###############################################################################################################
        # ########## ADD COURSE,PFP ROUTING ############################################################################### 
# ###############################################################################################################

# @/add-pfp/
def user_pfp(req):
    print("\n----------------------------------> WE REACHED HERE\n")
    if req.method == "POST":
        pic_form = ProfilePicForm(req.POST,req.FILES)
        if pic_form.is_valid():
            profile_pic = pic_form.cleaned_data["picture"]
            mobile = req.user.username
            name = req.user.first_name + " " + req.user.last_name

            # this thig down below actually works
            print(f"\n\n\n===================> NAME: {name}")
            print(f"\n\n\n===================> MOBILE: {mobile}")
            print(f"\n\n\n===================> PIC: {profile_pic}")


            if educator_pictures.objects.filter(mobile=mobile).exists():
                user = educator_pictures.objects.filter(mobile=mobile).first()
                user.image = profile_pic
                user.save()
                print("................ SUCCESS IN UPDATING")
                
            else: 
                educator_pictures.objects.create(
                    mobile = mobile,
                    image = profile_pic,
                    name = name
                )
                print("................ SUCCESS IN ADDING")



            all_data = educator_pictures.objects.filter(mobile=mobile)
            print("___________",all_data)
            for x in all_data:
                print("\n\n:::",x.mobile)
                print("\n\n:::",x.name)
                print("\n\n:::",x.image)

            return redirect('/home/')
        



        else: 
            return redirect('/home/')
    else:
        return send_bad_request()















# @/add-course/
def add_course(req):
    print("\n----------------------------------> WE REACHED HERE\n")
    if req.method == "POST":    
        # this is where the educator posts their course content and it comes here

        # we cant use a set schema here so forms of django is redundant


        # the data, perhaps should be coming like this:
        # (( OVERVIEW TO COURSE ))
        # mobile
        # title
        # thumbnail
        # short desc
        # PK: 32-bit = <mobile><date><time_to_ms><random5>           --> FK
        # ...............//others as needed
        # 
        # 
        # (( MAJOR TOPICS ))
        # title
        # thumbnail
        # short desc
        # PK: 32-bit = <mobile><date><time_to_ms>MJ<id,3 digit>      --> FK
        # ...............//others as needed
        # 
        # 
        # (( MINOR TOPICS ))
        # title
        # video length
        # PK: 32-bit = <mobile><date><time_to_ms>MN<id,3 digit>      --> FK
        # ...............//others as needed
        # 
        # 
        # (( VIDEOS ))
        # PK which is also FK from minor topics
        # video
        # PK: 32-bit = <mobile><date><time_to_ms>MN<id,3 digit>      --> FK
        # ...............//others as needed





        # COURSE TABLE REQUIREMENTS
        course_title = req.POST.get("course_title")    # maxlength=100
        course_thumbnail = req.POST.get("course_thumbnail")
        course_description = req.POST.get("course_desc")
        course_level = req.POST.get("course_difficulty")
        course_prerequisite = req.POST.get("course_prerequisites")

        print("\n\n\n @@@@@@@@@@@@@@@@@@@@@@@")
        print(course_title, course_thumbnail, course_level,course_prerequisite, course_description)
        x,y=0,0

        """
        # MAJOR COURSE TITLE TABLE
            # the max major titles allowed would be 100
        for i in range(100):
            if req.POST.get(f"header{i+1}") :
                x+=1
                header = req.POST.get(f"header{i+1}")
                total_subcourses = req.POST.get(f"subcourses{i+1}")
                header_desc = req.POST.get(f"header_desc{i+1}")
                header_id = str(req.user.username) + "MAJOR" + instantaneous_time()



        
        # TOPICS TABLE
            # the max topics/major allowed would be 50
        for i in range(50):
            if req.POST.get(f"vid_title{i+1}") :
                y+=1
                vid_title = req.POST.get(f"vid_title{i+1}")
                vid_length = req.POST.get(f"vid_length{i+1}")
                vid_id = req.POST.get(f"vid_length{i+1}")
                header_id = str(req.user.username) + "MINOR" + instantaneous_time()


                video = req.POST.get(f"vid_video{i+1}")     # this goes to the VIDEO table DB
                vid_id = header_id


        DATA = {
            "course_title": course_title,
            "course_thumbnail": course_thumbnail,
            "course_desc": course_description,
            "course_level": course_level,
            "course_prerequisite": course_prerequisite,
        }

        for i in range(x):
            DATA[]

        print()
        """

        return redirect('/home/')
    


    else:
        return send_bad_request()













# ###############################################################################################################
        # ########## MISCELLANEOUS ROUTING ############################################################################### 
# ###############################################################################################################










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

