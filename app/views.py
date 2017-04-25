from index import app
from flask import render_template, request
from query import get_entries
from config import BASE_URL

entries = get_entries()

project_social = {
    "url": BASE_URL,
    "title": "Nearly 100 Days Into Trump's Administration...",
    "subtitle": "",
    "img": "http://mediad.publicbroadcasting.net/p/vpr/files/vpr-100-twitter.jpg",
    "description": "Add your voice to VPR coverage.",
    "twitter_text": "",
    "twitter_hashtag": ""
}


@app.route("/")
def index():
    page_url = BASE_URL + request.path
    page_title = "Vermont's Response: Trump's First 100 Days"
    landing = True

    social = project_social

    return render_template("content.html",
        page_title=page_title,
        social=social,
        entries=entries,
        landing=landing,
        project_social=project_social,
        page_url=page_url)


@app.route("/contribute")
def contribute_page():
    page_url = BASE_URL + request.path
    page_title = "Vermont's Response: Share Your Thoughts"

    social = project_social

    return render_template("contribute.html",
        page_title=page_title,
        social=social,
        entries=entries,
        project_social=project_social,
        page_url=page_url)


@app.route("/<Slug>")
def entry_page(Slug):
    for entry in entries:
        if "slug" in entry and Slug == entry["slug"]:
            entries.remove(entry)
            entries.insert(0, entry)

    page_url = BASE_URL + request.path
    page_title = "Vermont's Response: Trump's First 100 Days"

    social = {
        "title": page_title,
        "subtitle": "Nearly 100 Days Into the Trump Administration",
        "img": "http://mediad.publicbroadcasting.net/p/vpr/files/vpr-vermont-100-feeling.png",
        "description": "From Vermont Public Radio",
        "twitter_text": entries[0]["Name"],
        "twitter_hashtag": ""
    }

    return render_template("content.html",
        page_title=page_title,
        social=social,
        entries=entries,
        project_social=project_social,
        page_url=page_url)
