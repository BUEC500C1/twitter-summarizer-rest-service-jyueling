import queue
import threading
import tweet_api
import google_api
import img2video
import sys


thread_num = 4

q = queue.Queue()

USERNAME = ["@Discovery","@Twitter","@Google","@BU_Tweets"]

def ffmpeg_img2video(num,q):
    while True:
        username = q.get()
        d = 0
        if username is None:
            d = 0
            break
        d+=1
        print("Processing No." + str(d) + " from " + str(q.qsize()) + " items\n")
        tweet_api.print_tweet(username,num)
        img2video.ffmpeg(username)
        print("Done!")
        q.task_done()
    
def queue_sys():
    username_queue = queue.Queue()
    threads = []
    [username_queue.put(i) for i in sys.argv[1:]]
    
    for i in range(thread_num):
        t = threading.Thread(target=ffmpeg_img2video,args = (20,username_queue))
        t.daemon = True
        t.start()
        threads.append(t)
    q.join() 
    
    for i in range(thread_num):
        q.put(None)
    for j in threads:
        t.join()
        
    
if __name__ == "__main__":
    queue_sys()
    
        
    