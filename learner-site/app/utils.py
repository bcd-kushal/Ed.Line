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