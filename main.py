import os, re, json
import googleapiclient.discovery

from nlp_analysis import analyze_comments

# fetch comments from youtube video given its id
def list_comments(id, page_token):

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
        videoId=id,
        pageToken= page_token if page_token != None else ""
    )
    response = request.execute()

    return(response)

def getText(c):
    # TODO: weigh decision of using textOriginal vs. textDisplay
    return(c["snippet"]["topLevelComment"]["snippet"]["textOriginal"])

def comments_analysis(id, page_token):
    # regex credit: github user gustavoja, https://regex101.com/r/7CxmJP/8
    # youtube_url_regex = "(?:http:|https:)*?\/\/(?:www\.|)(?:youtube\.com|m\.youtube\.com|youtu\.|youtube-nocookie\.com).*(?:v=|v%3D|v\/|(?:a|p)\/(?:a|u)\/\d.*\/|watch\?|vi(?:=|\/)|\/embed\/|oembed\?|be\/|e\/)([^&?%#\/\n]*)"
    # match = re.findall(youtube_url_regex, url)

    # make sure exactly one id can be extracted from url
    # if len(match) != 1:
    #     raise Exception("Invalid url format")

    # id = match[0]
    
    # pull comments from video
    comments_res = list_comments(id, page_token)
    comments = [getText(i) for i in comments_res["items"]]

    # extract next page token for subsequent requests
    next_page_token = comments_res.get('nextPageToken', None)

    # run sentiment analysis on comments
    analysis = analyze_comments(comments)

    return { "analysis": analysis, "nextPageToken": next_page_token }