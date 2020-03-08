import tweet_api
from os import path
import os

def test():
    if path.exists("keys") and os.stat("keys").st_size != 0:
        tweet_api.print_tweet("@Discovery",20)
    else:
        return "keys file is empty or does not exist"
if __name__== "__main__":
   test()