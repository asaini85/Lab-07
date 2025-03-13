#!/usr/bin/env python3
# Student ID: asaini85

from lab7a import *

def change_time(time, seconds):
    """Modify time object by adding seconds."""
    time.second += seconds
    if valid_time(time) != True:
        while time.second >= 60:
            time.second -= 60
            time.minute += 1
        while time.minute >= 60:
            time.minute -= 60
            time.hour += 1
        while time.second < 0:
            time.second += 60
            time.minute -= 1
        while time.minute < 0:
            time.minute += 60
            time.hour -= 1
    return None
