#!/usr/bin/python
from sheet import get_google_sheet

def get_entries():
    full_list = get_google_sheet()
    return full_list
