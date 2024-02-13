from django.shortcuts import render

import time
import threading

from django.views.decorators.cache import cache_page
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
from moviepy.editor import VideoFileClip

from .forms import *
from .footer import *
from .utils import *
from .models import *
from .side_data import *
from .utils.generate_id import generate_id
from .utils.utils import initials_of_name, get_courses_of_educator, get_date_time_rn


MOBILE = ""

ATLAS_URI = ""

PIC_UPDATE_STATUS = False

FOOTER_LINKS = {
    "LINKS": footer_data(),
    "SOCIALS": footer_socials()
}


OVERVIEW_ID = ""
HEADER_ID = ""
VIDEO_ID = ""

def helper():
    global MOBILE
    time.sleep(1.5)
    MOBILE = ""

def helper_pfp():
    global PIC_UPDATE_STATUS
    time.sleep(2.5)
    PIC_UPDATE_STATUS = False


def helper_overview():
    global OVERVIEW_ID
    time.sleep(4)
    OVERVIEW_ID = ""


def helper_header():
    global HEADER_ID
    time.sleep(4)
    HEADER_ID = ""

    
def helper_video():
    global VIDEO_ID
    time.sleep(4)
    VIDEO_ID = ""

import beautifish.templates as bft
import subprocess
from django.conf import settings as sett

def check_vid_duration(vid):
    # get video file name 
    vid_name = vid.name

    # format file path just how django saves it up
    vid_name = vid_name.replace(" ","_")
    vid_name = vid_name.replace("'","")
    """ 
    vid_path = os.path.join(sett.MEDIA_ROOT,"media\\videos\\"+vid_name)
    t = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", vid_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    bft.success(vid_path)
    bft.warning(mode="spaced",msg=str(float(t.stdout))) """
    return 0


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
                "tab_title": "Ed.Teach - The Next Wave",
                
                "footer": FOOTER_LINKS["LINKS"],
                "social": FOOTER_LINKS["SOCIALS"],
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

                "homepage": 'home'
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
            return redirect('/')
        else:
            LogoutUser(req)
            return redirect('/login/')
        
    # elif req.method == "GET":
    #     if req.user.username == None or req.user.username == "":
    #         return redirect('/')
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
        # ########## EDUCATOR ROUTING ############################################################################### 
# ###############################################################################################################





















# ###############################################################################################################
        # ########## ADD COURSE,PFP ROUTING ############################################################################### 
# ###############################################################################################################

def redirect_to_course_overview(req):
    if req.method != "GET":
        return send_bad_request(req)
    else:
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:
            return redirect('/add-course-overview/')





# @educator/update-pfp/
def user_pfp(req):
    global PIC_UPDATE_STATUS

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


            PIC_UPDATE_STATUS = True
            thread2 = threading.Thread(target=helper_pfp)
            thread2.start()

            return redirect('/educator/update-pfp/')
        



        else: 
            return redirect('/home/')
    
    elif req.method=="GET":
        if req.user.username == None or req.user.username == "":
            return redirect('/')
        else:
            CONTEXT = {
                "tab_title": "Update profile picture|Ed.Teach",
                "footer": FOOTER_LINKS["LINKS"],
                "social": FOOTER_LINKS["SOCIALS"],
                "first_name": req.user.first_name.upper(),
                "picform": ProfilePicForm(),
                "update_status": PIC_UPDATE_STATUS,
                "homepage": "pfp-update"
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)
    
    
    else:
        return send_bad_request(req)














