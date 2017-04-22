#!/usr/bin/python
from sheet import get_google_sheet
from slugify import slugify

def get_entries():
    full_list = get_google_sheet()

    for i, entry in enumerate(full_list):
        entry['slug'] = slugify(entry['Name'])

    return full_list
