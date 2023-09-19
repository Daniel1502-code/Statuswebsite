import requests
import time
import json

print("Program Starting!")

name1_status = ""
name2_status = ""
name3_status = ""
name4_status = ""
test_status = ""

while True:
    url_youtube = "https://www.youtube.com"
    url_twitter = "https://twitter.com/"
    url_google = "https://www.google.com"
    url_steam = "https://store.steampowered.com/"
    url_test = "http://danielduesendieb.pythonanywhere.com"

    print("Requesting Servers...")
    googler_request = requests.get(url_google)
    name1 = googler_request.status_code
    youtube_request = requests.get(url_youtube)
    name2 = youtube_request.status_code
    steam_request = requests.get(url_steam)
    name3 = steam_request.status_code
    twitter_request = requests.get(url_twitter)
    name4 = twitter_request.status_code
    test_request = requests.get(url_test)
    test = test_request.status_code

    print("Requests Done!")
    print(googler_request.elapsed.total_seconds())
    print(youtube_request.elapsed.total_seconds())
    print(steam_request.elapsed.total_seconds())
    print(twitter_request.elapsed.total_seconds())
    print(test_request.elapsed.total_seconds())

    google_ms = googler_request.elapsed.total_seconds()
    youtube_ms = googler_request.elapsed.total_seconds()
    steam_ms = googler_request.elapsed.total_seconds()
    twitter_ms = googler_request.elapsed.total_seconds()
    test_ms = googler_request.elapsed.total_seconds()

    print("Writing Data!")


    def OnlineChecker():
        global name1_status, name2_status, name3_status, name4_status, test_status

        if name1 == 200:
            name1_status = "Online"
        else:
            name1_status = "Offline"
        if name2 == 200:
            name2_status = "Online"
        else:
            name2_status = "Offline"
        if name3 == 200:
            name3_status = "Online"
        else:
            name3_status = "Offline"
        if name4 == 200:
            name4_status = "Online"
        else:
            name4_status = "Offline"
        if test == 200:
            test_status = "Online"
        else:
            test_status = "Offline"


    OnlineChecker()

    dictionary = {
        "web_servers": [
            {
                "name": "google",
                "hostname": url_google,
                "status": name1_status,
                "response_code": name1,
                "response_time_ms": google_ms
            },
            {
                "name": "youtube",
                "hostname": url_youtube,
                "status": name2_status,
                "response_code": name2,
                "response_time_ms": youtube_ms
            },
            {
                "name": "steam",
                "hostname": url_steam,
                "status": name3_status,
                "response_code": name3,
                "response_time_ms": steam_ms
            },
            {
                "name": "twitter",
                "hostname": url_twitter,
                "status": name4_status,
                "response_code": name4,
                "response_time_ms": twitter_ms
            },
            {
                "name": "Server Test",
                "hostname": url_test,
                "status": test_status,
                "response_code": test,
                "response_time_ms": test_ms
            }
        ]
    }
    print("Writing Data done!")

    #  json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to data.json
    with open("data.json", "w") as outfile:
        outfile.write(json_object)
    time.sleep(30)

    print("Waiting 30 Secs")