# @educator/<str:to_edit>/
def user_edit(req,to_edit):
    global PIC_UPDATE_STATUS
    print("``````````````````````````````",to_edit)
    to_edit = to_edit[7:]

    if req.method == "POST":

        if req.user.username == None or req.user.username == "":
            return redirect('/')
        else:

            new_data = req.POST.get("updated_data")
            print(new_data)

            educator = RegisteredUsers.objects.get(username=req.user.username)


            if to_edit == 'name':
                educator.first_name = new_data
            elif to_edit == 'email':
                educator.email = new_data
            elif to_edit == 'number':
                educator.username = new_data
            else:
                return bad_route(req)
        

            educator.save()


            PIC_UPDATE_STATUS = True
            thread3 = threading.Thread(target=helper_pfp)
            thread3.start()

            return redirect(f'/educator/update-{to_edit}/')
        

    elif req.method=="GET":
        if req.user.username == None or req.user.username == "":
            return redirect('/')
        else:
            CONTEXT = {
                "tab_title": "Update profile picture|Ed.Teach",
                "footer": FOOTER_LINKS["LINKS"],
                "social": FOOTER_LINKS["SOCIALS"],
                "first_name": req.user.first_name.upper(),
                "update_status": PIC_UPDATE_STATUS,
                "to_edit": to_edit.upper(),
                "to_edit2": to_edit,
                "homepage": f"{to_edit}-edit"
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)
    
    
    else:
        return send_bad_request(req)





















# @/add-course-overview/
def add_course_overview(req):
    global OVERVIEW_ID
    print("\n----------------------------------> REACHED: CREATE NEW COURSE PAGE\n")
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
        course_id=generate_id()
        OVERVIEW_ID = course_id
        course_title = req.POST.get("course_title") or "Empty title"    # maxlength=100
        course_thumbnail = req.FILES["course_thumbnail"]
        course_description = req.POST.get("course_desc") or "Description not provided"
        course_level = req.POST.getlist("course_level")
        course_prerequisite = req.POST.get("course_prerequisites") or "none"



        print(f"{course_title}, {course_thumbnail}, {course_level}, {course_prerequisite}, {course_description}, {course_id}")


        # add data to model db and redirect to course details
        overview_instance = CourseOverview(course_title=course_title, course_thumbnail=course_thumbnail, course_description=course_description, course_level=course_level, course_id=course_id)
        overview_instance.save()
        
        thread = threading.Thread(target=helper_overview)
        thread.start()

        return redirect('/add-course-data/')
   

    elif req.method == "GET":
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:
            # first fetch the overview details that queried this...

            # send the overview details to template in a hidden form
            CONTEXT = {
                "tab_title": "Course Details|Ed.Teach",
                "footer": FOOTER_LINKS["LINKS"],
                "social": FOOTER_LINKS["SOCIALS"],
                "homepage": 'add-course',
                "overview_id": ""
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)

    else:
        return send_bad_request(req)





