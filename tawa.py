#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import requests

#Variables that contains the user credentials to access Twitter API
access_token = "518677431-BZbNvSIucO6MTlwWzRX1HpP0KNwx9vx4fp8TWUeg"
access_token_secret = "ZHf1R0qR9hc7WXlARRKbliX2xNkReNGyGbqggha0jpn64"
consumer_key = "iHpVyDSlGHjz7RZQ6CyA7xezq"
consumer_secret = "oJc7xKpRWCkjT5FhrG764CHYGFo9fzeV59PXVooGQN63XP6NiH"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        decoded = json.loads(data)
        print(json.dumps(decoded,sort_keys=True))
        print(decoded['text'].encode('utf-8', 'ignore'),
              decoded['text'],
              type(decoded['text'])
              )
        #chat_id = "-1001193629428" #KAI
        chat_id = "-1001344081949" #TestCh
        apiurl = 'https://api.telegram.org/bot589972373:AAGPwdPXCnbMKj8rxJEZQQiFCZUcgyZMjew/'
        


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
    #users = [518677431]
    stream.filter(follow=['993160436001292288', '518677431', '93332575'])