import json
from arabic_reshaper import reshape as re 
from bidi.algorithm import get_display as gd
from modules.utils import validate_datetime, is_duplicate_appointment, load_file,save_file,show_consultants_list, show_search_results

APPOINTMENTS_FILE= "data/appointments.json"
CONSULTANTS_FILE= "data/consultants.json"
       
                
def add_appointment(username):
    """This function helps the user add appointment data to the appointments.json file."""
    
    # Import consultants and appointments list.
    appointments = load_file(APPOINTMENTS_FILE)
    consultants = load_file(CONSULTANTS_FILE)
        
    # Show consultant data for selection.
    consultant_id = show_consultants_list(consultants)
              
    # Check date & time format    
    while True:
        date= input(gd(re(":تاریخ مشاوره(نمونه YYYY-MM-DD)"))).strip()
        time= input(gd(re(":ساعت مشاوره(نمونه hh:mm)"))).strip()
        client=input(gd(re(":نام بیمار")))
        if not validate_datetime(date,time):
            print(gd(re("فرمت تاریخ یا ساعت نادرست است. دوباره تلاش کنید!")))
        elif is_duplicate_appointment(appointments,consultant_id,date,time):
            print(gd(re("این نوبت قبلا رزرو شده است. دوباره تلاش کنید!")))
        else:
            break    
        
    # Create a new appointment.
    new_id= appointments[-1]["id"]+ 1 if appointments else 1
    new_appointment = {
        "id": new_id,
        "consultant_id": consultant_id,
        "date": date,
        "time": time,
        "client":client,
        "created_by" : username
    }
    
    # Saved new data in Json file.
    save_file(appointments,APPOINTMENTS_FILE,new_appointment)
    print(gd(re("وقت مشاوره با موفقیت ثبت شد!")))


def show_appointments():
    """This function shows appointments list to the users."""
       
    # Import appointments list.
    appointments= load_file(APPOINTMENTS_FILE)
        
    # import consultant name.
    consultants = load_file(CONSULTANTS_FILE)
             
    # Show appointments list.
    if not consultants:
        print(gd(re("هیچ نوبتی ثبت نشده است!")))
    else:
        sorted_appointments= sorted(appointments,key=lambda x: (x['date'], x['time']))
        print(gd(re("\n لیست وقت های مشاوره:")))
        show_search_results(sorted_appointments,consultants)


    
def search_appointments_by_consultant():
    """This function searches appointments list by consultant name."""
    
    c_name = input(gd(re(":نام مشاور را وارد کنید"))).strip()
    consultants = load_file(CONSULTANTS_FILE)
    appointments= load_file(APPOINTMENTS_FILE)

    # Find matched IDs.
    matched_ids = [c["id"] for c in consultants if c_name.lower() in c["name"].lower()]

    if not matched_ids:
        print(gd(re("مشاوری با این نام یافت نشد.")))
    else:
        # Find matched appointments
        results = [a for a in appointments if a["consultant_id"] in matched_ids]
        if not results:
            print(gd(re("هیچ نوبتی برای این مشاور ثبت نشده است.")))
        else:
            show_search_results(results,consultants)      
    
    
def search_appointments_by_date():
    """This function searches appointments list by date."""
    
    while True:
        date = input(gd(re(":تاریخ مد نظر (YYYY-MM-DD)"))).strip()
        if not validate_datetime(date,"1:00"):
            print(gd(re("فرمت تاریخ نادرست است. دوباره تلاش کنید!")))
        else:
            break    
    appointments = load_file(APPOINTMENTS_FILE)
    consultants = load_file(CONSULTANTS_FILE)
    
    # Find matched appointments
    results = [a for a in appointments if a["date"] == date]
    
    if not results:
        print(gd(re("نوبتی در این تاریخ ثبت نشده است!")))
    else:  
        # Show Final list.
        show_search_results(results,consultants)
    