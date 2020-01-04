
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

import data_collectionfunctions as collect
import random
# ps = PorterStemmer()
tree = ET.parse('articlesinXML/S002243751830416X.xml')

directory=('articlesinXML')

author_highlights=[]
abst=[]


summarymain={}

notimptags=[ '{http://purl.org/dc/elements/1.1/}description','{http://www.elsevier.com/xml/common/dtd}list-item','{http://www.elsevier.com/xml/xocs/dtd}normalized-srctitle',
             '{http://www.elsevier.com/xml/xocs/dtd}normalized-article-title','{http://www.elsevier.com/xml/xocs/dtd}normalized-first-auth-surname',
             '{http://www.elsevier.com/xml/xocs/dtd}normalized-first-auth-initial','{http://www.elsevier.com/xml/xocs/dtd}ref-normalized-surname',
             '{http://www.elsevier.com/xml/xocs/dtd}ref-normalized-initial','{http://www.elsevier.com/xml/xocs/dtd}ref-normalized-srctitle','{http://www.elsevier.com/xml/xocs/dtd}ref-normalized-article-title',
             '{http://www.elsevier.com/xml/xocs/dtd}articleinfo','{http://www.elsevier.com/xml/common/dtd}cross-refs','{http://www.elsevier.com/xml/common/dtd}textfn','{http://purl.org/dc/elements/1.1/}creator',
             '{http://prismstandard.org/namespaces/basic/2.0/}url','{http://prismstandard.org/namespaces/basic/2.0/}publicationName','{http://www.elsevier.com/xml/svapi/article/dtd}openaccessArticle',
             '{http://prismstandard.org/namespaces/basic/2.0/}url','{http://purl.org/dc/elements/1.1/}identifier','{http://www.elsevier.com/xml/svapi/article/dtd}eid','{http://prismstandard.org/namespaces/basic/2.0/}doi',
            '{http://prismstandard.org/namespaces/basic/2.0/}publicationName','{http://prismstandard.org/namespaces/basic/2.0/}aggregationType','{http://prismstandard.org/namespaces/basic/2.0/}coverDate',
            '{http://prismstandard.org/namespaces/basic/2.0/}coverDisplayDate','{http://prismstandard.org/namespaces/basic/2.0/}copyright','{http://prismstandard.org/namespaces/basic/2.0/}publisher',
            '{http://purl.org/dc/elements/1.1/}creator','{http://www.elsevier.com/xml/svapi/article/dtd}openaccess','{http://www.elsevier.com/xml/svapi/article/dtd}openaccessArticle',
            '{http://www.elsevier.com/xml/svapi/article/dtd}openaccessType','{http://www.elsevier.com/xml/svapi/article/dtd}openArchiveArticle','{http://www.elsevier.com/xml/svapi/article/dtd}openaccessSponsorName',
            '{http://www.elsevier.com/xml/svapi/article/dtd}openaccessSponsorType','{http://www.elsevier.com/xml/svapi/article/dtd}openaccessUserLicense','{http://www.elsevier.com/xml/svapi/article/dtd}scopus-id',
            '{http://www.elsevier.com/xml/svapi/article/dtd}scopus-eid','{http://www.elsevier.com/xml/svapi/article/dtd}link','{http://www.elsevier.com/xml/xocs/dtd}content-family',
            '{http://www.elsevier.com/xml/xocs/dtd}content-type','{http://www.elsevier.com/xml/xocs/dtd}cid','{http://www.elsevier.com/xml/xocs/dtd}ssids','{http://www.elsevier.com/xml/xocs/dtd}ssid',
            '{http://www.elsevier.com/xml/xocs/dtd}ssid','{http://www.elsevier.com/xml/xocs/dtd}ssid','{http://www.elsevier.com/xml/xocs/dtd}ssid','{http://www.elsevier.com/xml/xocs/dtd}ssid',
            '{http://www.elsevier.com/xml/xocs/dtd}ssid','{http://www.elsevier.com/xml/xocs/dtd}ssid','{http://www.elsevier.com/xml/xocs/dtd}srctitle','{http://www.elsevier.com/xml/xocs/dtd}normalized-srctitle',
            '{http://www.elsevier.com/xml/xocs/dtd}orig-load-date','{http://www.elsevier.com/xml/xocs/dtd}available-online-date','{http://www.elsevier.com/xml/xocs/dtd}vor-load-date',
            '{http://www.elsevier.com/xml/xocs/dtd}vor-available-online-date','{http://www.elsevier.com/xml/xocs/dtd}ew-transaction-id','{http://www.elsevier.com/xml/xocs/dtd}eid',
            '{http://www.elsevier.com/xml/xocs/dtd}pii-formatted','{http://www.elsevier.com/xml/xocs/dtd}pii-unformatted','{http://www.elsevier.com/xml/xocs/dtd}doi',
            '{http://www.elsevier.com/xml/xocs/dtd}item-stage','{http://www.elsevier.com/xml/xocs/dtd}item-version-number','{http://www.elsevier.com/xml/xocs/dtd}item-weight',
            '{http://www.elsevier.com/xml/xocs/dtd}hub-eid','{http://www.elsevier.com/xml/xocs/dtd}timestamp','{http://www.elsevier.com/xml/xocs/dtd}dco',
            '{http://www.elsevier.com/xml/xocs/dtd}tomb','{http://www.elsevier.com/xml/xocs/dtd}date-search-begin','{http://www.elsevier.com/xml/xocs/dtd}date-search-end',
            '{http://www.elsevier.com/xml/xocs/dtd}year-nav','{http://www.elsevier.com/xml/xocs/dtd}indexeddate','{http://www.elsevier.com/xml/xocs/dtd}copyright-line',
            '{http://www.elsevier.com/xml/xocs/dtd}oa-article-status','{http://www.elsevier.com/xml/xocs/dtd}oa-access-effective-date','{http://www.elsevier.com/xml/xocs/dtd}oa-sponsor'
            '{http://www.elsevier.com/xml/xocs/dtd}oa-sponsor-type','{http://www.elsevier.com/xml/xocs/dtd}oa-user-license','{http://www.elsevier.com/xml/xocs/dtd}ucs-locator',
            '{http://www.elsevier.com/xml/xocs/dtd}ucs-locator','{http://www.elsevier.com/xml/xocs/dtd}filename','{http://www.elsevier.com/xml/xocs/dtd}extension',
            '{http://www.elsevier.com/xml/common/dtd}copyright','{http://www.elsevier.com/xml/common/dtd}entry','{http://www.elsevier.com/xml/common/dtd}given-name',
            '{http://www.elsevier.com/xml/common/dtd}cross-ref','{http://www.elsevier.com/xml/common/dtd}sup']

