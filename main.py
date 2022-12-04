'''
import pafy

url = 'https://youtu.be/7dSDoh9ebVA'
video = pafy.new(url)

#print(video)

print("\n")
#streams = video.audiostreams

#for s in streams:
#    print(s.bitrate, s.extension,s.get_filesize())


bestaudio = video.getbestaudio()
print(bestaudio.url)

'''

from youtubesearchpython import VideosSearch


#print(x['result'][0]['richThumbnail']['url'])

videosSearch = VideosSearch('ram siya ram', limit = 2)

song_search_youtube = videosSearch.result()

result = song_search_youtube['result'][0]



print(result ['channel']['name'])
print(result['thumbnails'][0]['url'])
print(result['link'])

'''
import pafy

url = 'https://www.youtube.com/watch?v=u9yg83-gSRY'
video = pafy.new(url)

#print(video)

print("\n")
#streams = video.audiostreams

#for s in streams:
#    print(s.bitrate, s.extension,s.get_filesize())


bestaudio = video.getbestaudio()
#streamSongUrl =  bestaudio.url

print(bestaudio)'''