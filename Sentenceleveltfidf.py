import xml.etree.ElementTree as ET
import numpy as np
import os

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


ps = PorterStemmer()
tree = ET.parse('articlesinXML/S002243751830416X.xml')

directory=('articlesinXML')
origtext=[]
author_highlights=[]
abst=[]
sentenceindex=[]
termfreq={}
sentence_score=[]

# for filename in os.listdir(directory):
#
#     if filename.endswith(".xml"):
#         print(filename)
#           tree = ET.parse(directory+"/"+filename)
for tag in tree.iter():
    if(tag.tag == '{http://purl.org/dc/elements/1.1/}description'):
        continue
    if(tag.tag == '{http://www.elsevier.com/xml/common/dtd}list-item'):
        continue
    if(tag.tag == '{http://www.elsevier.com/xml/xocs/dtd}normalized-srctitle'):
        continue
    if (tag.tag == '{http://www.elsevier.com/xml/xocs/dtd}normalized-article-title'):
        continue
    if (tag.tag == '{http://www.elsevier.com/xml/xocs/dtd}normalized-first-auth-surname'):
        continue
    if (tag.tag == '{http://www.elsevier.com/xml/xocs/dtd}normalized-first-auth-initial'):
        continue
    if (tag.tag == '{http://www.elsevier.com/xml/xocs/dtd}ref-normalized-surname'):
        continue
    if (tag.tag == '{http://www.elsevier.com/xml/xocs/dtd}ref-normalized-initial'):
        continue
    if (tag.tag == '{http://www.elsevier.com/xml/xocs/dtd}ref-normalized-srctitle'):
        continue
    if (tag.tag == '{http://www.elsevier.com/xml/xocs/dtd}ref-normalized-article-title'):
        continue
    if(tag.tag== '{http://www.elsevier.com/xml/xocs/dtd}articleinfo'):
        continue
    if(tag.tag == '{http://www.elsevier.com/xml/common/dtd}cross-refs'):
        continue
    if(tag.tag=='{http://www.elsevier.com/xml/common/dtd}textfn'):
        continue
    else:
        if (tag.text != None):
            if(len(tag.text)>75 and not (tag.text).startswith('https')):
                sentenceindex.append(tag.text)
                stopWords = set(stopwords.words('english'))
                tokenizer = RegexpTokenizer(r'\w+')
                words = tokenizer.tokenize(tag.text)
                wordsFiltered = []

                for w in words:
                    if w not in stopWords:
                        wordsFiltered.append(ps.stem(w))

                origtext.append(wordsFiltered)


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

        sentence_sc+=np.log(len(origtext)/docfreq[termf])*(termfreq[termf]/len(sentence))
    sentence_score.append(sentence_sc)



print(len(sentence_score))
top_5_idx = np.argsort(sentence_score)[-7:]
print(top_5_idx)
for ind in sorted(top_5_idx):
    print(sentenceindex[ind])
print(len(sentenceindex))






