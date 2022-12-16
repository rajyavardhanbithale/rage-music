from flask import Flask, render_template,request
from youtubesearchpython import VideosSearch
import mineRequestedData as mrd

app = Flask(__name__)



@app.route('/requests_for_song')
def requestSong():
    return None

@app.route('/player')
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


@app.route('/')
def home():
    return render_template('index.html')
 




if __name__ == '__main__':

    app.run(debug=True,port="8000")
    
