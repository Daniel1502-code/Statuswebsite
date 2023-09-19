from flask import Flask, render_template
import datetime
import json

app = Flask(__name__)

with open('data.json') as f:
    data = json.load(f)

# Define all the global variables with initial values
google_name = google_hostname = google_status = google_response_code = google_response_time_ms = ""
youtube_name = youtube_hostname = youtube_status = youtube_response_code = youtube_response_time_ms = ""
steam_name = steam_hostname = steam_status = steam_response_code = steam_response_time_ms = ""
twitter_name = twitter_hostname = twitter_status = twitter_response_code = twitter_response_time_ms = ""
test_name = test_hostname = test_status = test_response_code = test_response_time_ms = ""

@app.route("/")
def main():

    def jsonsearch():
        global google_name, google_hostname, google_status, google_response_code, google_response_time_ms
        global youtube_name, youtube_hostname, youtube_status, youtube_response_code, youtube_response_time_ms
        global steam_name, steam_hostname, steam_status, steam_response_code, steam_response_time_ms
        global twitter_name, twitter_hostname, twitter_status, twitter_response_code, twitter_response_time_ms
        global test_name, test_hostname, test_status, test_response_code, test_response_time_ms

        for server in data["web_servers"]:
            if server["name"] == "google":
                google_name = server["name"]
                google_hostname = server["hostname"]
                google_status = server["status"]
                google_response_code = server["response_code"]
                google_response_time_ms = server["response_time_ms"]
            if server["name"] == "youtube":
                youtube_name = server["name"]
                youtube_hostname = server["hostname"]
                youtube_status = server["status"]
                youtube_response_code = server["response_code"]
                youtube_response_time_ms = server["response_time_ms"]
            if server["name"] == "steam":
                steam_name = server["name"]
                steam_hostname = server["hostname"]
                steam_status = server["status"]
                steam_response_code = server["response_code"]
                steam_response_time_ms = server["response_time_ms"]
            if server["name"] == "twitter":
                twitter_name = server["name"]
                twitter_hostname = server["hostname"]
                twitter_status = server["status"]
                twitter_response_code = server["response_code"]
                twitter_response_time_ms = server["response_time_ms"]
            if server["name"] == "test":
                test_name = server["name"]
                test_hostname = server["hostname"]
                test_status = server["status"]
                test_response_code = server["response_code"]
                test_response_time_ms = server["response_time_ms"]

    jsonsearch()

    return render_template(
        "status.html",
        test_name=test_name,
        test_hostname=test_hostname,
        test_status=test_status,
        test_response_code=test_response_code,
        test_response_time_ms=test_response_time_ms,
        twitter_name=twitter_name,
        twitter_hostname=twitter_hostname,
        twitter_status=twitter_status,
        twitter_response_code=twitter_response_code,
        twitter_response_time_ms=twitter_response_time_ms,
        steam_name=steam_name,
        steam_hostname=steam_hostname,
        steam_status=steam_status,
        steam_response_code=steam_response_code,
        steam_response_time_ms=steam_response_time_ms,
        youtube_name=youtube_name,
        youtube_hostname=youtube_hostname,
        youtube_status=youtube_status,
        youtube_response_code=youtube_response_code,
        youtube_response_time_ms=youtube_response_time_ms,
        google_name=google_name,
        google_hostname=google_hostname,
        google_status=google_status,
        google_response_code=google_response_code,
        google_response_time_ms=google_response_time_ms,
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
