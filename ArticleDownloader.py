
import urllib.request
import shutil

APIKEY='f202e79f5f94584f509bf748d90fbb8b'
listurls = open('listurls.txt', "r")
listPII = []
for url in listurls:
    if url.startswith("(http://www.sciencedirect.com"):
        pii = url.replace("(http://www.sciencedirect.com/science/article/pii/", "").replace(")", "").replace("\n", "")
        if not pii in listPII:
            listPII.append(pii)
print(listPII)

for pii in listPII:
    piir = "http://api.elsevier.com/content/article/PII:" + pii + "?httpAccept=text/xml&APIKey=" + APIKEY
    local_filename, headers = urllib.request.urlretrieve(piir)
    shutil.copy(local_filename, "articlesinXML/" +pii + ".xml")