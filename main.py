import json

def add_consultant():
    """This function helps the user add new consultant data to the consultants.json file."""
    
    # Insert consultant data by user.
    name= input("نام مشاور:")
    specialty= input("تخصص مشاور:")

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
    print("مشاور با موفقیت افزوده شد!")


def add_appointment():
    """This function helps the user add appointment data to the appointments.json file."""
    
    # Import consultants list.
    try:
        with open("consultants.json", "r", encoding="utf-8") as f:
            consultants = json.load(f)
    except FileNotFoundError:
        consultants = []
        
    # Show consultant data for select.
    if consultants==[]:
        print("هیچ مشاوری برای ثبت نوبت وجود ندارد!")
    else:
        consultant_id_list=[]
        for c in consultants:
            print(f"{c['id']}.{c['name']}({c['specialty']})")
            consultant_id_list.append(c['id'])

        # Insert appointment data by user.
        consultant_id= int(input("ID مشاور را وارد کنید:"))
        while int(consultant_id) not in consultant_id_list:
            print("کد وارد شده صحیح نمی باشد!")
            consultant_id= int(input("ID مشاور را وارد کنید:"))
        date= input("تاریخ مشاوره(نمونه 2025-06-30):")
        time= input("ساعت مشاوره(نمونه 14:00):")
        
        # Create a new appointment.
        new_appointment = {
            "consultant_id": consultant_id,
            "date": date,
            "time": time
        }
        
        # Saved new data in Json file.
        try:
            with open("appointments.json", "r", encoding= "utf-8") as f:
                appointments = json.load(f)
        except FileNotFoundError:
            appointments = []
                
        appointments.append(new_appointment)
        with open("appointments.json", "w", encoding= "utf-8") as f:
            json.dump(appointments,f,ensure_ascii=False,indent=2)
        print("وقت مشاوره با موفقیت ثبت شد!")
    

def consultants_list():
    """This function shows consultants list to the users."""
       
    # Import consultants list.
    try:
        with open("consultants.json","r", encoding="utf-8")as f:
            consultants = json.load(f)
    except FileNotFoundError:
        consultants = []
         
    # Show consultant list.
    if consultants==[]:
        print("هیچ مشاوری ثبت نشده است!")
    else:
        sorted_consultants= sorted(consultants,key=lambda x: x['name'])
        print("\n لیست مشاوران:")
        for c in sorted_consultants:
            print(f"{c['id']} | {c['name']} |  تخصص: {c['specialty']}")
        

def appointments_list():
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
        print("هیچ نوبتی ثبت نشده است!")
    else:
        sorted_appointments= sorted(appointments,key=lambda x: (x['date'], x['time']))
        print("\n لیست وقت مشاوره:")
        for a in sorted_appointments:
            name = consultant_map.get(a['consultant_id'],"مشاور ناشناس")
            print(f"{name} | {a['date']} | {a['time']}")
            

         
add_consultant()  
add_appointment()  
consultants_list()
appointments_list()