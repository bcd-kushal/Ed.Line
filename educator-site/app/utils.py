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




def instantaneous_time():
    now = datetime.now()
    return now.strftime("%d%m%Y%H%M%S%f")






def get_courses_of_educator(user_id:str="", user_fname:str=""):
    return [
                    {
                        "title":"NextJS: The Complete Guide",
                        "thumbnail": "https://img-b.udemycdn.com/course/240x135/3873464_403c_3.jpg",
                        "language": "EN",
                        "courseType": "DEVELOPMENT",
                        "last_lesson": "Folder Routing",
                        "progress": "0.56",
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
    ]