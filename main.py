import os
import json
import googleapiclient.discovery

from nlp_analysis import analyze_comments

# fetch comments from youtube video given its id
# TODO: add next_page_token as optional arg
def list_comments(id):

    # load developer key from secrets.json
    with open('secrets.json') as secrets_file:
        secrets = json.load(secrets_file)
        DEVELOPER_KEY = secrets["developerKey"]

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=100,
        videoId=id
    )
    response = request.execute()

    return(response)

def getText(c):
    # TODO: weigh decision of using textOriginal vs. textDisplay
    return(c["snippet"]["topLevelComment"]["snippet"]["textOriginal"])

def comments_analysis(url):
    # TODO: add string methods to pull video id out of url
    # TODO: remove hardcoded video id
    # TODO: accept nextPageToken, pass into into list_comments, and pass it back to user
    comments_res = list_comments("Y4W4Yup6_A8")

    comments = [getText(i) for i in comments_res["items"]]
    next_page_token = comments_res.get('nextPageToken', None)

    return analyze_comments(comments)