import json
from django.core.cache import cache
from .models import *

def read_educator_courses(educator_name):
    DATA,TEMP = [],{}
    overviews = CourseOverview.objects.filter(username=educator_name)
    
    # iterate over all overviews if they exist
    if overviews:
        print(overviews,"...",len(overviews))
        for overview in overviews:

            # TEMP stores entire course...
            TEMP = {}
            TEMP["course_name"] = overview.course_title
            TEMP["course_desc"] = overview.course_description
            TEMP["data"] = []
            OVERVIEW_INSTANCE = overview.course_id

            print({"course_name":overview.course_title,"course_desc":overview.course_description})

            # get the corresponding Headers
            headers = HeaderTitles.objects.filter(overview_id=OVERVIEW_INSTANCE)
            for header in headers:
                HEADER_INSTANCE = header.header_id
                videoTitles = VideoTitles.objects.filter(header_id=HEADER_INSTANCE)
                VIDEOS = []
                for videoTitle in videoTitles:
                    VIDEOS.append({ "title": videoTitle.vid_title, "length": videoTitle.vid_length })
                
                TEMP["data"].append({
                    "title": header.header,
                    "desc": header.header_desc,
                    "videos": VIDEOS
                })

            DATA.append(TEMP)

    return DATA