from datetime import datetime as dt

def tell_time():
    time_str = dt.now().strftime("%I:%M %p")
    return f"The current time is {time_str}"

def tell_date():
    date_str = dt.now().strftime("%B %d, %Y")
    return f"Today's date is {date_str}"
