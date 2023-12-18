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