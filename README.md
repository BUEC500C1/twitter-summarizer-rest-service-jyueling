## twitter-summarizer-rest-service-jyueling
This assignment allows multithreads to get tweets and image from twitter then convert it to videos according to each twitter accounts. Each frame of the video is 3 seconds.

## Requirement

Get credentials of Twitter API, Google Vision API and ffmpeg

- [Twitter API](https://developer.twitter.com/en/apps)
	<br> Create a file called "keys" under the dame directory of python files in following format
	```python
  [auth]
	consumer_key = consumer key
	consumer_secret = consumer secret
	access_token = access token
	access_secret = access secret
	```
- [Google Vision API](https://cloud.google.com/vision/docs/quickstart-cli?hl=en)
	<br> Copy the JSON file under the same directory of python files.
	<br> Change the filename in google_api.py 
	```python
  os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="yourfilename.json"
  ```
- [ffmpeg](http://ffmpeg.org/)
## Assignment Question Answers

-   How many API calls you can handle simultaneously and why?
    <br>My laptop is quad-core that it has 4 processors, so that it can handle 4 API calls simultaneously.
-   For example, run different API calls at the same time?
    <br>It can run different API calls at the same time
-   Split the processing of an API into multiple threads?
    <br>The processing of the API is split into 4 multiple threads.
	
## Example Result
The video result is in the output video folder accoding to each twitter account. 
![Image text](https://github.com/BUEC500C1/video-jyueling/raw/master/video_result.png)
The image results from each twitter account are in the Image folder.
![Image text](https://github.com/BUEC500C1/video-jyueling/raw/master/image_result.png)

