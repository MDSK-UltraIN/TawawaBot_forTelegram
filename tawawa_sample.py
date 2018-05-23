#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import requests

#Variables that contains the user credentials to access Twitter API
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        decoded = json.loads(data)
        print(json.dumps(decoded,sort_keys=True))
        print(decoded['text'].encode('utf-8', 'ignore'),
              decoded['text'],
              type(decoded['text'])
              )
        
        chat_id = "" #telegram chat id
        apiurl = '' #telegram bot api
        


        try: #if photo exist ,then do the work
            print(decoded["entities"]["media"][0]["media_url_https"])
            telemethod = "sendPhoto"
            urlphoto = '%s%s?chat_id=%s&photo=%s' % (apiurl,telemethod,chat_id,decoded["entities"]["media"][0]["media_url_https"])  #imageurl
            telemethod = "sendMessage"
            urlm = '%s%s?chat_id=%s&text=%s' % (apiurl,telemethod,chat_id,decoded["entities"]["media"][0]["url"]) #messangeurl
            #偵測是否含有指定字
            if("月曜日のたわわ" in decoded['text'] and "その" in decoded['text'] and "RT" not in decoded['text']):
                print("Exist!!!")
                r = requests.get(urlm+' this week\'s tawawa')
                print(r.status_code)
                r = requests.get(urlphoto)
                print(r.status_code)

        except:
            print("No Photo RRRRRRRR")
            pass        
        return True
 
    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keyword: 'python'
    #users = []
    stream.filter(follow=[]) # filter source with twitter user id