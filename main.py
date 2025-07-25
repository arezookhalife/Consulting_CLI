from arabic_reshaper import reshape as re 
from bidi.algorithm import get_display as gd
from modules.users import login, signup
from modules.consultants import add_consultant, show_consultants
from modules.appointments import add_appointment, show_appointments, search_appointments_by_consultant, search_appointments_by_date
from modules.utils import cls


def show_menu(role):
    """This function helps the user select a option from menu."""
      
    if role == "admin": 
        print(gd(re("\n ====== منوی اصلی ======")))
        print(gd(re("1.افزودن مشاور")))
        print(gd(re("2.افزودن وقت مشاوره")))
        print(gd(re("3.نمایش مشاوران")))
        print(gd(re("4.نمایش نوبت ها")))
        print(gd(re("5.جستجوی نوبت بر اساس نام مشاور")))
        print(gd(re("6.جستجوی نوبت بر اساس تاریخ")))    
        print(gd(re("7.خروج")))
    elif role =="user":
        print(gd(re("\n ====== منوی اصلی ======")))
        print(gd(re("1.نمایش مشاوران")))
        print(gd(re("2.نمایش نوبت ها")))
        print(gd(re("3.جستجوی نوبت بر اساس نام مشاور")))
        print(gd(re("4.جستجوی نوبت بر اساس تاریخ")))    
        print(gd(re("5.خروج")))
    
# START.
if __name__ == "__main__":
    count = 0
    cls()
    while True:
        print(gd(re("\n ====== به برنامه مشاوره خوش آمدید ======")))
        print(gd(re("1.ثبت نام")))
        print(gd(re("2.ورود")))
        selection= input(gd(re(":انتخاب شما")))
        if selection == "1":
            signup()    
        elif selection == "2":
            user  = login(count)
            role = user['role']
            username = user['username']
        
            # menu selection loop.
            while True:
                show_menu(role)
        
                if role == "admin":
                    choice= input(gd(re(":انتخاب شما")))       

                    if choice == "1":
                        add_consultant()
                    elif choice == "2":
                        add_appointment(username) 
                    elif choice == "3":
                        show_consultants()
                    elif choice == "4":
                        show_appointments()
                    elif choice == "5":
                        search_appointments_by_consultant()
                    elif choice == "6":
                        search_appointments_by_date()
                    elif choice == "7":
                        cls() 
                        print(gd(re("خروج از برنامه...")))
                        break
                            

                    else:
                        print(gd(re("گزینه نامعتبر،دوباره تلاش کنید.")))
                    
                elif role == "user":
                    choice= input(gd(re(":انتخاب شما")))       

                    if choice == "1":
                        show_consultants()
                    elif choice == "2":
                        show_appointments()
                    elif choice == "3":
                        search_appointments_by_consultant()
                    elif choice == "4":
                        search_appointments_by_date()
                    elif choice == "5": 
                        cls()
                        print(gd(re("خروج از برنامه...")))
                        break    
                    else:
                        print(gd(re("گزینه نامعتبر،دوباره تلاش کنید.")))
        else:
            cls()
            print(gd(re("گزینه نامعتبر،دوباره تلاش کنید.")))
            continue