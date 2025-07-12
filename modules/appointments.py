import json
from arabic_reshaper import reshape as re 
from bidi.algorithm import get_display as gd
from modules.utils import validate_datetime, is_duplicate_appointment
from modules.consultants import load_consultants

APPOINTMENTS_FILE= "data/appointments.json"
CONSULTANTS_FILE= "data/consultants.json"

def load_appointments():
    try:
        with open(APPOINTMENTS_FILE, "r", encoding= "utf-8") as g:
            return json.load(g)
    except FileNotFoundError:
        return []  
        
        
def add_appointment():
    """This function helps the user add appointment data to the appointments.json file."""
    
    # Import consultants and appointments list.
    consultants = load_consultants()
    appointments = load_appointments()
        
    # Show consultant data for select.
    if consultants==[]:
        print(gd(re("هیچ مشاوری برای ثبت نوبت وجود ندارد!")))
    else:
        consultant_id_list=[]
        for c in consultants:
            print(gd(re(f"{c['id']}.{c['name']}({c['specialty']})")))
            consultant_id_list.append(c['id'])

        # Insert appointment data by user.
        consultant_id= int(input(gd(re(":شماره مشاور را وارد کنید"))))
        while int(consultant_id) not in consultant_id_list:
            print(gd(re("کد وارد شده صحیح نمی باشد!")))
            consultant_id= int(input(gd(re(":شماره مشاور را وارد کنید"))))
                   
        # Check date & time format    
        while True:
            date= input(gd(re(":تاریخ مشاوره(نمونه YYYY-MM-DD)")))
            time= input(gd(re(":ساعت مشاوره(نمونه hh:mm)")))
            if not validate_datetime(date,time):
                print(gd(re("فرمت تاریخ یا ساعت نادرست است. دوباره تلاش کنید!")))
            elif is_duplicate_appointment(appointments,consultant_id,date,time):
                print(gd(re("این نوبت قبلا رزرو شده است. دوباره تلاش کنید!")))
            else:
                break    
          
        # Create a new appointment.
        new_appointment = {
            "consultant_id": consultant_id,
            "date": date,
            "time": time
        }
        
        # Saved new data in Json file.
        appointments.append(new_appointment)
        with open(APPOINTMENTS_FILE, "w", encoding= "utf-8") as g:
            json.dump(appointments,g,ensure_ascii=False,indent=2)
        print(gd(re("وقت مشاوره با موفقیت ثبت شد!")))
    

def show_appointments():
    """This function shows appointments list to the users."""
       
    # Import appointments list.
    appointments= load_appointments()
        
    # import consultant name.
    consultants = load_consultants()
        
    consultant_map= {c['id']:c['name'] for c in consultants}
     
    # Show appointments list.
    if consultants==[]:
        print(gd(re("هیچ نوبتی ثبت نشده است!")))
    else:
        sorted_appointments= sorted(appointments,key=lambda x: (x['date'], x['time']))
        print(gd(re("\n لیست وقت های مشاوره:")))
        for a in sorted_appointments:
            name = consultant_map.get(a['consultant_id'],"مشاور ناشناس")
            print(gd(re(f"{name} | {a['date']} | {a['time']}")))


def search_appointments_by_consultant():
    """This function searches appointments list by consultant name."""
    
    c_name = input(gd(re(":نام مشاور را وارد کنید")))
    consultants = load_consultants()
    appointments= load_appointments()

    # Find matched IDs  .
    matched_ids = [c["id"] for c in consultants if c_name.lower() in c["name"].lower()]
    consultant_map= {c['id']:c['name'] for c in consultants}

    if matched_ids == []:
        print(gd(re("مشاوری با این نام یافت نشد.")))
    else:
        # Find matched appointments
        results = [a for a in appointments if a["consultant_id"] in matched_ids]
        if not results:
            print(gd(re("هیچ نوبتی برای این مشاور ثبت نشده است.")))
        else:
            # Show Final list.
            for a in results:
                name = consultant_map.get(a['consultant_id'],"مشاور ناشناس")
                print(gd(re(f"مشاور: {name} | تاریخ: {a['date']} | ساعت: {a['time']}")))  
    
    
def search_appointments_by_date():
    """This function searches appointments list by date."""
    
    date = input(gd(re(":تاریخ مد نظر (YYYY-MM-DD)"))).strip()
    appointments = load_appointments()
    consultants = load_consultants()
    
    # Find matched appointments
    consultant_map= {c['id']:c['name'] for c in consultants}
    results = [a for a in appointments if a["date"] == date]
    
    if not results:
        print(gd(re("نوبتی در این تاریخ ثبت نشده است!")))
      
    # Show Final list.
    for a in results:
        name = consultant_map.get(a['consultant_id'],"مشاور ناشناس")
        print(gd(re(f"مشاور: {name} | تاریخ: {a['date']} | ساعت: {a['time']}")))  
    