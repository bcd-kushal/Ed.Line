from datetime import datetime

def get_date_time_rn():
    now = datetime.now()
    # Format as "dd-mm-yyyy,hh:mm:ss"
    # return now.strftime("%d-%m-%Y,%H:%M:%S")
    return now.strftime("%d-%m-%Y")




def initials_of_name(name):
    words = name.split()
    initials = [word[0].upper() for word in words]
    result = ''.join(initials)

    return result




def format_change_title(str:str=""):
    arr = str.split('-')
    print(arr)
    for i in range(len(arr)):
        if arr[i]=="and":
            arr[i] = "&"
            continue
        if arr[i]=="it":
            arr[i] = "IT"
            continue
        arr[i] = arr[i].capitalize()
    
    print(arr)

    
    return '"' + " ".join(arr) + '"'





def format_date(d:str=""):
    month = d[0:3]
    
    date_time_obj = datetime.strptime(d, "%b. %d, %Y, %I:%M %p")

    print(date_time_obj)

    formatted_date = date_time_obj.strftime("%d %b %Y")
    formatted_date = formatted_date.replace(" 0", " ")  # Remove leading zero in day
    return formatted_date




def get_user_created_list_data(user_id:str="", user_fname:str=""):
    x = {
        "App Development": {
            "name": "App Development",
            "desc": "Kotlin or Flutter?? Meh..",
            "list_items": [
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
            ]
        },


        "JSP & JDBC": {
            "name": "JSP & JDBC",
            "desc": "For the Sem 5",
            "list_items": [
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
            ]
        },



        "Web Dev": {
            "name": "Web Dev",
            "desc": "For the love of it",
            "list_items": [
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
            ]
        },



        "ML/AI": {
            "name": "ML/AI",
            "desc": "For the heck of it",
            "list_items": [
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
            ]
        },

    }
    
    return x















def get_all_user_enrollments(user_id:str="", user_fname:str=""):
    x = [
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "Rajesh Verma"
                },
        ]
    
    return x







def get_user_ongoing_courses(user_id:str="", user_fname:str=""):
    x = [
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "DiscordJS"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "AnimeJS"
                },
                {
                    "name": "The Complete Android Q Developer Course",
                    "title": "YES"
                },
        ]
    
    return x