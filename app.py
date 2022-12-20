from flask import Flask, render_template,request
from youtubesearchpython import VideosSearch
import mineRequestedData as mrd
import os
import generateStaticPage as gsp

app = Flask(__name__)



@app.route('/requests_for_song')
def requestSong():
    return None

'''@app.route('/player')
def player():
    parser = mrd.Search('better call saul theme')
    parserFinal = parser.processJson(True)
    print(parserFinal[0])
    return render_template('player.html',
    musicThumbnail = parserFinal[3],
    musicName = parserFinal[0],
    singerName = parserFinal[4],
    musicUrl = parserFinal[6]
    )
    '''


def frontPageContent():
    topMusic = ["careless whisper","tourne"]

@app.route('/')
def home():



    return render_template('index.html')
 

@app.route('/preLoadedPages/<id>', methods=['GET'])
def preloaded(id):
    print(id)
    return(render_template(f"preLoadedPages/{id}.html"))


global saveIdFromlPTosrch

def loadPlayer(mname):
    parser = mrd.Search(mname)
    parserFinal = parser.processJson(True)

    saveDynamic = gsp.buildPage(parserFinal[3],parserFinal[0],parserFinal[4],parserFinal[6],parserFinal[1])
    saveDynamic.build()

   
    #return render_template(f'player.html',
    #musicThumbnail = parserFinal[3]
    #musicName = parserFinal[0]
    #singerName = parserFinal[4]
    #musicUrl = parserFinal[6]
    #)
    
    return parserFinal[1]

@app.route('/', methods =["GET", "POST"])
def srch():
    if request.method == "POST":
 
       musicName = request.form.get("searchmusic")

    saveIdFromlPTosrch = loadPlayer(musicName)

    return preloaded(saveIdFromlPTosrch)

'''


@app.route('/player/')
def buildDynamic():

    if request.args.get('playid', default = 1, type = str) == '':
        print("no")
        parser = mrd.Search('No fet')
        parserFinal = parser.processJson(True)
    
        saveDynamic = gsp.buildPage(parserFinal[3],parserFinal[0],parserFinal[4],parserFinal[6],parserFinal[1])
        saveDynamic.build()

        #return render_template(f'player.html',
        #musicThumbnail = parserFinal[3]
        #musicName = parserFinal[0]
        #singerName = parserFinal[4]
        #musicUrl = parserFinal[6]
        #)
        return preloaded(request.args.get('playid', default = 1, type = str))

    if os.path.exists('templates/preLoadedPages/'+request.args.get('playid', default = 1, type = str)+'.html'):
        print("yes")
        return preloaded(request.args.get('playid', default = 1, type = str))


    else:
        print("no")
        parser = mrd.Search('BX0lKSa_PT')
        parserFinal = parser.processJson(True)
    
        saveDynamic = gsp.buildPage(parserFinal[3],parserFinal[0],parserFinal[4],parserFinal[6],parserFinal[1])
        saveDynamic.build()

        #return render_template(f'player.html',
        #musicThumbnail = parserFinal[3]
        #musicName = parserFinal[0]
        #singerName = parserFinal[4]
        #musicUrl = parserFinal[6]
        #)
        return preloaded(request.args.get('playid', default = 1, type = str))
        
'''

    
    
    #page = request.args.get('shareid', default = 1, type = str)
    #return str(page)'''


if __name__ == '__main__':

    app.run(debug=True,host="127.0.0.1",port="8000")
    
