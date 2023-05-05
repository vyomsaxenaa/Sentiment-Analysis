import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize,word_tokenize
import numpy as np
import re
from textblob import TextBlob
#Stemming
from nltk.stem.porter import PorterStemmer
port=PorterStemmer()

# Read Text file
data=open("data_file.txt","r")
text=data.read()

raw_data=text.split()
#print(raw_data)

#Convert to lower text
clean_text_1=[]
def to_lower_case(data):
    for words in data:
        clean_text_1.append(str.lower(words))
to_lower_case(raw_data)


"""TOKENIZATION"""

#Word tokenization
clean_text_2=[]
def tokenize(clean_text_1):
    for i in clean_text_1:
        word=word_tokenize(i)
        clean_text_2.append(word)
    return(clean_text_2)
tokenize(clean_text_1)

clean_text_3=[]
def clean(clean_text_2):
    for words in clean_text_2:
        clean=[]
        for w in words:
            res=re.sub(r"[^\w\s]","",w)
            if res!="":
                clean.append(res)
            clean_text_3.append(clean)
    return(clean_text_3)
clean(clean_text_2)

"""Stop Word Removal"""
nltk.download("stopwords")
from nltk.corpus import stopwords

clean_text_4=[]
def word_remove(clean_text_3):
    for words in clean_text_3:
        w=[]
        for word in words:
            if not word in stopwords.words("english"):
                if word !="":
                    w.append(word)
                    clean_text_4.append(w)
    return(clean_text_4)
word_remove(clean_text_3)

    

"""LEMITIZATION"""
from nltk.stem.wordnet import WordNetLemmatizer
wnet=WordNetLemmatizer()
import nltk
nltk.download("wordnet")

lem=[]
def lemmatize(clean_text_4):
    for words in clean_text_4:
        w=[]
        for word in words:
            w.append(wnet.lemmatize(word))
            lem.append(w)
    return(lem)
lemmatize(clean_text_4)



res_1=TextBlob(str(lem)).sentiment
print(res_1)

""" PERFORMING SENTIMENTAL ANALYSIS """
from textblob import TextBlob
def getSubjectivity(text):
    return TextBlob(str(lem)).sentiment.subjectivity
def getPolarity(clean_text_4):
    return TextBlob(str(lem)).sentiment.polarity

pred_1=getSubjectivity(lem)
pred_2=getPolarity(lem)
#Function to analyse the Text

def analysis(score):
    if score<0:
        return "Negative"
    elif score==0:
        return "Neutral"
    else:
        return "Positive"
predict=analysis(pred_2)
print(pred_1)
print(predict)





        
