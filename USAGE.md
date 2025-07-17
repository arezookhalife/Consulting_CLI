# USAGE - Consulting Appointment CLI System

----------------------------------------
## How to Run the Project
----------------------------------------
1. Make sure Python 3.8+ is installed on your system.
2. (Recommended) Create and activate a virtual environment:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the project:
```bash
python main.py
```
----------------------------------------
## Welcome Menu (Login / Register)
----------------------------------------
When the program starts, you will see the following options:

====== به برنامه مشاوره خوش آمدید ======
1. ثبت نام
2. ورود

If you choose **ثبت‌نام**, you can create a new user account by providing:

- نام کاربری
- رمز عبور

**Note**: After successful registration, your information will be saved as a **user role** in the *data/users.json* file, and you can log in using the same credentials.

If you choose **ورود**, you will be asked to enter:

- نام کاربری
- رمز عبور

----------------------------------------
## Choosing a Role (Login Info)
----------------------------------------
After logging in, you will access different features depending on your role.

Available roles:

**Admin**
Default credentials:
- نام کاربری: admin
- رمز عبور: admin123

====== منوی اصلی ======
1. افزودن مشاور
2. افزودن وقت مشاوره
3. نمایش مشاوران
4. نمایش نوبت ها
5. جستجوی نوبت بر اساس نام مشاور
6. جستجوی نوبت بر اساس تاریخ   
7. خروج

**User**
Default credentials:
- نام کاربری: user
- رمز عبور: user123

====== منوی اصلی ======
1. نمایش مشاوران
2. نمایش نوبت ها
3. جستجوی نوبت بر اساس نام مشاور
4. جستجوی نوبت بر اساس تاریخ    
5. خروج

----------------------------------------
## Data Storage Files
----------------------------------------
The system stores information in the following JSON files:

**data/users.json**
➤ Stores registered user accounts with:
- id
- username
- password
- role (admin/user)

**data/consultants.json**
➤ Stores a list of all registered consultants.
- id
- name
- specialty

**data/appointments.json**
➤ Stores all scheduled appointments, including:
- id
- consultant_id
- date
- time
- client
- created_by

These files are automatically created and updated as you use the program. You don’t need to manually edit them.

----------------------------------------

**Note:**
Always run the program using the virtual environment (if created), and keep JSON files in the correct *data/directory* to avoid errors.
