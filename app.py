from pafy import new
import pyshorteners
# url of video

import requests
from flask import Flask,request,jsonify
# instant created
#video = pafy.new(url)

# print title
app=Flask(__name__)
@app.route('/' ,methods=['POST'])
def helloworld():
   

   try:
       data = request.get_json()
       link = str(data['queryResult']['queryText'])
       video = new(link)


       # api_key = "17efd5015e4a69d287611d9121378a8fb1068"
       # api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
       # print(api_url)
       # or
       # api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name=some_unique_name"
       # make the request
       # data = requests.get(api_url).json()["url"]
       # if data["status"] == 7:
       # OK, get shortened URL
       #   shortened_url = data["shortLink"]
       #  print("Shortened URL:", shortened_url)
       # else:
       #   print("[!] Error Shortening URL:", data)



   except:

       err="Unfortunately! i am not able to Process your link 🥺\nCurrently i only work on youtube video's 🔗\nPlease Click /helpme to know more 🙏 \n @Youtube_audi0_video_bot ❤"
       response1 = {
           "fulfillmentText": "{}".format(err)
       }
       return  jsonify(response1)

   a = video.getbestaudio()
   print(a.url)
   a1 = a.url
   title = video.title
   b = video.getbestvideo()
   print(b.url)
   b1 = b.url
   shortner = pyshorteners.Shortener()
   a11 = shortner.tinyurl.short(a1)
   b11 = shortner.tinyurl.short(b1)
   print(a11)
   print(b11)
   a = "SUCCESSFULLY PROCESSED ☺\n{}             \nAudio: {} \nVideo: {}  \ncurrently the bot is in development stage please keep using it.‍💻\n@Youtube_audi0_video_bot ❤".format(title, a11, b11)
   response = {
       "fulfillmentText": "{} ".format(a)
      }

   print(a)
   return jsonify(response)

if __name__ == "__main__":
        app.run(debug=True)



