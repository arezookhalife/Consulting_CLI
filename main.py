from arabic_reshaper import reshape as re 
from bidi.algorithm import get_display as gd
from modules.consultants import add_consultant, show_consultants
from modules.appointments import add_appointment, show_appointments, search_appointments_by_consultant, search_appointments_by_date


def login():
    """This function returns the user's role to display the appropriate menu."""
    
    print(gd(re("\n ==ورود به سیستم==")))
    username = input(gd(re(":نام کاربری"))).strip()
    password = input(gd(re(":رمز عبور"))).strip()
    
    if username == "admin" and password == "admin123":
        return "admin"
    elif username == "user" and password == "user123":
        return "user"
    else:
        print(gd(re("اطلاعات نادرست!")))
        return login()


def show_menu(role):
    """This function helps the user select a option from menu."""
    
    print(gd(re("\n ===== منوی اصلی ======")))
    
    if role == "admin":
        print(gd(re("1.افزودن مشاور")))
        print(gd(re("2.افزودن وقت مشاوره")))
        print(gd(re("3.نمایش مشاوران")))
        print(gd(re("4.نمایش نوبت ها")))
        print(gd(re("5.جستجوی نوبت بر اساس نام مشاور")))
        print(gd(re("6.جستجوی نوبت بر اساس تاریخ")))    
        print(gd(re("7.خروج")))
    elif role =="user":
        print(gd(re("1.نمایش مشاوران")))
        print(gd(re("2.نمایش نوبت ها")))
        print(gd(re("3.جستجوی نوبت بر اساس نام مشاور")))
        print(gd(re("4.جستجوی نوبت بر اساس تاریخ")))    
        print(gd(re("5.خروج")))

if __name__ == "__main__": 
    role  = login()
    
    # menu selection loop.
    while True:
        show_menu(role)
        choice= input(gd(re(":انتخاب شما")))       
    
        if role == "admin":
            if choice == "1":
                add_consultant()
            elif choice == "2":
                add_appointment(role) 
            elif choice == "3":
                show_consultants()
            elif choice == "4":
                show_appointments()
            elif choice == "5":
                search_appointments_by_consultant()
            elif choice == "6":
                search_appointments_by_date()
            elif choice == "7": 
                print(gd(re("خروج از برنامه...")))
                break
            else:
                print(gd(re("گزینه نامعتبر،دوباره تلاش کنید.")))
        elif role == "user":
            if choice == "1":
                show_consultants()
            elif choice == "2":
                show_appointments()
            elif choice == "3":
                search_appointments_by_consultant()
            elif choice == "64":
                search_appointments_by_date()
            elif choice == "5": 
                print(gd(re("خروج از برنامه...")))
                break
            else:
                print(gd(re("گزینه نامعتبر،دوباره تلاش کنید.")))

