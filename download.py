from pytube import YouTube
from sys import argv

link = argv[1]

try :
    yt = YouTube(link)

    # video = yt.streams.get_by_resolution('720p')
    video = yt.streams.get_highest_resolution()

    video.download('/home/airbus/Downloads')

except Exception as e:
    print('problem', e)