import tweepy
from tweepy import OAuthHandler
import google_api
import configparser
from glob import glob
import wget
from PIL import Image, ImageDraw, ImageFont
import urllib
import shutil  
import sys


def print_tweet(username,num):
    config = configparser.ConfigParser()
    config.read("keys")
    auth = OAuthHandler(config.get('auth', 'consumer_key').strip(),
                               config.get('auth', 'consumer_secret').strip())
    auth.set_access_token(config.get('auth', 'access_token').strip(),
                          config.get('auth', 'access_secret').strip())

    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name=username,count=num)
    
    media_files = set()

    d = 1
    for status in tweets:
#        print('-----------------------------------------')
#        print('Twitter Feed ' + str(d))
#        print('-----------------------------------------')
#
#        print(status.text)
        media = status.entities.get('media', [])
        
        if(len(media) > 0):
            filename="./Image/"+username+"_img_%d.jpg"%d
#            print('-----------------------------------------')
            #wget.download(media[0]['media_url'])
            urllib.request.urlretrieve(media[0]['media_url'],filename)
            img = Image.open(filename)
            img.resize((300,200))
            img.save(filename)
            media_files.add(media[0]['media_url'])
#            print('Image url: '+ media[0]['media_url'])
#            print()
#            print('Description: ')
            google_api.google_image_detect(media[0]['media_url'])
            d+=1
            
        if(len(status.text) > 0):
            filename="./Image/"+username+"_img_%d.jpg"%d
            createImg(status.text,filename)
            d+=1
#        print('-----------------------------------------')


    
    return True

def createImg(text,filename):
    i = 0
    textlist = ""
    while i < len(text):
        textlist = textlist + text[i:i+35] + '\n'
        i += 35 
    try:   
        img = Image.new('RGB', (300, 200), color = (0, 0, 0))
     
        font = ImageFont.truetype('Arial.ttf', 15)
        draw = ImageDraw.Draw(img)
        draw.text((10,10), textlist, font=font, fill=(255, 255, 0))
     
        img.save(filename)
        return "Success"
    except Exception as e:
        return "Failed create image"
def main():
    print(sys.argv[1])
    print(sys.argv[2])
    print_tweet(sys.argv[1],sys.argv[2])
    
if __name__ == "__main__":
    main()