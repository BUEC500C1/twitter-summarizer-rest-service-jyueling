from google.cloud import vision
from google.cloud.vision import types
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="homework2-38b13453b129.json"

def google_image_detect(url):
    client = vision.ImageAnnotatorClient()

    img = vision.types.Image()
    img.source.image_uri = url

    response = client.label_detection(image=img)
    labels = response.label_annotations
    
#    for label in labels:
#        print(' '+ label.description)