import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import pandas as pd
import os
# from data_collectionfunctions import all_files
import csv
import numpy as np
directory=('articlesinXML')
all_files=[]
for filename in os.listdir(directory):
    author_highlights = " "
    abst = " "
    origtext = " "
    if filename.endswith(".xml"):
        #print(filename)
        all_files.append(filename)
#generated_summary_df = pd.read_csv("summarymain.csv")
#print(generated_summary_df)

#print(contentmain)
#read abstract csv and convert it to a dataframe
col_Names=["Filename", "Abstract"]
abstract_df = pd.read_csv("abstract.csv",encoding='utf-8',names=col_Names)
#print(abstract_df)
#abstract_df.head()
clean_abstract_df = abstract_df.dropna()
#print(clean_abstract_df)

#read highlights csv and convert it to a dataframe
col_Names=["Filename", "Highlight"]
highlights_df = pd.read_csv("highlights.csv",encoding='utf-8',names=col_Names)
#print(highlights_df)
clean_highlights_df = highlights_df.dropna()
#print(clean_highlights_df)

#Apply tfidf vectorizer and kmeans on abstract
vectorizer = TfidfVectorizer()
vectorized_abst= vectorizer.fit_transform(clean_abstract_df["Abstract"])
#print(vectorized_abst)
#print(vectorized_abst)
terms = (vectorizer.get_feature_names())
#print(terms)
#Apply kmeans on abstract
kmeans_abstract = KMeans(n_clusters=6, random_state=300).fit(vectorized_abst)
labels = kmeans_abstract.labels_
print(len(labels))
labelnp=list(labels)
abstract_array=[]
# array1 = [i for i, x in enumerate(labelnp) if x == 1]
for j in range(6):
     abstract_array.append([all_files[i] for i, x in enumerate(labelnp) if x == j])
print("abstractclusters")
print(abstract_array)
#print(labels)
# clean_abstract_df['cluster assignment'] = labels
# clean_abstract_df.head()
# for i,label in enumerate(labels):
#      abstract_cluster_assignment = (label, all_files[i])
     #print(abstract_cluster_assignment)
#Apply dbscan on abstract(yet to do)
# clustering = DBSCAN(eps=3).fit(vectorized_abst) #apply dbscan
# dbscan_abstract_clusters = clustering.labels_
#print(dbscan_abstract_clusters)
# hac_clustering = AgglomerativeClustering(affinity='euclidean', linkage='ward', n_clusters=6).fit(vectorized_abst)
# print(hac_clustering.labels_)

#Apply tfidf vectorizer and kmeans on Highlights
vectorizer = TfidfVectorizer()
clean_highlights_df['Highlight']=clean_highlights_df['Highlight'].replace(' ', np.nan)
clean=clean_highlights_df.dropna(axis=0,subset=["Highlight"])

vectorized_highlights= vectorizer.fit_transform(clean["Highlight"])
kmeans_highlights = KMeans(n_clusters=6).fit(vectorized_highlights) #apply kmeans
#print(kmeans_highlights.labels_)
highlights_labels = kmeans_highlights.labels_
labelnp=list(highlights_labels)
print(len(highlights_labels))
highlights_array=[]
# array1 = [i for i, x in enumerate(labelnp) if x == 1]
for j in range(6):
     highlights_array.append([all_files[i] for i, x in enumerate(labelnp) if x == j])
print("highlightclusters")
print((highlights_array))
# for i,label in enumerate(highlights_labels):
#      highlights_cluster_assignment = (label, all_files[i])
     #print(highlights_cluster_assignment)
#Apply dbscan on highlights(yet to do)
# clustering = DBSCAN(eps=3).fit(vectorized_highlights)#apply dbscan
# dbscan_clusters_highlights = clustering.labels_
# #print(dbscan_clusters_highlights)

 #Apply tfidf vectorizer and kmeans on other content
col_Names=["Filename", "Content"]
content_df= pd.read_csv("content.csv", encoding='utf-8',names=col_Names)
#print(content_df)
clean_content_df = content_df.dropna()
#print(clean_content_df)
vectorizer = TfidfVectorizer()
vectorized_content= vectorizer.fit_transform(clean_content_df["Content"])
#print(vectorized_content)
kmeans_content = KMeans(n_clusters=6, random_state=300).fit(vectorized_content) #apply kmean
labels = kmeans_content.labels_
print(len(labels))
labelnp=list(labels)
array=[]
# array1 = [i for i, x in enumerate(labelnp) if x == 1]
for j in range(6):
     array.append([all_files[i] for i, x in enumerate(labelnp) if x == j])
print("contentclusters")
print(array)



# for i,label in enumerate(labels):
#      print(label, all_files[i])
# clustering = DBSCAN(eps=3).fit(vectorized_content) #apply dbscan
# dbscan_content_clusters = clustering.labels_
# # for i,label in enumerate(dbscan_content_clusters):
# #      print(label, all_files[i])
# #print(dbscan_content_clusters)

#Apply kmeans on the generated summary
col_Names=["Filename", "Summary"]
generated_summary_df = pd.read_csv("summarymain.csv", encoding='utf-8', names=col_Names)
#print(generated_summary_df)
#generated_summary_df.head()
vectorizer = TfidfVectorizer()
vectorized_summary= vectorizer.fit_transform(generated_summary_df["Summary"])
kmeans_summary = KMeans(n_clusters=6, random_state=300).fit(vectorized_summary) #apply kmeans
#print(kmeans_highlights.labels_)
summary_labels = kmeans_summary.labels_
print(len(summary_labels))
labelnp=list(summary_labels)
summary_array=[]
# array1 = [i for i, x in enumerate(labelnp) if x == 1]
for j in range(6):
     summary_array.append([all_files[i] for i, x in enumerate(labelnp) if x == j])
print("summaryclusters")
print(summary_array)
# for i,label in enumerate(summary_labels):
#      summary_cluster_assignment = (label, all_files[i])
     #print(summary_cluster_assignment)
#Apply dbscan on highlights(yet to do)
# clustering = DBSCAN(eps=3).fit(vectorized_highlights)#apply dbscan
# dbscan_clusters_highlights = clustering.labels_
# #print(dbscan_clusters_highlights)





