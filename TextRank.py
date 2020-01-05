import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
import os
import nltk
import networkx as nx
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import data_collectionfunctions as collect
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt') # one time execution
import re
col_Names=["Filename", "Content"]
content_df= pd.read_csv("content.csv", encoding='utf-8',names=col_Names)
#print(content_df)
clean_content_df = content_df.dropna()
#print(clean_content_df)

directory=('articlesinXML')
notimptags=collect.notimptags
lst= collect.validfiles

sentences =[]

for filename in os.listdir(directory):
    sentence_index=[]
    mainscore=[]
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
                                    sentence_index.append(s)
    #print(sentence_index)
            #
            # for s in clean_content_df['Content']:
            #     sentences.append(sent_tokenize(s))
            #     sentences = [y for x in sentences for y in x] # flatten list
            #     print(sentences[:5])

    # Extract word vectors
    word_embeddings = {}
    f = open('glove.6B.100d.txt', encoding='utf-8')
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        word_embeddings[word] = coefs
    f.close()
    len (word_embeddings)

    # remove punctuations, numbers and special characters
    clean_sentences = pd.Series(sentence_index).astype(str).replace("[^a-zA-Z]", " ")

    # make alphabets lowercase
    clean_sentences = [s.lower() for s in clean_sentences]


    stop_words = stopwords.words('english')
    # function to remove stopwords
    def remove_stopwords(sent_new):
        sent_new = " ".join([i for i in sent_new if i not in stop_words])
        return sent_new

    # remove stopwords from the sentences
    clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]
    #print(clean_sentences)

    #vector representation of sentences
    word_embeddings = {}
    f = open('glove.6B.100d.txt', encoding='utf-8')
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        word_embeddings[word] = coefs
    f.close()

    #create vectors for sentences
    sentence_vectors = []
    for i in clean_sentences:
        if len(i) != 0:
            v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()]) / (len(i.split()) + 0.001)
        else:
            v = np.zeros((100,))
        sentence_vectors.append(v)

    #create similarity matrix
    sim_mat = np.zeros([len(sentence_index), len(sentence_index)])
    for i in range(len(sentence_index)):
        for j in range(len(sentence_index)):
            if i != j:
                sim_mat[i][j] = \
                cosine_similarity(sentence_vectors[i].reshape(1, 100), sentence_vectors[j].reshape(1, 100))[0, 0]

    #Apply pagerank algorithm
    nx_graph = nx.from_numpy_array(sim_mat)
    scores = nx.pagerank(nx_graph)
    mainscore=list(scores.values())
    print(mainscore)
    # ranked_sentences = (((scores[i], s) )
    # for i, s in enumerate(sentence_index):
    #     print(ranked_sentences)
    # Extract top 10 sentences as the summary
    # for i in range(10):
    #     print(ranked_sentences[i][2])


