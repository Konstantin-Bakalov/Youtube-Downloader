from pytube import YouTube
from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLAKBzsqgf6j3LbenQsSXCCstJsp1Y4UCs')

for url in p.video_urls:
	try:
		yt = YouTube(url)
		yt.streams.get_highest_resolution().download('/home/airbus/Downloads/B')

	except KeyError:
		print(f'FAILED {url}')
	except Exception:
		print(f'EXEPTION {url}')
	else:
		print(f'Downloading video {url}')