import os


class buildPage():

    def __init__(self,thumbnail,mName,sName,mUrl,id) -> None:
        self.musicThumbnail = thumbnail
        self.musicName = mName
        self.singerName = sName
        self.musicUrl = mUrl
        self.saveId = id



    def build(self):









        with open('templates/player.html','r') as readPlayerHtml:
            readPlayerHtml = readPlayerHtml.read().replace("{{ musicThumbnail }}",self.musicThumbnail).replace("{{ musicName }}",self.musicName).replace("{{ singerName }}",self.singerName).replace("{{ musicUrl }}",self.musicUrl)
           

        with open(f'templates/preLoadedPages/{self.saveId}.html','w') as writeSaveIdHtml:
            writeSaveIdHtml.write(readPlayerHtml)

            writeSaveIdHtml.close()
        


#run = buildPage('https://i.ytimg.com/vi_webp/8jzDnsjYv9A/sddefault.webp',"Sam Smith - Writing's On The Wall (from Spectre) (Official Music Audio)","SamSmithVEVO"," https://rr3---sn-gwpa-civl.googlevideo.com/videoplayback?expire=1671281603&ei=Y2edY8fJNKWAjuMPmPOW6AY&ip=49.43.42.237&id=o-ANbVT_ZsCm1Lo8uZm3vuSberpNJ9CjOcG0hqwQODYjL1&itag=140&source=youtube&requiressl=yes&mh=ZP&mm=31%2C29&mn=sn-gwpa-civl%2Csn-gwpa-cvhs&ms=au%2Crdu&mv=m&mvi=3&pl=22&gcr=in&initcwndbps=252500&vprv=1&mime=audio%2Fmp4&gir=yes&clen=4605265&dur=284.514&lmt=1649387789157792&mt=1671259532&fvip=4&keepalive=yes&fexp=24001373%2C24007246&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhANlApD3AFLhSmDFo7IwDw4FeBBQG9MWBf7BhlhqjORyIAiEAsobIaDNhbCpKvA51-q8Z7KtOOaj5T9MrOPjSeWgVRFE%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAMi7Meyvqp39flsEfAM0nYNhNxqLgKeO54mv58QUtBdUAiAcCS99I7xFwmfkCyILwO6CBpICRhbsZpnP7kMkICCtSA%3D%3D","8jzDnsjYv9A")
#run.build()


