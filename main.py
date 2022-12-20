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

'''from youtubesearchpython import VideosSearch
from youtubesearchpython import *

#print(x['result'][0]['richThumbnail']['url'])

videosSearch = VideosSearch('Tourner Dans Le Vide', limit = 2)
fetcher = StreamURLFetcher()


song_search_youtube = videosSearch.result()

result = song_search_youtube['result'][0]


video = Video.get(result['link'])
print(result ['channel']['name'])
print(result['thumbnails'][0]['url'])
print(result['link'])
print(result['duration'])
url = fetcher.get(video, 251)
print(url)'''






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



from youtubesearchpython import VideosSearch
from youtubesearchpython import *


musicSearch = VideosSearch('Tourner Dans Le Vide', limit = 2)
urlFetch = StreamURLFetcher()

song_search_youtube = musicSearch.result()   #Search music of Youtube
#
result = song_search_youtube['result'][0]


#
#
#print(result)
#



#video = Video.get(result['link'])
#url = urlFetch.get(video, 251)
#
#print(result ['channel']['name'])
#print(result['thumbnails'][0]['url'])
#print(result['id'])
#print(result['duration'])

#print(url)


def musicExtractUrl(jsonData):

    dat = jsonData


    for x in range (int(len(dat['streamingData']['adaptiveFormats']))):

        if 'audio/mp4' in dat['streamingData']['adaptiveFormats'][x]['mimeType']:
            if 'AUDIO_QUALITY_MEDIUM' in dat['streamingData']['adaptiveFormats'][x]['audioQuality']:
                #print( dat['streamingData']['adaptiveFormats'][x]['mimeType'],':', dat['streamingData']['adaptiveFormats'][x]['audioQuality']) 
                #print(dat['streamingData']['adaptiveFormats'][x]['url'])

                return dat['streamingData']['adaptiveFormats'][x]['url']

def thumbnailExtractUrl():
	thumbnailsSize = []
	for x in range(len(music['thumbnails'])):
		refSzie = music['thumbnails'][x]['width'] + music['thumbnails'][x]['height']
		thumbnailsSize.append(refSzie)

	return thumbnailsSize.index(max(thumbnailsSize))


music = Video.get(f"https://music.youtube.com/watch?v=yBm4K00SMEk", mode = ResultMode.json, get_upload_date=True)
print(music)

print('Title    : ',music['title'])
print('ID       : ',music['id'])
print('Duration : ', str("{:.2f}".format(int(music['duration']['secondsText'])/60)).replace('.',':') )    #
print('Thumbnail: ',music['thumbnails'][thumbnailExtractUrl()]['url'])
print('Uploader : ',music['channel']['name'])
print('Upl. Date: ',music['uploadDate'])
print('Audio URL: ',musicExtractUrl(music))



print()







#print(int(len(dat['streamingData']['adaptiveFormats'])))



'''
	<!--
	<form action="{{ url_for("requests_for_song")}}" method="post">
		<label for="firstname">SongName Name:</label>
		<input type="text" id="songname" name="sname" placeholder="songname">

		<button type="submit">Search</button>
	</form>


	<br>
	<br>
	{{table | safe}}

	<br><br>
	<audio controls>

		<source src="{{ audio_url }}" type="audio/mpeg">
		Your browser does not support the audio element.

	</audio>-->
'''