from datetime import datetime


def current_datetime():
    return datetime.now().strftime("%d %B %Y %I:%M %p")