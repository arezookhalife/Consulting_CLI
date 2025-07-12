import json
from arabic_reshaper import reshape as re 
from bidi.algorithm import get_display as gd

CONSULTANTS_FILE= "data/consultants.json"

def load_consultants():
    """This function import/create consultants list."""
    
    try:
        with open(CONSULTANTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
      
        
def add_consultant():
    """This function helps the user add new consultant data to the consultants.json file."""
    
    # Insert consultant data by user.
    name= input(gd(re(":نام مشاور")))
    specialty= input(gd(re(":تخصص مشاور")))

    # Import/create consultants list.
    consultants = load_consultants()
    
    # Create a new consultant with a unique ID.
    new_id= consultants[-1]["id"]+ 1 if consultants else 1
    new_consultant = {
        "id": new_id,
        "name": name,
        "specialty": specialty
    }
    consultants.append(new_consultant)
    
    # Saved new data in Json file.
    with open(CONSULTANTS_FILE, "w", encoding= "utf-8") as f:
        json.dump(consultants,f,ensure_ascii=False,indent=2)
    print(gd(re("مشاور با موفقیت افزوده شد!")))


def show_consultants():
    """This function shows consultants list to the users."""
       
    # Import consultants list.
    consultants = load_consultants()
         
    # Show consultant list.
    if consultants==[]:
        print(gd(re("هیچ مشاوری ثبت نشده است!")))
    else:
        sorted_consultants= sorted(consultants,key=lambda x: x['name'])
        print(gd(re("\n لیست مشاوران:")))
        for c in sorted_consultants:
            print(gd(re(f"{c['id']} | {c['name']} |  تخصص: {c['specialty']}")))


     