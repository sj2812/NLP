import xml.etree.ElementTree as ET
import glob
import os
import pandas as pd

tree = ET.parse('S002243751830416X.xml')
root = tree.getroot()
#print(root)

# for group in root:
#     for e in group:
#         #print(e.tag)
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
for coredata in tree.findall('{http://www.elsevier.com/xml/svapi/article/dtd}coredata'):
    print(coredata.find('{http://purl.org/dc/elements/1.1/}description').text)
    #coredata_arr.append(coredata.find('{http://purl.org/dc/elements/1.1/}description').text)
#print(tree.findall('{http://purl.org/dc/elements/1.1/}description'))


    # get other content
    for tag in tree.getiterator():
        if tag == '{http://purl.org/dc/elements/1.1/}description' :
            continue
        else:
            print(tag.text)

        #content_arr.append(tag.text)


    # get Author Highlights
    for originalText in tree.findall('{http://www.elsevier.com/xml/svapi/article/dtd}originalText'):
        for xcosDoc in originalText.findall('{http://www.elsevier.com/xml/xocs/dtd}doc'):
            for serialItem in xcosDoc.findall('{http://www.elsevier.com/xml/xocs/dtd}serial-item'):
                for article in serialItem.findall('{http://www.elsevier.com/xml/ja/dtd}article'):
                    for head in article.findall('{http://www.elsevier.com/xml/ja/dtd}head'):
                        for abstract in head.findall('{http://www.elsevier.com/xml/common/dtd}abstract'):
                            for abstractSec in abstract.findall('{http://www.elsevier.com/xml/common/dtd}abstract-sec'):
                                for simplePara in abstractSec.findall('{http://www.elsevier.com/xml/common/dtd}simple-para'):
                                    for listXML in simplePara.findall('{http://www.elsevier.com/xml/common/dtd}list'):
                                        for listItem in listXML.findall('{http://www.elsevier.com/xml/common/dtd}list-item'):
                                            for para in listItem.findall('{http://www.elsevier.com/xml/common/dtd}para'):
                                                print(para.text)
                                                #para_arr.append(para.text)
                                                #print(para_arr)
    # write to dataframe
    """
    :input : dataframe
    Creates dataframe
    :return : Dataframe
    """
    '''d = {'Filename': filename, 'Abstract' : coredata_arr, 'Author-Highlights' : para_arr, 'Other Content' : content_arr}
    data = pd.DataFrame.from_dict(d, orient='index')
    #print(data)
    Data_collection_csv = data.to_csv(index=False)
    print(Data_collection_csv)

"""for filename in glob.glob(os.path.join(path, "*.xml")):
    with open (filename,"r", encoding="utf-8") as open_file:
        #print(filename)
        content = open_file.read()
        #print(content)
        #file.write(content)
        with open(filename, 'r', encoding="utf-8") as input:
            for index, filename in enumerate(input):
                with open('filename{}.txt'.format(index), 'w',encoding="utf-8") as output:
                    output.write(content)"""


for file in os.listdir(path):
    if file.endswith('.xml') or file.endswith('.XML'):
        file_path = os.path.join(path, file)
        print(file_path)
        with open(file_path, encoding="utf-8") as fp:
            contents = fp.read()
            print(contents)


#Abstract
"""for originalText in tree.findall('{http://www.elsevier.com/xml/svapi/article/dtd}originalText'):
    for xcosDoc in originalText.findall('{http://www.elsevier.com/xml/xocs/dtd}doc'):
        for serialItem in xcosDoc.findall('{http://www.elsevier.com/xml/xocs/dtd}serial-item'):
            for article in serialItem.findall('{http://www.elsevier.com/xml/ja/dtd}article'):
                for head in article.findall('{http://www.elsevier.com/xml/ja/dtd}head'):
                    for abstract in head.findall('{http://www.elsevier.com/xml/common/dtd}abstract'):
                        for abstractSec in abstract.findall('{http://www.elsevier.com/xml/common/dtd}abstract-sec'):
                            for simplePara in abstractSec.findall('{http://www.elsevier.com/xml/common/dtd}simple-para'):
                                for listXML in simplePara.findall('{http://www.elsevier.com/xml/common/dtd}list'):
                                    for listItem in listXML.findall('{http://www.elsevier.com/xml/common/dtd}list-item'):
                                        for para in listItem.findall('{http://www.elsevier.com/xml/common/dtd}para'):
                                            print(para.text)
"""

'''
# def create_dataframe():
#     pass
#
# def write_to_dataframe():
#     """
#     :input : dataframe
#     Writes to dataframe
#     :return : dataframe
#     """
#     pass
#
# def save_to_csv()
#     """
#     :input: dataframe
#     Saves dataframe to csv
#     """
#     pass
#
#
# if __name__ == '__main__':
#     # path = "C:\\Users\\SANKET\\.PyCharmCE2019.3\\config\\scratches"
#     path = "D:\\TextSumm\\NLP-master\\NLP-master\\articlesinXML"
#     # "C:\Users\SANKET\.PyCharmCE2019.2\config\scratches"
#
#     filenames = glob.glob(os.path.join(path, "*.xml"))
#
#     # Create Dataframe
#
#     for filename in filenames:
#         print(filename)
#         with open(filename, 'r', encoding="utf-8") as content:
#             # print(content)
#             # all_content =content.read()
#             # print(all_content)
#
#             # Call the retrieving function
#             add_row()
#
# '''
