
import xml.etree.ElementTree as ET
import csv
import os
import json
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
tree = ET.parse('articlesinXML/S002243751830416X.xml')
from nltk.stem import PorterStemmer
directory=('articlesinXML')
# ps=PorterStemmer()


sentenceindex=[]
all_files = []
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

abstractmain={}

highlightmain={}

contentmain={}

stopWords = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')
for filename in os.listdir(directory):
    author_highlights = " "
    abst = " "
    origtext = " "
    if filename.endswith(".xml"):
        #print(filename)
        all_files.append(filename)
        tree = ET.parse(directory+"/"+filename)
        for tag in tree.iter():
            if(tag.tag == '{http://purl.org/dc/elements/1.1/}description'):
                words = tokenizer.tokenize(tag.text)
                wordsFiltered = " "
                # wordsFiltered =[]
                for w in words:
                    if w not in stopWords:
                        # wordsFiltered.append(w)
                        wordsFiltered += ((w) + " ")
                abst+=str(wordsFiltered)

                continue
            if(tag.tag in notimptags):

                continue
            else:
                if (tag.text != None):
                    sentenceindex.append(tag.text)

                    words = tokenizer.tokenize(tag.text)
                    wordsFiltered = " "
                    #wordsFiltered =[]
                    for w in words:
                        if w not in stopWords:
                            #wordsFiltered.append(w)
                            wordsFiltered +=((w) +" ")
                    origtext +=str(wordsFiltered)
                    #content=origtext.join(wordsFiltered)
                    # print(origtext)

        #print("length abstract")
        #print((abst))

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
                                                words = tokenizer.tokenize(ti.text)
                                                wordsFiltered = " "
                                                # wordsFiltered =[]
                                                for w in words:
                                                    if w not in stopWords:
                                                        # wordsFiltered.append(w)
                                                        wordsFiltered += ((w) + " ")
                                                author_highlights += str(wordsFiltered)

        #print("lngth of highlights")
        #print((origtext))
        abstractmain[filename]=(abst)
        highlightmain[filename]=(author_highlights)
        contentmain[filename]=(origtext)
        #print(origtext)
        #print(len(origtext))
        #print(len(sentenceindex))
        #print(highlightmain)
wm= csv.writer(open("abstract.csv", "w",encoding="utf-8"))
for key, val in abstractmain.items():
    wm.writerow([key, val])

w = csv.writer(open("content.csv", "w",encoding="utf-8"))
for key, val in contentmain.items():
    w.writerow([key, val])

w = csv.writer(open("highlights.csv", "w",encoding="utf-8"))
for key, val in highlightmain.items():
    w.writerow([key, val])