# @/add-course-data/
def add_course_data(req):
    if req.method=="POST":
        if not (req.POST.get("overview_id") and req.POST.get("overview_id")!=""):
            return send_bad_request(req)
        else:

            overview_id = req.POST.get("overview_id")
            if not (CourseOverview.objects.filter(course_id=overview_id).exists()):
                return send_bad_request(req)
            else:

                # get all form data 
                section_title = req.POST.get("header_title")
                section_desc = req.POST.get("header_desc") or ""
                


                videos = [
                    {
                        "name": req.POST.get("video_name_1") or "",
                        "video": req.FILES.get("video1") if req.FILES.get("video1")!=None else "",
                        "duration": -1 if req.FILES.get("video1")==None else 35
                    },
                    {
                        "name": req.POST.get("video_name_2") or "",
                        "video": req.FILES["video2"] if req.FILES.get("video2")!=None else "",
                        "duration": -1 if req.FILES.get("video1")==None else 35
                    },
                    {
                        "name": req.POST.get("video_name_3") or "",
                        "video": req.FILES["video3"] if req.FILES.get("video3")!=None else "",
                        "duration": -1 if req.FILES.get("video1")==None else 35
                    },
                    {
                        "name": req.POST.get("video_name_4") or "",
                        "video": req.FILES["video4"] if req.FILES.get("video4")!=None else "",
                        "duration": -1 if req.FILES.get("video1")==None else 35
                    },
                    {
                        "name": req.POST.get("video_name_5") or "",
                        "video": req.FILES["video5"] if req.FILES.get("video5")!=None else "",
                        "duration": -1 if req.FILES.get("video1")==None else 35
                    },
                    {
                        "name": req.POST.get("video_name_6") or "",
                        "video": req.FILES["video6"] if req.FILES.get("video6")!=None else "",
                        "duration": -1 if req.FILES.get("video1")==None else 35
                    },
                    {
                        "name": req.POST.get("video_name_7") or "",
                        "video": req.FILES["video7"] if req.FILES.get("video7")!=None else "",
                        "duration": -1 if req.FILES.get("video1")==None else 35
                    },
                    {
                        "name": req.POST.get("video_name_8") or "",
                        "video": req.FILES["video8"] if req.FILES.get("video8")!=None else "",
                        "duration": -1 if req.FILES.get("video1")==None else 35
                    },
                ]

                submit_type = req.POST.get("submit-action")

                videos = [ video for video in videos if video["video"]!="" ]

                print(f"INVOKED: {submit_type}")
                print(f"\nTITLE = {section_title}\nDESC = {section_desc}")
                print(f"TOTAL VIDEOS GIVEN: {len(videos)}")
                print(f"VIDEOS ARE: {videos}")

                header_id = "head-" + generate_id()
                
                overview_instance = CourseOverview.objects.get(course_id=overview_id)

                # ADD HEADER...
                header_instance = HeaderTitles(overview_id=overview_instance,header=section_title,total_subcourses=len(videos),header_desc=section_desc,header_id=header_id)
                header_instance.save()
                print("ADDED HEADER", header_id)

                header_instance = HeaderTitles.objects.get(header_id=header_id)

                # after getting all valid data... first add it to the database --------------------------------

                count = 1
                for video in videos:
                    video_id = f"vid{count}-" + header_id

                    # ADD VIDEO TITLE...
                    vid_title_instance = VideoTitles(header_id=header_instance,overview_id=overview_instance,vid_title=video["name"],vid_length=video["duration"],vid_id=video_id)
                    vid_title_instance.save()
                    print(f"ADDED VIDEO TITLE {count}")

                    # ADD VIDEO...
                    video_title_instance = VideoTitles.objects.get(vid_id=video_id)
                    vid_instance = Videos(overview_id=overview_instance,vid_id=video_title_instance,video=video["video"])
                    vid_instance.save()
                    print(f"ADDED VIDEO {count}")
                    count+=1
                
            
                # then check for what submit button was clicked and navigate as required...
                if(submit_type=="add-more-header"):
                    CONTEXT = {
                        "tab_title": "Course Details|Ed.Teach",
                        "footer": FOOTER_LINKS["LINKS"],
                        "social": FOOTER_LINKS["SOCIALS"],
                        "homepage": 'course-details',
                        "overview_id": overview_id,
                        "overview_title": ""
                    }
                    return render(req,"src/home/_base_structure.html",CONTEXT)

                if(submit_type=="save-all"):
                    # since the records are already saved so just go to homepage
                    return redirect("/home/")
                
                
            

    
    elif req.method=="GET":
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:
            global OVERVIEW_ID
            overview_id = OVERVIEW_ID

            if overview_id=="":
                return send_bad_request(req)
            if not CourseOverview.objects.filter(course_id=overview_id).exists():
                return send_bad_request(req)

            overview_title = ""
            data = ""
            try:
                data = CourseOverview.objects.get(course_id=overview_id)
            except CourseOverview.DoesNotExist:
                return send_bad_request(req)
            
            overview_title = data.course_title
            overview_thumbnail = data.course_thumbnail

            CONTEXT = {
                "tab_title": "Course Details|Ed.Teach",
                "footer": FOOTER_LINKS["LINKS"],
                "social": FOOTER_LINKS["SOCIALS"],
                "homepage": 'course-details',
                "overview_id": overview_id,
                "overview_title": overview_title
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)
    
    else: 
        return send_bad_request(req)








# ###############################################################################################################
        # ########## MISCELLANEOUS ROUTING ############################################################################### 
# ###############################################################################################################

