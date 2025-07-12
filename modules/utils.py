from datetime import datetime

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
            break   
        else:
            continue
        return False                 
    
       