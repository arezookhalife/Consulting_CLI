# Consulting Appointment CLI System

A simple and extensible Python-based command-line project for managing consultants and scheduling appointments, with user role separation (Admin / Regular User).

---------

## Features

- Role-based login system (Admin and User)
- Admin-only features: Add new consultants and register appointments
- Search appointments by date or consultant name
- Data storage using JSON files for simplicity and portability

---------

## Running the Project

Make sure you have **Python 3.8+** installed.

### 1. Clone the project
```bash
git clone https://github.com/arezookhalife/Consulting_CLI.git
cd consulting-cli
```

### 2. Set up a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate     # On Linux/macOS
venv\Scripts\activate        # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the project
```bash
python main.py
```

### Login Credentials
* Admin
    Username: admin
    Password: admin123

* Users
    User data is stored in the **users.json** file, and new users can be added to this file.


### Project Structure
```pgsql
consulting-cli/
├── main.py
├── modules/
│   ├── appointments.py
│   ├── consultants.py
│   ├── users.py
│   └── utils.py
├── data/
│   ├── consultants.json
│   ├── appointments.json
│   └── users.json
├── requirements.txt
├── USAGE.md
└── README.md
```

### Future Improvements
* Add a GUI using Tkinter or PyQt
* Connect to a real database (SQLite or PostgreSQL)
* Add email/SMS reminders for appointments
* Add appointment cancellation/editing options

### Developer
- Arezoo Khalifeh | Python Developer 
- GitHub: arezookhalife