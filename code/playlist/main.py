from pytube import Playlist
link = input("Enter you Playlist Link:  ")
playlist = Playlist(link)
print(f'Playlist Title: {playlist.title}')
videosList = playlist.videos
for video in videosList:
    video.streams.get_highest_resolution().download('Downloads')
    print(f'Video:  {video.title} download is processing, please wait...')
    print('Video download successfully')


