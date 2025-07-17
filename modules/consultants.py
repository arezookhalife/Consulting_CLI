import json
from arabic_reshaper import reshape as re 
from bidi.algorithm import get_display as gd
from modules.utils import load_file,save_file

CONSULTANTS_FILE= "data/consultants.json"
     
        
def add_consultant():
    """This function helps the user add new consultant data to the consultants.json file."""
    
    # Insert consultant data by user.
    name= input(gd(re(":نام مشاور"))).strip()
    specialty= input(gd(re(":تخصص مشاور"))).strip()

    # Import/create consultants list.
    consultants = load_file(CONSULTANTS_FILE)
    
    # Create a new consultant with a unique ID.
    new_id= consultants[-1]["id"]+ 1 if consultants else 1
    new_consultant = {
        "id": new_id,
        "name": name,
        "specialty": specialty
    }
    
    # Save new data in Json file.
    save_file(consultants,CONSULTANTS_FILE,new_consultant)
    print(gd(re("مشاور با موفقیت افزوده شد!")))


def show_consultants():
    """This function shows consultants list to the users."""
       
    # Import consultants list.
    consultants = load_file(CONSULTANTS_FILE)
         
    # Show consultant list.
    if consultants==[]:
        print(gd(re("هیچ مشاوری ثبت نشده است!")))
    else:
        sorted_consultants= sorted(consultants,key=lambda x: x['name'])
        print(gd(re("\n لیست مشاوران:")))
        for c in sorted_consultants:
            print(gd(re(f"{c['id']} | {c['name']} |  تخصص: {c['specialty']}")))


     