# @/educator/courses/
def educator_courses(req):
    if req.method != "GET":
        return send_bad_request(req)
    else:
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:
            CONTEXT = {
                "tab_title": "Courses|Ed.Teach",
                "footer": FOOTER_LINKS["LINKS"],
                "social": FOOTER_LINKS["SOCIALS"],
                "homepage": 'courses',
                "educator_name": req.user.username.capitalize()
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)
        

        




# @/educator/profile/
def educator_profile(req):
    if req.method != "GET":
        return send_bad_request(req)
    else:
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:
            CONTEXT = {
                "tab_title": "Profile|Ed.Teach",
                "join_date": req.user.date_joined,
                "full_name": req.user.first_name + " " + req.user.last_name,
                "footer": FOOTER_LINKS["LINKS"],
                "social": FOOTER_LINKS["SOCIALS"],
                "educator_courses": get_courses_of_educator(req.user.username,req.user.first_name),
                "homepage": 'profile'
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)



# @/educator/settings/
@cache_page(60 * 15)        
def educator_settings(req):
    if req.method != "GET":
        return send_bad_request(req)
    else:
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:
            CONTEXT = {
                "tab_title": "Settings|Ed.Teach",
                "footer": FOOTER_LINKS["LINKS"],
                "social": FOOTER_LINKS["SOCIALS"],
                "full_name": req.user.first_name + " " + req.user.last_name,
                "number": req.user.username,
                "email": req.user.email,
                "homepage": 'settings'
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)



# @/course/analytics/
def course_analytics(req):
    if req.method != "GET":
        return send_bad_request(req)
    else:
        if req.user.username == "" or req.user.username == None:
            return redirect('/')
        else:
            CONTEXT = {
                "tab_title": "Analytics|Ed.Teach",
                "footer": FOOTER_LINKS["LINKS"],
                "social": FOOTER_LINKS["SOCIALS"],
                "homepage": 'analytics'
            }
            return render(req,"src/home/_base_structure.html",CONTEXT)








# =======================================================================
# =======================================================================

def send_bad_request(req):
    CONTEXT = {
                "tab_title": "404 Bad Request Type...",
                "footer": FOOTER_LINKS["LINKS"],
                "social": FOOTER_LINKS["SOCIALS"],
                "homepage": 'error',
                "bad_request": 1
            }
    return render(req,"src/home/_base_structure.html",CONTEXT)


def bad_route(req):
    CONTEXT = {
                "tab_title": "Page unaccessible...",
                "footer": FOOTER_LINKS["LINKS"],
                "social": FOOTER_LINKS["SOCIALS"],
                "homepage": 'error',
                "bad_route": 1
            }
    return render(req,"src/home/_base_structure.html",CONTEXT)






# =======================================================================
# ====================== [ OTHERS ] =====================================
# =======================================================================


# -------------------------------------> 1

# @/about-us/
def about_us(req):
    CONTEXT = {
        "tab_title": "Ed.Teach & Ed.Line - Your right, Our website",
        "company_data": about_edline(),
        "footer": FOOTER_LINKS["LINKS"],
        "social": FOOTER_LINKS["SOCIALS"],

        "other": "about-us"
    }

    return render(req,'src/others/_base.html',CONTEXT)




# -------------------------------------> 2

# @/careers/
def careers(req):
    CONTEXT = {
        "tab_title": "Careers | Ed.Teach, Ed.Line",
        "company_data": careers_edline(),
        "footer": FOOTER_LINKS["LINKS"],
        "social": FOOTER_LINKS["SOCIALS"],

        "careers": get_current_job_openings(),
        "other": "careers"
    }
    
    return render(req,'src/others/_base.html',CONTEXT)




# -------------------------------------> 3

# @/history/
def history(req):
    CONTEXT = {
        "tab_title": "History | Ed.Teach, Ed.Line",
        "company_data": careers_edline(),
        "footer": FOOTER_LINKS["LINKS"],
        "social": FOOTER_LINKS["SOCIALS"],

        "history": get_company_history(),

        "other": "history"
    }
    
    return render(req,'src/others/_base.html',CONTEXT)
    
    




