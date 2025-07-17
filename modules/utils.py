import json
import os
from datetime import datetime
from arabic_reshaper import reshape as re 
from bidi.algorithm import get_display as gd

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
        if a["consultant_id"] == consultant_id and a["date"] == date and a["time"] == time:
            return True
 
        else:
            return False                 
    

def load_file(file):
    """This function import/create list."""

    try:
        with open(file, "r", encoding= "utf-8") as g:
            return json.load(g)
    except FileNotFoundError:
        return [] 


def save_file(list,file,new_data):
    list.append(new_data)
    with open(file, "w", encoding= "utf-8") as g:
        json.dump(list,g,ensure_ascii=False,indent=2)
   
            
def show_consultants_list(list):
    
    if not list:
        print(gd(re("هیچ مشاوری برای ثبت نوبت وجود ندارد!")))
    else:
        consultant_id_list=[]
        for c in list:
            print(gd(re(f"{c['id']}.{c['name']}({c['specialty']})")))
            consultant_id_list.append(c['id'])    
        # Insert appointment data by user.    
        while True:
            consultant_id= int(input(gd(re(":شماره مشاور را وارد کنید"))))
            if int(consultant_id) not in consultant_id_list:
                print(gd(re("کد وارد شده صحیح نمی باشد!")))
            else:
                return consultant_id
 
 
def show_search_results(results,list):
    """This function shows searche results."""

    consultant_map= {c['id']:c['name'] for c in list}

    for a in results:
        name = consultant_map.get(a['consultant_id'],"مشاور ناشناس")
        print(gd(re(f"مشاور: {name} | تاریخ: {a['date']} | ساعت: {a['time']} | بیمار: {a['client']}")))
  
                         
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')       