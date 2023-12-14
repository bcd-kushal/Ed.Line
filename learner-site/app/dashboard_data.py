from .utils import get_all_user_enrollments

def get_quick_links(user_id:str="", user_fname:str=""):
    return [
        {
            "name": "Ongoing",
            "path": "/user/my-learning/ongoing/"
        },

        {
            "name": "All Courses",
            "path": "/home/courses/"
        },

        {
            "name": "Web Development",
            "path": "/home/courses/web-development/"
        },

        {
            "name": "Settings",
            "path": "/user/settings/"
        },
    ]







def slider_pics(user_id:str="", user_fname:str=""):
    return [
        {
            "title": "Skills for your future",
            "short": "Expand your potential with a course. Start learning!",
            "btn": "To Courses",
            "href": "/home/courses/",
            "banner": "https://images.pexels.com/photos/326503/pexels-photo-326503.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },

        {
            "title": "Software Dev",
            "short": "Coding the future tech needs those skills of the future.",
            "btn": "See Development",
            "href": "/home/courses/development/",
            "banner": "https://images.pexels.com/photos/1181298/pexels-photo-1181298.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        
        {
            "title": "Symphonious Beats",
            "short": "Practice the notes, hone those beats.",
            "btn": "Check Music",
            "href": "/home/courses/music/",
            "banner": "https://images.pexels.com/photos/2016810/pexels-photo-2016810.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        
        {
            "title": "World through Lens",
            "short": "What it takes to be a professional multimedia executive.",
            "btn": "Open Photography & Video",
            "href": "/home/courses/photography-and-video/",
            "banner": "https://images.pexels.com/photos/935791/pexels-photo-935791.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        
        {
            "title": "Steady and Constant",
            "short": "Consistency and monetum is the key. Continue your preparation.",
            "btn": "Go to your courses",
            "href": "/user/enrolled/",
            "banner": "https://images.pexels.com/photos/926390/pexels-photo-926390.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        
    ]








def get_top_pick(user_id:str="", user_fname:str=""):
    return {
            "title": "Our Top Pick",
            "data": {
                        "title":"Machine Learning A-Z: AI, Python + ChatGPT Bonus",
                        "thumbnail": "https://img-c.udemycdn.com/course/240x135/950390_270f_3.jpg",
                        "language": "ES",
                        "courseType": "DEVELOPMENT",
                        "rating": "4.5",
                        "total_ratings": "178K",
                        "educator_name": "Kyle Perkins",
                        "educator_pfp": "https://static.uacdn.net/thumbnail/user/default.png?q=75&auto=format%2Ccompress&w=256",
                        "footer_course_details": "82 lectures • 1 PDF"
                    }
        }




def get_start_learning(user_id:str="", user_fname:str=""):
    return {
        "title": f"Let's start learning, {user_fname}",
        "data": [
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
    }





def fetch_dashboard_ribbons(user_id:str="", user_fname:str=""):
    return [
        {
            "title": "Recommended Topics",
            "data": [
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
        },
        
        {
            "title": "Based on your preferences",
            "data": [
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
        },
        

        {
            "title": "Because you searched 'XYZ'",
            "data": [
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
        },

        {
            "title": "Because you searched 'XYZ'",
            "data": [
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
        },

        {
            "title": "Featured Courses in 'PQR'",
            "data": [
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
        },

        {
            "title": "Featured Courses in 'ABC'",
            "data": [
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
        },
    ]

