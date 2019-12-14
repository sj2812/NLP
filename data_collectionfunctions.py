
import xml.etree.ElementTree as ET
import csv
import os
import json
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
tree = ET.parse('articlesinXML/S002243751830416X.xml')

directory=('articlesinXML')
origtext=[]


sentenceindex=[]

abstractmain={}
highlightmain={}
contentmain={}
for filename in os.listdir(directory):
    author_highlights = " "
    abst = " "
    if filename.endswith(".xml"):
        print(filename)
        tree = ET.parse(directory+"/"+filename)
        for tag in tree.iter():
            if(tag.tag == '{http://purl.org/dc/elements/1.1/}description'):

                abst+=(tag.text)

                continue
            if(tag.tag == '{http://www.elsevier.com/xml/common/dtd}list-item'):
                continue
            else:
                if (tag.text != None):
                    sentenceindex.append(tag.text)
                    stopWords = set(stopwords.words('english'))
                    tokenizer = RegexpTokenizer(r'\w+')
                    words = tokenizer.tokenize(tag.text)
                    wordsFiltered = []

                    for w in words:
                        if w not in stopWords:
                            wordsFiltered.append(w)

                    origtext.append(wordsFiltered)
        print("length abstract")
        print((abst))

        for tag in tree.iter():
            if (tag.tag == '{http://www.elsevier.com/xml/common/dtd}abstract-sec'):
                for t in tag:
                    if(t.tag=='{http://www.elsevier.com/xml/common/dtd}simple-para'):

                        for tg in t:
                            if (tg.tag == '{http://www.elsevier.com/xml/common/dtd}list'):

                                for g in tg:
                                    if (g.tag == '{http://www.elsevier.com/xml/common/dtd}list-item'):

                                        for ti in g:
                                            if (ti.tag == '{http://www.elsevier.com/xml/common/dtd}para'):

                                                author_highlights+=(ti.text)
        print("lngth of highlights")
        print((author_highlights))
        abstractmain[filename]=(abst)
        highlightmain[filename]=(author_highlights)
        contentmain[filename]=(origtext)
        print(origtext)
        print(len(origtext))
        print(len(sentenceindex))

wm= csv.writer(open("abstract.csv", "w",encoding="utf-8"))
for key, val in abstractmain.items():
    wm.writerow([key, val])

w = csv.writer(open("content.csv", "w",encoding="utf-8"))
for key, val in contentmain.items():
    w.writerow([key, val])

w = csv.writer(open("highlights.csv", "w",encoding="utf-8"))
for key, val in highlightmain.items():
    w.writerow([key, val])




