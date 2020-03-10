## twitter-summarizer-rest-service-jyueling
This assignment allows homework 4 video converter to run AWS, and using Flask as the WEB platform.

## Reference

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
- [Flask](https://palletsprojects.com/p/flask/)
- [Flask-RESTFUL](https://flask-restful.readthedocs.io/)
- [AWS](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc)

## How to Run
visit the following:
```python
http://ec2-3-19-185-70.us-east-2.compute.amazonaws.com:8000/
```

## Example Result
After connected to the AWS link, the website would show:
![Image text](https://github.com/BUEC500C1/twitter-summarizer-rest-service-jyueling/raw/master/result1.png)
Enter the username of the twitter and number of tweets, the result would show:
![Image text](https://github.com/BUEC500C1/twitter-summarizer-rest-service-jyueling/raw/master/result2.png)


