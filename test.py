import demoji
import re
import nltk
from nltk.tokenize.casual import TweetTokenizer
import alias
""" from nltk.corpus import wordnet
import spacy

def get_key(val,my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key

sen='david dobrik should be cancelled..how could he do this to his friend. This is sickening🤢 and pathetic😠.This is painful😔'
#sen='ronaldo scored his 100th goal for juventus is such a short amount of time..crazy🤯'
#sen='whoa 😮 what the hell is that'
nlp = spacy.load('en_core_web_md')
sett=demoji.findall(sen)
toeken=nltk.TweetTokenizer()
token_Sent=toeken.tokenize(sen)
for emoji in sett:
    i=token_Sent.index(emoji)
    #print(token_Sent[i-1])
    prior=token_Sent[i-1]
    emoji_text=sett[emoji]
    emoji_text=re.sub('\s','-',emoji_text)
    url=f'https://emojipedia.org/{emoji_text}/'
    alises=alias.getaliases(url)
    temp=[]
    dict={}
    alises.append(emoji_text)
    for alis in alises:
        #alis=re.sub('\s','-',alis)
        data=prior+" "+alis
        tokens= nlp(data)
        token1, token2 = tokens[0], tokens[1]
        sim=token1.similarity(token2)
        temp.append(sim)
        dict[alis]=sim
        print(alis,sim)
    max_sim=max(temp)
    alis_elect=get_key(max_sim,dict)
    if(prior!=alis_elect):token_Sent[i]=alis_elect
sen=' '.join(token_Sent)
print(sen)

 """

alis='fire-engine'
alis=re.sub('-',' ',alis)
toeken=TweetTokenizer()
token_Sent=toeken.tokenize(alis)
if(token_Sent[1].lower()=='face'):token_Sent[1]=''
sen=' '.join(token_Sent)
print(sen)
