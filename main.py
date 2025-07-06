def add_consultant():
    """This function helps the user add new consultant data to the consultants.json file."""
    
    # Insert consultant data by user.
    name= input("نام مشاور:")
    specialty= input("تخصص مشاور:")

    # Import/create consultants list.
    import json
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
    import json
    with open("consultants.json", "r", encoding="utf-8") as f:
        consultants = json.load(f)
    
    # View consultant data for select.
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
    with open("appointments.json", "r", encoding= "utf-8") as f:
        appointments = json.load(f)
    appointments.append(new_appointment)
    with open("appointments.json", "w", encoding= "utf-8") as f:
        json.dump(appointments,f,ensure_ascii=False,indent=2)
    print("وقت مشاوره با موفقیت ثبت شد!")
    
    
add_consultant()  
add_appointment()  