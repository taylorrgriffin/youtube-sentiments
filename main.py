import os
import json
import googleapiclient.discovery

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

# comments = list_comments("Y4W4Yup6_A8")
# next_page_token = comments.get('nextPageToken', None)

# print(next_page_token)
# print(len(comments['items']))
