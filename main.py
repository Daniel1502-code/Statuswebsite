from flask import Flask, render_template
import requests
import datetime
import sqlite3

app = Flask(__name__)


@app.route("/")
def main():
    url_youtube = "https://www.youtube.com"
    url_twitter = "https://twitter.com/"
    url_google = "https://www.google.com"
    url_steam = "https://store.steampowered.com/"
    url_test = "http://danielduesendieb.pythonanywhere.com"

    r = requests.get(url_google)
    name1 = r.status_code
    r = requests.get(url_youtube)
    name2 = r.status_code
    r = requests.get(url_steam)
    name3 = r.status_code
    r = requests.get(url_twitter)
    name4 = r.status_code
    r = requests.get(url_test)
    test = r.status_code

    def downtime(website):
        now = datetime.datetime.now()
        print(website, "is Down... Datetime", now)

    if name1 != 200:
        downtime(url_google)
    elif name2 != 200:
        downtime(url_youtube)
    elif name3 != 200:
        downtime(url_steam)
    elif name4 != 200:
        downtime(url_twitter)
    elif test != 200:
        downtime(url_test)
    else:
        print("Everything is Running!")

    downtime = datetime.datetime.now()
    return render_template(
        "status.html",
        name1=name1,
        name2=name2,
        name3=name3,
        name4=name4,
        test=test,
        downtime=downtime,
    )


@app.route("/edit")
def edit():
    return "Still in construction!"


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
