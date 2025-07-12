from arabic_reshaper import reshape as re 
from bidi.algorithm import get_display as gd
from modules.consultants import add_consultant, show_consultants
from modules.appointments import add_appointment, show_appointments, search_appointments_by_consultant, search_appointments_by_date


def show_menu():
    """This function helps the user select a option from menu."""
    
    print(gd(re("\n ===== منوی اصلی ======")))
    print(gd(re("1.افزودن مشاور")))
    print(gd(re("2.افزودن وقت مشاوره")))
    print(gd(re("3.نمایش مشاوران")))
    print(gd(re("4.نمایش نوبت ها")))
    print(gd(re("5.جستجوی نوبت بر اساس نام مشاور")))
    print(gd(re("6.جستجوی نوبت بر اساس تاریخ")))    
    print(gd(re("7.خروج")))
   
            
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
       search_appointments_by_consultant()
    elif choice == "6":
        search_appointments_by_date()
    elif choice == "7": 
       print(gd(re("خروج از برنامه...")))
       break
    else:
        print(gd(re("گزینه نامعتبر،دوباره تلاش کنید.")))

