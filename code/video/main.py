from pytube import YouTube
import time
import os
link = str(input('Input Your Youtube Link: '))

yt = YouTube(link)
# Video Details
print(f'Video Name:  {yt.title}, \nVideo Description: {yt.description}, \nVideo Views: {yt.views} views\n')
''' ------------------GET THE HIGHEST RESOLUTION-------------------------------'''
fileSize = yt.streams.get_highest_resolution().filesize_approx
print(f'File Size : {fileSize}')
video = yt.streams.get_highest_resolution()
time.sleep(1)
print(f'Downloading, {yt.title}')
video.download('Downloads/Videos')
print('Your Video is successfully downloaded!')


# ''' -------------------LIST ALL THE RESOLUTION-------------------------------------------------- '''
# videosAllResolution = yt.streams.filter(progressive=True, file_extension='mp4')
# ''' -------------------To list all qualities of the videos that's MP4---------------------------'''
# videos = yt.streams.filter(progressive=True, file_extension='mp4')
# '''' ------------------Download a single quality without listing them............................'''
# vid = list(enumerate(videos))
# for i in vid:
#     print(i)
# print(videos)
# quality = int(input("Enter quality index: "))
# time.sleep(1)
# print(f'Downloading, {yt.title}')
# videos[quality].download()
#
# print('Download Successfully')


# stream.filter(progressive=True, file_extension='mp4')
# stream.order_by('resolution')
# stream.desc()
# stream.get_highest_resolution()


