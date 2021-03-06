import xml.etree.ElementTree as ET
import csv
import os
# import pandas as pd
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
directory=('articlesinXML')
keyword_main={}
all_files = []
from nltk.stem import PorterStemmer

# ps=PorterStemmer()
for filename in os.listdir(directory):
    keywords = []
    if filename.endswith(".xml"):
#        print(filename)
        all_files.append(filename)
        tree = ET.parse(directory+"/"+filename)
        for tag in tree.iter():
            if(tag.tag == '{http://purl.org/dc/elements/1.1/}title'): # keywords
                #print(tag.text)
                stopWords = set(stopwords.words('English'))
                tokenizer = RegexpTokenizer(r'\w+')
                words = tokenizer.tokenize(tag.text)

                wordsFiltered = " "

                for w in words:
                    if w not in stopWords:
                        # wordsFiltered+=(w+" ")
                        keywords.append((w))
                #print(title)

        for tag in tree.iter():
            if(tag.tag == '{http://www.elsevier.com/xml/common/dtd}keyword'):  # get keywords
                    for t in tag:
                        if (t.tag == '{http://www.elsevier.com/xml/common/dtd}text'):
                            #print(t.text)
                            stopWords = set(stopwords.words('English'))
                            tokenizer = RegexpTokenizer(r'\w+')

                            words = tokenizer.tokenize(t.text)
                            #print(words)

                            # wordsFiltered = " "
                            for w in words:
                                if w not in stopWords:
                                    keywords.append((w))
                                    # keywords.append(wordsFiltered)
        keyword_main[filename]=(keywords)
# print(keyword_main)