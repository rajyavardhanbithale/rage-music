
from youtubesearchpython import VideosSearch
from youtubesearchpython import *
import generateStaticPage as gsp


class Search:
    def __init__(self,name) -> None:
        self.musicName = name
        self.debug = False 

        


    
    def extractJson(self):

   
        musicSearch = VideosSearch(self.musicName, limit = 1)

        musicResultYoutubeVideos = musicSearch.result()


        musicResultYoutubeMusic = Video.get(f"https://music.youtube.com/watch?v={musicResultYoutubeVideos['result'][0]['id']}", mode = ResultMode.json, get_upload_date=True)

        return musicResultYoutubeMusic


    def processJson(self,debug):
        music = self.extractJson()
        if debug == True:
  

            print('Title    : ',music['title'].replace('Video','Audio'))
            print('ID       : ',music['id'])
            print('Duration : ', str("{:.2f}".format(int(music['duration']['secondsText'])/60)).replace('.',':') )    #
            print('Thumbnail: ',music['thumbnails'][self.thumbnailExtractUrl()]['url'])
            print('Uploader : ',music['channel']['name'])
            print('Upl. Date: ',music['uploadDate'])
            print('Audio URL: ',self.musicExtractUrl())

            return music['title'], music['id'], str("{:.2f}".format(int(music['duration']['secondsText'])/60)).replace('.',':'),music['thumbnails'][self.thumbnailExtractUrl()]['url'], music['channel']['name'], music['uploadDate'], self.musicExtractUrl()
        else:
            return music['title'], music['id'], str("{:.2f}".format(int(music['duration']['secondsText'])/60)).replace('.',':'),music['thumbnails'][self.thumbnailExtractUrl()]['url'], music['channel']['name'], music['uploadDate'], self.musicExtractUrl()

    def musicExtractUrl(self):

        dat = self.extractJson()


        for x in range (int(len(dat['streamingData']['adaptiveFormats']))):

            if 'audio/mp4' in dat['streamingData']['adaptiveFormats'][x]['mimeType']:
                if 'AUDIO_QUALITY_MEDIUM' in dat['streamingData']['adaptiveFormats'][x]['audioQuality']:
                    #print( dat['streamingData']['adaptiveFormats'][x]['mimeType'],':', dat['streamingData']['adaptiveFormats'][x]['audioQuality']) 
                    #print(dat['streamingData']['adaptiveFormats'][x]['url'])

                    return dat['streamingData']['adaptiveFormats'][x]['url']


    def thumbnailExtractUrl(self):

        dat = self.extractJson()

        thumbnailsSize = []
        for x in range(len(dat['thumbnails'])):
            refSzie = dat['thumbnails'][x]['width'] + dat['thumbnails'][x]['height']
            thumbnailsSize.append(refSzie)

        return thumbnailsSize.index(max(thumbnailsSize))



run = Search('No time to die')


parserFinal = run.processJson(True)
print(parserFinal[6])
'''saveDynamic = gsp.buildPage(parserFinal[3],parserFinal[0],parserFinal[4],parserFinal[6],parserFinal[1])
saveDynamic.build()'''

'''

Title       :  0   
ID          :  1   
Duration    :  2   
Thumbnail   :  3   
Uploader    :  4   
Upl. Date   :  5
Audio URL   :  6  

'''