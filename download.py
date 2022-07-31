from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link)

# video = yt.streams.get_by_resolution('480p')
video = yt.streams.get_highest_resolution()

video.download('/home/airbus/Downloads')