lst= collect.validfiles


for filename in os.listdir(directory):
    summary = ""
    sentenceindex = []
    origtext = []
    termfreq = {}
    sentence_score = []
    if filename in lst:
        if filename.endswith(".xml") :
            if(filename=="S0197455618301540.xml"):
                print(filename)
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
                                        if w not in stopWords:
                                            wordsFiltered.append((w))

                                    origtext.append(wordsFiltered)
            print(sentenceindex)
            # print(origtext)
                # abstractmain[filename]=(abst)
                # highlightmain[filename]=(author_highlights)
                # contentmain[filename]=(origtext)

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
                    if(termf in keyword_main):
                        w=2
                    else:
                        w=1
                    sentence_sc+=np.log(len(origtext)/docfreq[termf])*(termfreq[termf]/len(sentence))*w
                sentence_score.append(sentence_sc)



            # print(normalize(np.reshape( sentence_score,[-1,1]),norm='l2',axis=0))
            sentence_Score=np.array(sentence_score)
            mainscore=(np.interp(sentence_Score, (sentence_Score.min(), sentence_Score.max()), (0, 1)))
            # top_5_idx = np.argwhere(mainscore[0:int(len(mainscore)/3)]>0.74)

            # newarr=mainscore[(int(len(mainscore) / 3) * 2) + 1:len(mainscore) - 1]
            # top_2_idx = np.argwhere(mainscore[(int(len(mainscore) / 3) * 2) + 1:len(mainscore) - 1] > 0.74)
            top_5_idx = np.argwhere(mainscore[0:int(len(mainscore) / 3)] > 0.74)

            if(len(top_5_idx)==0):
                top_5_idx = np.argwhere(mainscore[0:int(len(mainscore) / 3)] > 0.5)
                if (len(top_5_idx) == 0):
                    top_5_idx = np.argwhere(mainscore[0:int(len(mainscore) / 3)] > 0.4)
            if (len(top_5_idx) > 5):
                top_5_idx = random.sample(list(top_5_idx),5)
            for ind in sorted(top_5_idx):
                for i in ind:
                    summary+=(sentenceindex[i])+". "
            top_5_idx = np.argwhere(mainscore[int(len(mainscore) / 3)+1:int(len(mainscore) / 3)*2] > 0.74)
            if (len(top_5_idx) == 0):
                top_5_idx = np.argwhere(mainscore[int(len(mainscore) / 3)+1:int(len(mainscore) / 3)*2] > 0.5)
                if (len(top_5_idx) == 0):
                    top_5_idx = np.argwhere(mainscore[int(len(mainscore) / 3)+1:int(len(mainscore) / 3)*2] > 0.4)
            if (len(top_5_idx) > 10):
                top_5_idx = random.sample(list(top_5_idx),10)
            for ind in sorted(top_5_idx):
                for i in ind:
                    summary += (sentenceindex[i+int(len(mainscore) / 3)])+". "
            top_5_idx = np.argwhere(mainscore[(int(len(mainscore) / 3) * 2)+1:len(mainscore)-1] > 0.74)
            if (len(top_5_idx) == 0):
                top_5_idx = np.argwhere(mainscore[(int(len(mainscore) / 3) * 2)+1:len(mainscore)-1] > 0.5)
                if (len(top_5_idx) == 0):
                    top_5_idx = np.argwhere(mainscore[(int(len(mainscore) / 3) * 2)+1:len(mainscore)-1] > 0.4)

            if (len(top_5_idx) > 5):
                top_5_idx = random.sample(list(top_5_idx),5)
            for ind in sorted(top_5_idx):
                for i in ind:
                    i=i+(int(len(mainscore) / 3) * 2)
                    summary += (sentenceindex[i])+". "
            print(len(sentenceindex))
            summarymain[filename]=summary


w = csv.writer(open("summarymain.csv", "w", encoding="utf-8"))
for key, val in summarymain.items():
    w.writerow([key, val])





