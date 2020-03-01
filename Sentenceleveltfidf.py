
import xml.etree.ElementTree as ET
import numpy as np
import os
import csv
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from keywords_title import keyword_main
import pandas as pd
import data_collectionfunctions as collect
import rouge
import random
import TextRank as tr
# ps = PorterStemmer()
tree = ET.parse('articlesinXML/S002243751830416X.xml')

directory=('articlesinXML')

author_highlights=[]
abst=[]

evaluator = rouge.Rouge(metrics=['rouge-l'])
summarymain={}

notimptags=collect.notimptags
lst= collect.validfiles

col_Names=["Filename", "Highlight"]
highlights_df = collect.highlightnopre

def appendInSingleArray(arr,indexSent):
    for elem in arr:
        indexSent.append(elem)
    return indexSent

def getTopindexes(mainscore,start,end,number):
    top_5_idx = np.argwhere(mainscore[start:end] > 0.74)

    if (len(top_5_idx) == 0):
        top_5_idx = np.argwhere(mainscore[0:int(len(mainscore) / 3)] > 0.5)
        if (len(top_5_idx) == 0):
            top_5_idx = np.argwhere(mainscore[0:int(len(mainscore) / 3)] > 0.4)
    if (len(top_5_idx) > number):
        top_5_idx = random.sample(list(top_5_idx), number)
    return top_5_idx

def getSummary(mainscore, sentenceindex):
    summary = ""

    # top_5_idx = np.argwhere(mainscore[0:int(len(mainscore)/3)]>0.74)

    # newarr=mainscore[(int(len(mainscore) / 3) * 2) + 1:len(mainscore) - 1]
    # top_2_idx = np.argwhere(mainscore[(int(len(mainscore) / 3) * 2) + 1:len(mainscore) - 1] > 0.74)

    for ind in sorted(getTopindexes(mainscore,0,int(len(mainscore)/3),5)):
        for i in ind:
            summary += (sentenceindex[i]) + ". "
    for ind in sorted(getTopindexes(mainscore,int(len(mainscore) / 3) + 1,int(len(mainscore) / 3) * 2,10)):
        for i in ind:
            summary += (sentenceindex[i + int(len(mainscore) / 3)]) + ". "
    for ind in sorted(getTopindexes(mainscore,(int(len(mainscore) / 3) * 2) + 1,len(mainscore) - 1,5)):
        for i in ind:
            i = i + (int(len(mainscore) / 3) * 2)
            summary += (sentenceindex[i]) + ". "
    return summary

HighlightPointer=0
HighlightMainMoreLength={}
TextRanksDict=tr.textrank_s()
for filename in os.listdir(directory):
    HighlightSentInd=[]
    sentenceindex = []
    origtext = []
    termfreq = {}
    sentence_score = []
    if filename in lst:
        if filename.endswith(".xml") :
            tree = ET.parse(directory+"/"+filename)
            for tag in tree.iter():
                if(tag.tag in notimptags):
                    continue

                else:
                    if (tag.text != None):
                        if(len(tag.text)>60 and not (tag.text).startswith('https')):
                            stringtext=str(tag.text)
                            for s in stringtext.split(sep='.'):
                                if(len(s)>50):
                                    sentenceindex.append(s)
                                    stopWords = set(stopwords.words('english'))
                                    tokenizer = RegexpTokenizer(r'\w+')
                                    words = tokenizer.tokenize(s)
                                    wordsFiltered = []

                                    for w in words:
                                        w = str(w).lower()
                                        if w not in stopWords:
                                            wordsFiltered.append((w))

                                    origtext.append(wordsFiltered)
            print(sentenceindex)

            highlights=highlights_df.get(filename)
            print(HighlightPointer)
                # highlights_df.loc[highlights_df["Filename"] == filename, "Highlight"]
            HighlightPointer=HighlightPointer+1

            highlightmain = []
            highlightscore=[]
            if(len(highlights)>0):
                for highlight in str(highlights).split(sep='.'):
                    if((highlight!=' ' )& (highlight!='')):
                        highlightindex = []
                        for sent in sentenceindex:

                            eval=evaluator.get_scores(sent,highlight)

                            highlightindex.append(eval[0].get('rouge-l').get('f'))
                        highlightmain.append(highlightindex)
            else:
                print("Hii")
            # highlightscore.append(highlightmain)
            indices=[]
            for highlightPerSent in highlightmain:

                indices=(np.argsort(highlightPerSent)[-5:])
                HighlightSentInd=appendInSingleArray(indices,HighlightSentInd)
            print(np.unique(HighlightSentInd))
            if(len(np.unique(HighlightSentInd))>10):
                mainInd=np.random.choice(np.unique(HighlightSentInd),10)
            else:
                mainInd=np.unique(HighlightSentInd)
            HighlightSummInter=highlights
            for ind in mainInd:
                HighlightSummInter+=sentenceindex[ind]+"."

            HighlightMainMoreLength[filename]=HighlightSummInter
            docfreq={}



            for sentence in origtext:
                sentence_sc = 0
                unique, counts = np.unique(sentence, return_counts=True)

                termfreq=(dict(zip(unique, counts)))
                for termf in termfreq:
                    count = 0
                    for elem in origtext:
                        if(termf in elem ):
                            count=count+1
                    docfreq[termf]=count
                for termf in termfreq:
                    if(termf in keyword_main[filename]):
                        w=1.2
                    else:
                        w=1
                    sentence_sc+=np.log(len(origtext)/docfreq[termf])*(termfreq[termf]/len(sentence))*w
                sentence_score.append(sentence_sc)
                textRank_sentScore=TextRanksDict.get(filename)
            sentence_Score=np.array(sentence_score)+np.array(textRank_sentScore)
            mainscore = (np.interp(sentence_Score, (sentence_Score.min(), sentence_Score.max()), (0, 1)))
            print(len(sentenceindex))
            summarymain[filename]=getSummary(mainscore,sentenceindex)


w = csv.writer(open("summarymain.csv", "w", encoding="utf-8"))
for key, val in summarymain.items():
    w.writerow([key, val])

w = csv.writer(open("HighlightmainMorelength.csv", "w", encoding="utf-8"))
for key, val in HighlightMainMoreLength.items():
    w.writerow([key, val])




