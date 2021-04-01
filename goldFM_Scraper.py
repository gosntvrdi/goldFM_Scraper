import pandas as pd
import requests
from youtube_search import YoutubeSearch
from youtube_dl import YoutubeDL
from apscheduler.schedulers.blocking import BlockingScheduler
import sys


audio_downloader = YoutubeDL({'format':'bestaudio', 'outtmpl': '%(title)s.%(ext)s', 'download_archive': 'download_archive_fn', 'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '320',}],})
download_archive_fn = '/app/archive'

def findYT():
    url2 = ('http://live.goldfm.hr:8068/played.html?sid=1')
    df = pd.read_html(url2)[1][1][1]
    query = (''.join(df))
    results = YoutubeSearch(query, max_results=1).to_dict()
    results = list(results)[:1]
    for v in results:
        url = ('https://www.youtube.com' + v['url_suffix'])
        try:
            print('Youtube Downloader'.center(40, '_'))
            audio_downloader.extract_info(url)
        except Exception:
            print("Couldn\'t download the audio")

            

scheduler = BlockingScheduler(timezone="Europe/Zagreb")
scheduler.add_job(findYT, 'interval', seconds=120, max_instances=1)
scheduler.start()

