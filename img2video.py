import os
import io
from io import BytesIO
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

def reshape():
    d = 0
    for image in os.listdir('./Image/'):
#        print(image)
        
        if image.endswith('.jpg'):
            with open(image, 'rb') as f:
                print(image)
                b = BytesIO()
                f.seek(15, 0)
                b.write(f.read())
                img = Image.open(b)
                img.load()
#                img = Image.open('./Image/'+image)
                img.resize((300,200))
                img.save('./Image/'+image)
            d+=1
            
def ffmpeg(username):
#    reshape()
    try:
        os.popen('ffmpeg -framerate 1/3 -i ./Image/'+username+'_img_%d.jpg ./outputVideo/'+username+'_video.mp4').read()
        return "Success"
    except Exception as e:
        return "Failed create video" 
    
#if __name__ == "__main__":
#    ffmpeg("@Discovery")