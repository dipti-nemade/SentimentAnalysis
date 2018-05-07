from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from http.client import IncompleteRead
import sentiment_mod as s
import csv

#consumer key, consumer secret, access token, access secret.
ckey = "aNDL1BTm5lBmEXU3ovhb4iKgw"
csecret = "cenusIDGrRsNiMgIc43QwvJcrq3o4CxhwQYpYVw0GQI7IpyUIX"
atoken = "4800374677-662vzChysLY2TpRkDe3ALM0WWM0m04dwUCzArAZ"
asecret= "ejy3aQDQK5j6OB0g5EIhaJP0aeKikVC16wsc0HgzvOdzn"

class listener(StreamListener):

    def on_data(self,data):

        try:
                
            result = json.loads(data)
            
            if type(result["geo"]) != type(None):
                #print(result["geo"])
                user = result["user"]["screen_name"]
                tweet = result["text"]
                latitude = result["geo"]["coordinates"][0]
                longitude = result["geo"]["coordinates"][1]
                print("lat:", latitude)
                sentiment_value,confidence = s.sentiment(tweet)
                row = [user,tweet,latitude,longitude,sentiment_value]
                row1 = [str(user),str(tweet),latitude,longitude,sentiment_value]
                print(row)
                
                with open("eggs.csv", "a") as csvfile:
                    spamwriter = csv.writer(csvfile)
                    spamwriter.writerow(row1)
                    spamwriter.close()
                return True
        except:
            return True
            print("error")

    def on_error(self,status):
        print("error za:",tweet,status)



auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)


while True:
    try:
        twitterStream = Stream(auth,listener())
        twitterStream.filter(track=["and"])
    except IncompleteRead:
        print("incompleteread")
        continue
