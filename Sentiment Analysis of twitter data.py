from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from http.client import IncompleteRead
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey = "aNDL1BTm5lBmEXU3ovhb4iKgw"
csecret = "cenusIDGrRsNiMgIc43QwvJcrq3o4CxhwQYpYVw0GQI7IpyUIX"
atoken = "4800374677-662vzChysLY2TpRkDe3ALM0WWM0m04dwUCzArAZ"
asecret= "ejy3aQDQK5j6OB0g5EIhaJP0aeKikVC16wsc0HgzvOdzn"

class listener(StreamListener):

    def on_data(self,data):
  #      print("hi 1 more tweet", data)
        try:
            all_data = json.loads(data)
            tweet=all_data["text"]
            sentiment_value,confidence = s.sentiment(tweet)
            print(sentiment_value,confidence)

            if confidence*100>=80:
                output=open("C:/Users/dnema00/Documents/Projects/Adhoc/Blog/GPR Clustering/Twitter Clustering/twitter_mil_out.txt","a")
                output.write(sentiment_value)
                output.write('/n')
                output.close()
            return True
        except:
            return True 

    def on_error(self,status):
        print("error zala:",tweet,status)



auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)


while True:
    try:
        twitterStream = Stream(auth,listener())
        twitterStream.filter(track=["MIL","mother in law","Mother-In-Law","Mother", "Law"])
    except IncompleteRead:
        print("incompleteread")
        continue
