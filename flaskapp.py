from flask import Flask, render_template, url_for,request
import tweet_api
import img2video
import os
from datetime import timedelta

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds = 1)


@app.route("/")
def root():
#    return render_template('main_sys.html') #this line use for running the queue system
    return render_template('main.html')

@app.route('/', methods=['POST'])
def post():

    username = request.form['username']
    tweetNum = request.form['tweetNum']

#    arg="python queue_system.py "+ str(username) #this line use for running the queue system
    arg="python tweet_api.py "+ str(username) +" "+ str(tweetNum)
    os.system(arg)
#    a = tweet_api.print_tweet(username,tweetNum)
    img2video.ffmpeg(username)
    return render_template('result.html')



if __name__ == '__main__':
    app.run(debug=True)
 #   app.run(host = '0.0.0.0', port = 8000)