from flask import Flask, render_template,request
from youtubesearchpython import VideosSearch
import pafy

app = Flask(__name__)

audio = '''
https://rr6---sn-gwpa-civy.googlevideo.com/videoplayback?expire=1669926607&ei=brqIY8PELeq-
juMPmMSF-AY&ip=49.36.24.215&id=o-AAqjuGkc8avFmFPNqb9zYGTjUIy8XiyvyJugpwjYZWQp&itag=140&sour
ce=youtube&requiressl=yes&mh=17&mm=31%2C29&mn=sn-gwpa-civy%2Csn-gwpa-cvhe7&ms=au%2Crdu&mv=m&
mvi=6&pl=23&initcwndbps=172500&vprv=1&mime=audio%2Fmp4&ns=_J_t0EmqblKvEt9u2Wp_IuIJ&gir=yes&cle
n=4040753&dur=249.614&lmt=1667080298791647&mt=1669904514&fvip=6&keepalive=yes&fexp=24001373%2C
24007246&c=WEB&txp=5432434&n=vI4v0UzAz1VIjj3&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Cre
quiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl
%2Cinitcwndbps&lsig=AG3C_xAwRQIhALmcyiTRcpEeM03um4X7-56SuHNgwsGzd6uZfnEwPBn0AiAn96mN0yVhmwOn8Ei
wCbk_GdyAr7Z4F40oI5JVljoYwg%3D%3D&sig=AOq0QJ8wRgIhAIbU_SYwiMxFirXeD2ZoMFF5glCSnxIaHmHLj0YbalqQA
iEA-XSXguV2UtT-nKPeF2cgx2b0HE9mna3xxf_96y8e7z0=

'''

class songSearch():
    print('init')
    def __init__(self) -> None:
        self.song = 'open it up'
        self.songName = 0
        self.channelName = 0
        self.thumbnailUrl = 0
        self.songUrl =0

        self.streamSongUrl = 0;

 

    def song_search(self):
        print('song search')
        videosSearch = VideosSearch(self.song, limit = 2)

        song_search_youtube = videosSearch.result()

        result = song_search_youtube['result'][0]

        song = VideosSearch('careless whisper', limit = 2)

        self.songName =  result['title']

        self.channelName =  result ['channel']['name']
        self.thumbnailUrl =  result['thumbnails'][0]['url']
        self.songUrl = result['link']

        print(self.songName)



    def table(self):

        print('table') 
        self.song_search()

        struct =  f'''
        <table>
        <tr>
            <th> SongName </th>
            <th> Chanelname </th>
            <th> Thumbnail </th>
            <th> Song </th>
        </tr>

        <tr>
            <td>{self.songName}</td>
            <td>{self.channelName}</td>
            <td><img src="{self.thumbnailUrl}"></img></td>
            <td> </td>
        </tr>
        </table>
        '''
        return struct

    def grab_url(self):
        

        url = self.songUrl
        video = pafy.new(url)

        #print(video)

        print("\n")
        #streams = video.audiostreams

        #for s in streams:
        #    print(s.bitrate, s.extension,s.get_filesize())


        bestaudio = video.getbestaudio()
        self.streamSongUrl =  bestaudio.url

        print(self.streamSongUrl)

        return self.streamSongUrl




@app.route('/', methods =["GET", "POST"])
def requests_for_song():

    if request.method == "POST":
       # getting input with name = fname in HTML form
       sname = request.form.get("sname")
     
    
    return index(sname)




displayTable = songSearch()



@app.route('/')
def index(processSongName):
    displayTable.song = processSongName
    print(processSongName)
    return render_template('index.html',table=displayTable.table(),audio_url=displayTable.grab_url())





if __name__ == '__main__':

    app.run(debug=True,port=8000)
    
