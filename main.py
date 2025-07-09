import json
from arabic_reshaper import reshape as re 
from bidi.algorithm import get_display as gd
from datetime import datetime


def show_menu():
    """This function helps the user select a option from menu."""
    
    print(gd(re("\n ===== منوی اصلی ======")))
    print(gd(re("1.افزودن مشاور")))
    print(gd(re("2.افزودن وقت مشاوره")))
    print(gd(re("3.نمایش مشاوران")))
    print(gd(re("4.نمایش نوبت ها")))
    print(gd(re("5.خروج")))
    
    
def validate_datetime(date_str,time_str):
    """This function Check date & time format."""
    
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        datetime.strptime(time_str,"%H:%M")
        return True
    except ValueError:
        return False


def is_duplicate_appointment(appointments,consultant_id,date,time):
    """This function checks for appointment duplication.""" 
    
    for a in appointments:
        if a["consultant_id"] == int(consultant_id) and a["date"] == date and a["time"] == time:
            return True
            break   
        else:
            continue
        return False                 
    
        
def add_consultant():
    """This function helps the user add new consultant data to the consultants.json file."""
    
    # Insert consultant data by user.
    name= input(gd(re(":نام مشاور")))
    specialty= input(gd(re(":تخصص مشاور")))

    # Import/create consultants list.
    try:
        with open("consultants.json", "r", encoding="utf-8") as f:
            consultants = json.load(f)
    except FileNotFoundError:
        consultants = []

    # Create a new consultant with a unique ID.
    new_id= consultants[-1]["id"]+ 1 if consultants else 1
    new_consultant = {
        "id": new_id,
        "name": name,
        "specialty": specialty
    }
    consultants.append(new_consultant)
    
    # Saved new data in Json file.
    with open("consultants.json", "w", encoding= "utf-8") as f:
        json.dump(consultants,f,ensure_ascii=False,indent=2)
    print(gd(re("مشاور با موفقیت افزوده شد!")))


def add_appointment():
    """This function helps the user add appointment data to the appointments.json file."""
    
    # Import consultants and appointments list.
    try:
        with open("consultants.json", "r", encoding="utf-8") as f:
            consultants = json.load(f)
    except FileNotFoundError:
        consultants = []
    
    try:
        with open("appointments.json", "r", encoding= "utf-8") as g:
            appointments = json.load(g)
    except FileNotFoundError:
        appointments = []        
        
    # Show consultant data for select.
    if consultants==[]:
        print(gd(re("هیچ مشاوری برای ثبت نوبت وجود ندارد!")))
    else:
        consultant_id_list=[]
        for c in consultants:
            print(gd(re(f"{c['id']}.{c['name']}({c['specialty']})")))
            consultant_id_list.append(c['id'])

        # Insert appointment data by user.
        consultant_id= input(gd(re(":شماره مشاور را وارد کنید")))
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
                print(gd(re("این نوبت قبلا رزور شده است. دوباره تلاش کنید!")))
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
        with open("appointments.json", "w", encoding= "utf-8") as g:
            json.dump(appointments,g,ensure_ascii=False,indent=2)
        print(gd(re("وقت مشاوره با موفقیت ثبت شد!")))
    

def show_consultants():
    """This function shows consultants list to the users."""
       
    # Import consultants list.
    try:
        with open("consultants.json","r", encoding="utf-8")as f:
            consultants = json.load(f)
    except FileNotFoundError:
        consultants = []
         
    # Show consultant list.
    if consultants==[]:
        print(gd(re("هیچ مشاوری ثبت نشده است!")))
    else:
        sorted_consultants= sorted(consultants,key=lambda x: x['name'])
        print(gd(re("\n لیست مشاوران:")))
        for c in sorted_consultants:
            print(gd(re(f"{c['id']} | {c['name']} |  تخصص: {c['specialty']}")))
        

def show_appointments():
    """This function shows appointments list to the users."""
       
    # Import appointments list.
    try:
        with open("appointments.json","r", encoding="utf-8")as f:
            appointments= json.load(f)
    except FileNotFoundError:
        appointments = []
        
    # import consultant name.
    try:
        with open("consultants.json","r", encoding="utf-8")as g:
            consultants= json.load(g)
    except FileNotFoundError:
        consultants = []
        
    consultant_map= {c['id']:c['name'] for c in consultants}
     
    # Show appointments list.
    if consultants==[]:
        print(gd(re("هیچ نوبتی ثبت نشده است!")))
    else:
        sorted_appointments= sorted(appointments,key=lambda x: (x['date'], x['time']))
        print(gd(re("\n لیست وقت مشاوره:")))
        for a in sorted_appointments:
            name = consultant_map.get(a['consultant_id'],"مشاور ناشناس")
            print(gd(re(f"{name} | {a['date']} | {a['time']}")))

            
# menu selection loop.
while True:
    show_menu()
    choice= input(gd(re(":انتخاب شما")))       
    
    if choice == "1":
        add_consultant()
    elif choice == "2":
        add_appointment() 
    elif choice == "3":
        show_consultants()
    elif choice == "4":
        show_appointments()
    elif choice == "5":
       print(gd(re("خروج از برنامه...")))
       break
    else:
        print(gd(re("گزینه نامعتبر،دوباره تلاش کنید.")))

