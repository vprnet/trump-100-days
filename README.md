# Trump's First 100 Days

This project showcases a collection of voices from around the region on President Trump's first 100 days in office. The final product is [here](http://www.vpr.net/apps/vermont-100).

## Get Involved

Questions about the repo? Reach out! I'm at [@sarambsimon](http://twitter.com/sarambsimon).

## Notes on the Project

This project started from VPR's [Podcast Directory](http://www.vpr.net/podcasts). We like to recycle.

The steps to get set up are here:

1. Make sure you have Python 2.7 installed.
1. Clone the repo locally. `git clone git@github.com:vprnet/trump-100-days.git`
1. [Install `pip`](https://pip.pypa.io/en/latest/installing.html)
1. Install virtualenv. `pip install virtualenv`
1. Change into the project directory. `cd trump-100-days`
1. Create a virtual environment for the app. `virtualenv venv`
1. Enter the virtual environment. `source venv/bin/activate`
1. Install the app requirements. `pip install -r requirements.txt`
1. To run locally, just hit a quick	`python app/index.py` and head to `127.0.0.1:5000`, but know that it will all be broken until you follow the Google Spreadsheet steps below.

## Notes on Interacting with Google Spreadsheets

The project is hooked up to a Google Spreadsheet that VPR producers and editors can populate. If you're interested in cloning this project, you'll need your own Google Spreadsheet to get started.

We use [gspread](https://github.com/burnash/gspread) with the Drive API to connect our spreadsheet to the app. Here are a few things to know about the implementation:

1. To start a new project, head to the [Google Developer's Console](https://console.developers.google.com/project).
1. Click `create a project`. Give it a name.
1. Click `Enable and manage APIs`.
1. Under `Google Apps APIs` click `Drive API` and `Enable`.
1. Click `Go to Credentials`.
1. `Create Credentials`.
1. `Create service account key`, and select `New service account`. Give it a name.
1. When you `create`, you'll see a JSON file incoming. Save that file to your project directory. Add it to your gitignore if your code is going anywhere public.
1. The json file is what gets loaded and opened in `sheet.py`. Make sure the names match!
1. Create a Google Spreadsheet through your Google Drive. Make sure your spreadsheet title is exactly what's trying to be opened in `sheet.py`'s `authorization.open("")` line.
1. Share your Google Spreadsheet with the email provided in `client_email`.
