import xml.etree.ElementTree as ET
import csv
import os
# import pandas as pd
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
tree = ET.parse('articlesinXML/S002243751830416X.xml')

directory=('articlesinXML')
origtext=[]
author_highlights=[]
abst=[]
sentenceindex=[]

abstractmain={}
highlightmain={}
contentmain={}
for filename in os.listdir(directory):

    if filename.endswith(".xml"):
        print(filename)
        tree = ET.parse(directory+"/"+filename)
        for tag in tree.iter():
            if(tag.tag == '{http://purl.org/dc/elements/1.1/}description'):

                abst.append(tag.text)

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
        print(abst)

        for tag in tree.iter():
            if (tag.tag == '{http://www.elsevier.com/xml/common/dtd}list-item'):
                for t in tag:
                    if(t.tag=='{http://www.elsevier.com/xml/common/dtd}para'):

                        author_highlights.append(t.text)
        print(author_highlights)
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


'''
def add_row():
    """
    Takes the file as input and writes it to dataframe
    :input : filename, dataframe
    :return : dataframe
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    #print(tree.getiterator())
    coredata_arr = []
    content_arr = []
    para_arr = []
'''
    # Get abstract
# for coredata in tree.findall('{http://www.elsevier.com/xml/svapi/article/dtd}coredata'):
#     print(coredata.find('{http://purl.org/dc/elements/1.1/}description').text)
    #coredata_arr.append(coredata.find('{http://purl.org/dc/elements/1.1/}description').text)
#print(tree.findall('{http://purl.org/dc/elements/1.1/}description'))


    # get other content



    # print(origtext)
        # if tag.tag == '{http://www.elsevier.com/xml/svapi/article/dtd}coredata':
        #     continue
        #     # for coredata in tree.findall('{http://www.elsevier.com/xml/svapi/article/dtd}coredata'):
        #     #     print(coredata.find('{http://purl.org/dc/elements/1.1/}description'))
        #     #     for description in coredata:
        #     #         if(description.tag == '{http://purl.org/dc/elements/1.1/}description' ):
        #     #             continue
        #     #         else:
        #     #             origtext.append(description.text)
        # if tag.tag== '{http://www.elsevier.com/xml/svapi/article/dtd}originalText':
        #     for originalText in tree.findall('{http://www.elsevier.com/xml/svapi/article/dtd}originalText'):
        #         for xcosDoc in originalText.findall('{http://www.elsevier.com/xml/xocs/dtd}doc'):
        #             for serialItem in xcosDoc.findall('{http://www.elsevier.com/xml/xocs/dtd}serial-item'):
        #                 for article in serialItem.findall('{http://www.elsevier.com/xml/ja/dtd}article'):
        #                     for head in article.findall('{http://www.elsevier.com/xml/ja/dtd}head'):
        #                         for abstract in head.findall('{http://www.elsevier.com/xml/common/dtd}abstract'):
        #                             if(abstract.tag == '{http://www.elsevier.com/xml/common/dtd}abstract-sec'):
        #                                 continue
        #                             else:
        #                                 origtext.append(head.text)
        #
        #  else:
        #      origtext.append(tag.text)


        #content_arr.append(tag.text)


    # get Author Highlights
    # for originalText in tree.findall('{http://www.elsevier.com/xml/svapi/article/dtd}originalText'):
    #     for xcosDoc in originalText.findall('{http://www.elsevier.com/xml/xocs/dtd}doc'):
    #         for serialItem in xcosDoc.findall('{http://www.elsevier.com/xml/xocs/dtd}serial-item'):
    #             for article in serialItem.findall('{http://www.elsevier.com/xml/ja/dtd}article'):
    #                 for head in article.findall('{http://www.elsevier.com/xml/ja/dtd}head'):
    #                     for abstract in head.findall('{http://www.elsevier.com/xml/common/dtd}abstract'):
    #                         for abstractSec in abstract.findall('{http://www.elsevier.com/xml/common/dtd}abstract-sec'):
    #                             for simplePara in abstractSec.findall('{http://www.elsevier.com/xml/common/dtd}simple-para'):
    #                                 for listXML in simplePara.findall('{http://www.elsevier.com/xml/common/dtd}list'):
    #                                     for listItem in listXML.findall('{http://www.elsevier.com/xml/common/dtd}list-item'):
    #                                         for para in listItem.findall('{http://www.elsevier.com/xml/common/dtd}para'):
    #                                             print(para.text)
                                                #para_arr.append(para.text)
                                                #print(para_arr)
    # write to dataframe
