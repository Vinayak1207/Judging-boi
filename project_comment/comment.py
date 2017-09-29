import nltk
from os.path import exists
from nltk.corpus import wordnet
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords




#funct to tokenize each sentence for analysis
def word_token(line):
    tokens=[]
    stopword=set(stopwords.words("english"))
    words = nltk.word_tokenize(line)

    for i in words:
        if i not in stopword:
            tokens.append(i)
    print (tokens)
    return tokens


#function for  comparision    of words with the positivity and negativity
def compare(tokens):
    review_collector = []
    avg=0
    for i in tokens:
        synonyms = wordnet.synsets(i)
        w1=wordnet.synset(synonyms[0].name())
        w2=wordnet.synset('good.n.01')
        review_collector.append(w1.wup_similarity(w2))

    for k in review_collector:
          avg += k
    avg /=len(review_collector)
    return avg




#comment = raw_input("Enter the comment to check weather it is positive in respect of movie")
comment =input("enter comment to check its positivity or negativity: ")

sent=nltk.sent_tokenize(comment)
#stopword=set(stopwords.words("english"))


analysis = []
j=0

while j<len(sent):
    #calling token function
    tokens=word_token(sent[j])
    analyse=compare(tokens)
    print("analyse is ",analyse)
    analysis.append(analyse)
    j += 1

final =0

for i in analysis:
    final = final+i

final /=len(analysis)
print (final)

if final > .55:
    print ("this is a positive comment with positivity percentage ",final*100)
else:
    print ("this is a negative comment with negativity percentage ",(1-final)*100)
