from pytube import YouTube
from sys import argv

link = argv[1]

def on_progress(a, b, c):
    pass

try :
    # yt = YouTube(link)
    yt = YouTube(link, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)

    # video = yt.streams.get_by_resolution('720p')
    video = yt.streams.get_highest_resolution()

    video.download('/home/airbus/Downloads')

except Exception as e:
    print('problem', e)