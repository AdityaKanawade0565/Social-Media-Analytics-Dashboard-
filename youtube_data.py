from googleapiclient.discovery import build
import pandas as pd

api_key = 'AIzaSyCEVbl0NhizHM1GjHIK-u7OXc9zjWozmQY'

def get_youtube():
    youtube = build('youtube', 'v3', developerKey=api_key)
    return youtube

def get_channel_stats(youtube, channel_id):
    try:
        request = youtube.channels().list(
            part='snippet,contentDetails,statistics',
            id=channel_id
        )
        response = request.execute()

        all_data = []
        for i in range(len(response['items'])):
            data = dict(
                Channel_name=response['items'][i]['snippet']['title'],
                Subscribers=response['items'][i]['statistics']['subscriberCount'],
                Views=response['items'][i]['statistics']['viewCount'],
                Total_videos=response['items'][i]['statistics']['videoCount'],
                playlist_id=response['items'][i]['contentDetails']['relatedPlaylists']['uploads']
            )
            all_data.append(data)

        return all_data
    except Exception as e:
        print(f"An error occurred while fetching channel stats: {e}")
        return []

def get_playlist_id(youtube, channel_id):

    channel_statistics = get_channel_stats(youtube,channel_id)
    playlist_id = channel_statistics[0]['playlist_id']

    return playlist_id


#Funtion to get video ids
def get_video_ids(youtube, playlist_id):
    
    request = youtube.playlistItems().list(
                part = 'contentDetails',
                playlistId = playlist_id,
                maxResults = 50)
    response = request.execute()
    
    video_ids = []
    for i in range(len(response['items'])):
        data = response['items'][i]['contentDetails']['videoId']
        video_ids.append(data)
    
    next_page_token = response.get('nextPageToken')
    more_pages = True
    
    while(more_pages):
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                        part = 'contentDetails',
                        playlistId = playlist_id,
                        maxResults = 50,
                        pageToken = next_page_token)

            response = request.execute()
            
            for i in range(len(response['items'])):
                data = response['items'][i]['contentDetails']['videoId']
                video_ids.append(data)
                
            next_page_token = response.get('nextPageToken')

    return video_ids

# Function to extract video details

def get_video_details(youtube, video_ids):
    all_video_stats = []

    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part='snippet, statistics',
            id=','.join(video_ids[i:i + 50]),
            maxResults=50
        )
        response = request.execute()

        for video in response.get('items', []):
            video_stats = {
                'Title': video['snippet']['title'],
                'Published_date': video['snippet']['publishedAt'],
                'Views': pd.to_numeric(video['statistics'].get('viewCount', 0)),
                'Likes': pd.to_numeric(video['statistics'].get('likeCount', 0)),
                'Comments': pd.to_numeric(video['statistics'].get('commentCount', 0))
            }
            all_video_stats.append(video_stats)

    return all_video_stats