#     """
#     :input : dataframe
#     Creates dataframe
#     :return : Dataframe
#     """
#     '''d = {'Filename': filename, 'Abstract' : coredata_arr, 'Author-Highlights' : para_arr, 'Other Content' : content_arr}
#     data = pd.DataFrame.from_dict(d, orient='index')
#     #print(data)
#     Data_collection_csv = data.to_csv(index=False)
#     print(Data_collection_csv)
#
# """for filename in glob.glob(os.path.join(path, "*.xml")):
#     with open (filename,"r", encoding="utf-8") as open_file:
#         #print(filename)
#         content = open_file.read()
#         #print(content)
#         #file.write(content)
#         with open(filename, 'r', encoding="utf-8") as input:
#             for index, filename in enumerate(input):
#                 with open('filename{}.txt'.format(index), 'w',encoding="utf-8") as output:
#                     output.write(content)"""
#
#
# for file in os.listdir(path):
#     if file.endswith('.xml') or file.endswith('.XML'):
#         file_path = os.path.join(path, file)
#         print(file_path)
#         with open(file_path, encoding="utf-8") as fp:
#             contents = fp.read()
#             print(contents)
#
#
# #Abstract
# """for originalText in tree.findall('{http://www.elsevier.com/xml/svapi/article/dtd}originalText'):
#     for xcosDoc in originalText.findall('{http://www.elsevier.com/xml/xocs/dtd}doc'):
#         for serialItem in xcosDoc.findall('{http://www.elsevier.com/xml/xocs/dtd}serial-item'):
#             for article in serialItem.findall('{http://www.elsevier.com/xml/ja/dtd}article'):
#                 for head in article.findall('{http://www.elsevier.com/xml/ja/dtd}head'):
#                     for abstract in head.findall('{http://www.elsevier.com/xml/common/dtd}abstract'):
#                         for abstractSec in abstract.findall('{http://www.elsevier.com/xml/common/dtd}abstract-sec'):
#                             for simplePara in abstractSec.findall('{http://www.elsevier.com/xml/common/dtd}simple-para'):
#                                 for listXML in simplePara.findall('{http://www.elsevier.com/xml/common/dtd}list'):
#                                     for listItem in listXML.findall('{http://www.elsevier.com/xml/common/dtd}list-item'):
#                                         for para in listItem.findall('{http://www.elsevier.com/xml/common/dtd}para'):
#                                             print(para.text)
# """
#
#
# # def create_dataframe():
# #     pass
# #
# # def write_to_dataframe():
# #     """
# #     :input : dataframe
# #     Writes to dataframe
# #     :return : dataframe
# #     """
# #     pass
# #
# # def save_to_csv()
# #     """
# #     :input: dataframe
# #     Saves dataframe to csv
# #     """
# #     pass
# #
# #
# # if __name__ == '__main__':
# #     # path = "C:\\Users\\SANKET\\.PyCharmCE2019.3\\config\\scratches"
# #     path = "D:\\TextSumm\\NLP-master\\NLP-master\\articlesinXML"
# #     # "C:\Users\SANKET\.PyCharmCE2019.2\config\scratches"
# #
# #     filenames = glob.glob(os.path.join(path, "*.xml"))
# #
# #     # Create Dataframe
# #
# #     for filename in filenames:
# #         print(filename)
# #         with open(filename, 'r', encoding="utf-8") as content:
# #             # print(content)
# #             # all_content =content.read()
# #             # print(all_content)
# #
# #             # Call the retrieving function
# #             add_row()
# #
# # '''
