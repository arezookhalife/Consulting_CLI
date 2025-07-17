import json
from arabic_reshaper import reshape as re 
from bidi.algorithm import get_display as gd
from modules.utils import cls, load_file


USERS_FILE= "data/users.json"


def signup():
    """This function gets information for new users."""
    # Import users and appointments list.
    users = load_file(USERS_FILE)

    # Insert data by user.
    print(gd(re("\n ==ثبت نام==")))
    username = input(gd(re(":نام کاربری"))).strip()
    password = input(gd(re(":رمز عبور"))).strip()

    user_list = [c['username'] for c in users]
    pass_list = [c['password'] for c in users]
    
    # Check data.    
    if username in user_list or password in pass_list:
        print(gd(re(". مجددا تلاش کنید!نام کاربری یا کلمه عبور تکراری است")))
        return signup()  
       
    # Create a new appointment.
    else:
        new_id= users[-1]["id"]+ 1 if users else 1
        new_user = {
            "id": new_id,
            "username": username,
            "password": password,
            "role": "user"
        }
        
        # Saved new data in Json file.
        users.append(new_user)
        with open(USERS_FILE, "w", encoding= "utf-8") as g:
            json.dump(users,g,ensure_ascii=False,indent=2)
        cls()
        print(gd(re("ثبت نام شما با موفقیت انجام شد")))
   
   
def login(count):
    """This function returns the user's role to display the appropriate menu."""
    
    print(gd(re("\n ==ورود به سیستم==")))
    username = input(gd(re(":نام کاربری"))).strip()
    password = input(gd(re(":رمز عبور"))).strip()
    users= load_file(USERS_FILE)
    
    user= [a for a in users if a['username'] == username and a['password'] == password]

    if not user:
        count = count + 1
        if count < 4:
            print(gd(re("نام کاربری یا کلمه عبور اشتباه وارد شده است! \n لطفا مجددا تلاش کنید!")))  
            return login(count)
        else:
            print(gd(re("نام کاربری یا کلمه عبور بیش از سه بار اشتباه وارد شده است! \n لطفا بعدا تلاش کنید!")))
            EncodingWarning  
    else:
        for a in user:
            return a
