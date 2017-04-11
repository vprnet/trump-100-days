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
