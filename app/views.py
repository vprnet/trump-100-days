from index import app
from flask import render_template, request
from query import get_entries
from config import BASE_URL

entries = get_entries()

project_social = {
    "url": BASE_URL,
    "title": "",
    "subtitle": "",
    "img": "",
    "description": "",
    "twitter_text": "",
    "twitter_hashtag": ""
}


@app.route("/")
def index():
    page_url = BASE_URL + request.path
    page_title = ""
    landing = True

    social = project_social

    return render_template("content.html",
        page_title=page_title,
        social=social,
        entries=entries,
        landing=landing,
        project_social=project_social,
        page_url=page_url)


@app.route("/<Name>")
def entry_page(Name):
    for entry in entries:
        if "slug" in entry and Name == entry["slug"]:
            entries.remove(entry)
            entries.insert(0, entry)

    page_url = BASE_URL + request.path
    page_title = entries[0]["Name"]

    social = {
        "title": page_title,
        "subtitle": "",
        "img": "",
        "description": "",
        "twitter_text": "",
        "twitter_hashtag": ""
    }

    return render_template("content.html",
        page_title=page_title,
        social=social,
        entries=entries,
        project_social=project_social,
        page_url=page_url)
