from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#import sentiments as project



#consumer key, consumer secret, access token, access secret.
ckey="*********" #generate consumer key in twitter
csecret="********"  #consumer secret would be provided with keyy in twitter
atoken="********" #generate access token
asecret="MhgPNciOCovQAjN7W0GQZ69OrKccBZbltDJgzgwjjkDoF"  # access tsecret here

class listener(StreamListener):

    def on_data(self, data):
        tweet = data.split(',"text":"')[1].split(',"')[0]
        print(tweet,"\n\n")
        return(True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["movie"])
