import re

def extractURLs(fileContent):
    urls = re.findall('\(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', fileContent.lower())

    for url in urls:
        print(url)
    return urls

myFile = open("ScienceDirect_citations_1575215179038.txt",encoding="utf8")
fileContent = myFile.read()
extractURLs(fileContent)