# -------------------------------------> 4

# @/gallery/
def gallery(req):
    CONTEXT = {
        "tab_title": "Gallery | Ed.Teach, Ed.Line",
        "company_data": privacy_edline(),
        "footer": FOOTER_LINKS["LINKS"],
        "social": FOOTER_LINKS["SOCIALS"],

        "other": "gallery"
    }
    return render(req,'src/others/_base.html',CONTEXT)






# -------------------------------------> 5

# @/blogs/
def blogs(req):
    CONTEXT = {
        "tab_title": "Blogs | Ed.Teach, Ed.Line",
        "company_data": privacy_edline(),
        "footer": FOOTER_LINKS["LINKS"],
        "social": FOOTER_LINKS["SOCIALS"],

        "other": "blogs"
    }
    return render(req,'src/others/_base.html',CONTEXT)







# -------------------------------------> 6

# @/contact-us/
def contact_us(req):
    CONTEXT = {
        "tab_title": "Contact Us | Ed.Teach, Ed.Line",
        "company_data": privacy_edline(),
        "footer": FOOTER_LINKS["LINKS"],
        "social": FOOTER_LINKS["SOCIALS"],

        "other": "contact-us"
    }
    return render(req,'src/others/_base.html',CONTEXT)
    





# -------------------------------------> 7

# @/privacy/
def privacy(req):
    CONTEXT = {
        "tab_title": "Privacy | Ed.Teach, Ed.Line",
        "company_data": privacy_edline(),
        "footer": FOOTER_LINKS["LINKS"],
        "social": FOOTER_LINKS["SOCIALS"],

        "other": "privacy"
    }
    return render(req,'src/others/_base.html',CONTEXT)






# -------------------------------------> 8

# @/terms/
def terms(req):
    CONTEXT = {
        "tab_title": "Terms | Ed.Teach, Ed.Line",
        "company_data": terms_edline(),
        "footer": FOOTER_LINKS["LINKS"],
        "social": FOOTER_LINKS["SOCIALS"],

        "other": "terms"
    }
    return render(req,'src/others/_base.html',CONTEXT)







# -------------------------------------> 9

# @/testimonials/
def testimonials(req):
    CONTEXT = {
        "tab_title": "Testimonials | Ed.Teach, Ed.Line",
        "company_data": privacy_edline(),
        "footer": FOOTER_LINKS["LINKS"],
        "social": FOOTER_LINKS["SOCIALS"],

        "other": "testimonials"
    }
    return render(req,'src/others/_base.html',CONTEXT)











# -------------------------------------> 10

# @/reviews/
def reviews(req):
    CONTEXT = {
        "tab_title": "Our reviews | Ed.Teach, Ed.Line",
        "company_data": privacy_edline(),
        "footer": FOOTER_LINKS["LINKS"],
        "social": FOOTER_LINKS["SOCIALS"],

        "reviews": get_user_reviews(),

        "other": "reviews"
    }
    return render(req,'src/others/_base.html',CONTEXT)






# -------------------------------------> 11

# @/collaborate/
def collaborate(req):
    if req.method == "POST":
        name = req.POST.get("company_name")
        email = req.POST.get("company_email")
        brief = req.POST.get("company_msg")


        print(f"\n\nNAME: {name}\nEMAIL: {email}\nDESC: {brief}\n\n")


        pass

    elif req.method == "GET":
        CONTEXT = {
            "tab_title": "Collaboarte with us | Ed.Teach, Ed.Line",
            "company_data": privacy_edline(),
            "footer": FOOTER_LINKS["LINKS"],
            "social": FOOTER_LINKS["SOCIALS"],

            "other": "collaborate"
        }
        return render(req,'src/others/_base.html',CONTEXT)



    else:
        return send_bad_request(req)


    









# -------------------------------------
# -------------------------------------
# -------------------------------------
# -------------------------------------








# @/user-reviews/
# @/user-review/
# @/user_reviews/
# @/user_review/
# @/review/
def goto_reviews(req):
    return redirect('/reviews/')
