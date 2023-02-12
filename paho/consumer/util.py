import time


TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_current_time():
    return time.strftime(f"{TIME_FORMAT}", time.localtime())
