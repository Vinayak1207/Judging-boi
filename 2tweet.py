from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sentiments as project
import time



#consumer key, consumer secret, access token, access secret.
ckey="rG2yJRKoXhLTOUjZhuZDuZhMT"
csecret="mkMKPLfMBOBqiKvXWYkEUsddvEQL2ZdDAmoGVXIkfGXUPC1bDw"
atoken="1289132556-iegjIbCCamu28NyytsQLYgRhMcUC1eTR9J4LNhB"
asecret="MhgPNciOCovQAjN7W0GQZ69OrKccBZbltDJgzgwjjkDoF"

class listener(StreamListener):

    def on_data(self, data):
        tweet = data.split(',"text":"')[1].split(',\"')[0]
        save=str(time.time()) +'::'+tweet
        savefile= open("twiter _response/tweets_analysis.txt",'a')
        savefile.write(save)
        savefile.write(str(project.sentiment_classify(tweet)))
        savefile.write(str(project.sentiment_confi(tweet)))
        savefile.write('\n\n')
        savefile.close()
        print(tweet,project.sentiment(tweet),"\n\n")
        return(True)


    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["UFC"])
