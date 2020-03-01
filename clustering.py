import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

import pandas as pd
import os
# from data_collectionfunctions import all_files
import csv
import numpy as np
from sklearn.neighbors import NearestNeighbors

#pca = PCA(n_components=None)

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
highlights_df = pd.read_csv("HighlightmainMorelength.csv",encoding='utf-8',names=col_Names)
#print(highlights_df)
clean_highlights_df = highlights_df.dropna()
#print(clean_highlights_df)

#Apply tfidf vectorizer and kmeans on abstract
vectorizer = TfidfVectorizer()
vectorized_abst= vectorizer.fit_transform(clean_abstract_df["Abstract"])
#pca.fit(vectorized_abst)
#print(vectorized_abst)
terms = (vectorizer.get_feature_names())
#print(terms)
#Apply kmeans on abstract

for k in range(2, 10):
    kmeans_abstract = KMeans(n_clusters=k, random_state=300).fit(vectorized_abst) #apply kmean
    labels = kmeans_abstract.labels_
    #print(labels)
    #print(len(labels))
    labelnp=list(labels)
    abstract_array=[]
    array1 = [i for i, x in enumerate(labelnp) if x == 1]
    for j in range(6):
         abstract_array.append([all_files[i] for i, x in enumerate(labelnp) if x == j])
    #print("abstractclusters")
    #print(abstract_array)
    silhouette_avg = silhouette_score(vectorized_abst, labels)
    #print(silhouette_avg)
    print("For n_clusters in abstract =", k,
      "The average silhouette_score is :", silhouette_avg)



#for elbow method
# kmeans_abstract = [KMeans(n_clusters=k, random_state=250) for k in K]
# score = [kmeans_abstract[k].fit(vectorized_abst).score(vectorized_abst) for k in range(len(kmeans_abstract))] #it checks at which point your score does not have much variance
# print(score)
# plt.plot(K, score)
# plt.xlabel('Number of Clusters')
# plt.ylabel('Score')
# plt.title('Elbow Curve')
# plt.show()
#print(labels)
# clean_abstract_df['cluster assignment'] = labels
# clean_abstract_df.head()
# for i,label in enumerate(labels):
#      abstract_cluster_assignment = (label, all_files[i])
     #print(abstract_cluster_assignment)
#Apply dbscan on abstract(yet to do)
# clustering = DBSCAN(eps=0.9).fit(vectorized_abst) #apply dbscan
# dbscan_abstract_clusters = clustering.labels_
# print(dbscan_abstract_clusters)
clusternumber=[]
silscore=[]
for k in range(2, 10):
    hac_clustering = AgglomerativeClustering(affinity='euclidean', linkage='ward', n_clusters=k).fit(vectorized_abst.todense()) #linkage is ward
    hac_abst_labels =hac_clustering.labels_
    score = silhouette_score(vectorized_abst, hac_abst_labels, metric='euclidean')
    silhouette_avg_hac = silhouette_score(vectorized_abst, hac_abst_labels)
    clusternumber.append(k)
    silscore.append(silhouette_avg_hac)
    # print(silhouette_avg)
    print("For n_clusters in abstract for hac =", k,
          "The average silhouette_score is :", silhouette_avg_hac)
plt.plot(clusternumber,silscore)
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette score')
plt.legend(['Abstract'])

    # print("jdndnslkdnsl")
    # print(score)





#Apply tfidf vectorizer and kmeans on Highlights
vectorizer = TfidfVectorizer(stop_words='english',max_features=25000)
clean_highlights_df['Highlight']=clean_highlights_df['Highlight'].replace(' ', np.nan)
clean=clean_highlights_df.dropna(axis=0,subset=["Highlight"])

vectorized_highlights= vectorizer.fit_transform(clean["Highlight"])
for k in range(2, 10):
    kmeans_highlights = KMeans(n_clusters=k, random_state=300).fit(vectorized_highlights) #apply kmeans
    #print(kmeans_highlights.labels_)
    highlights_labels = kmeans_highlights.labels_
    labelnp=list(highlights_labels)
    #print(len(highlights_labels))
    highlights_array=[]
    # array1 = [i for i, x in enumerate(labelnp) if x == 1]
    for j in range(6):
         highlights_array.append([all_files[i] for i, x in enumerate(labelnp) if x == j])
    # print("highlightclusters")
    # print((highlights_array))
    silhouette_avg = silhouette_score(vectorized_highlights, highlights_labels)
    #print(silhouette_avg)
    print("For n_clusters in highlights =", k,
          "The average silhouette_score is :", silhouette_avg)
# K = range(1,20)
# kmeans_highlights = [KMeans(n_clusters=k, random_state=250) for k in K]
# score = [kmeans_highlights[k].fit(vectorized_highlights).score(vectorized_highlights) for k in range(len(kmeans_highlights))] #it checks at which point your score does not have much variance
# plt.plot(K, score)
# plt.xlabel('Number of Clusters')
# plt.ylabel('Score')
# plt.title('Elbow Curve')
# plt.show()
# for i,label in enumerate(highlights_labels):
#      highlights_cluster_assignment = (label, all_files[i])
     #print(highlights_cluster_assignment)
#Apply dbscan on highlights
# clustering = DBSCAN(eps=0.9).fit(vectorized_highlights)#apply dbscan
# dbscan_clusters_highlights = clustering.labels_
# print(dbscan_clusters_highlights)
clusternumber=[]
silscore=[]
for k in range(2, 10):
    hac_clustering_high = AgglomerativeClustering(affinity='euclidean', linkage='ward', n_clusters=k).fit(vectorized_highlights.todense())
    hac_high_labels =hac_clustering_high.labels_
    score = silhouette_score(vectorized_highlights, hac_high_labels, metric='euclidean')
    silhouette_avg_hac = silhouette_score(vectorized_highlights, hac_high_labels)
    # print(silhouette_avg)
    clusternumber.append(k)
    silscore.append(silhouette_avg_hac)
    print("For n_clusters in highlights for hac =", k,
          "The average silhouette_score is :", silhouette_avg_hac)
    #print(score)
plt.plot(clusternumber,silscore)
plt.legend(['Highlights'])

 #Apply tfidf vectorizer and kmeans on other content
col_Names=["Filename", "Content"]
content_df= pd.read_csv("content.csv", encoding='utf-8',names=col_Names)
#print(content_df)
clean_content_df = content_df.dropna()
#print(clean_content_df)
vectorizer = TfidfVectorizer(stop_words='english',max_features=25000)
vectorized_content= vectorizer.fit_transform(clean_content_df["Content"])
#print(vectorized_content)
for k in range(2, 10):
    kmeans_content = KMeans(n_clusters=k, random_state=300).fit(vectorized_content) #apply kmean
    content_labels = kmeans_content.labels_
    #print(len(labels))
    labelnp=list(content_labels)
    array=[]
    # array1 = [i for i, x in enumerate(labelnp) if x == 1]
    for j in range(6):
         array.append([all_files[i] for i, x in enumerate(labelnp) if x == j])
    # print("contentclusters")
    # print(array)
    silhouette_avg = silhouette_score(vectorized_content, content_labels)
    # print(silhouette_avg)
    print("For n_clusters in other content =", k,
          "The average silhouette_score is :", silhouette_avg)
#Apply dbscan on other content
# clustering = DBSCAN(eps=0.9).fit(vectorized_content)#apply dbscan
# dbscan_clusters_highlights = clustering.labels_
# print(dbscan_clusters_highlights)
clusternumber=[]
silscore=[]
for k in range(2, 10):
    hac_clustering_content = AgglomerativeClustering(affinity='euclidean', linkage='ward', n_clusters=k).fit(vectorized_content.todense())
    hac_content_labels =hac_clustering_content.labels_
    score = silhouette_score(vectorized_content, hac_content_labels, metric='euclidean')
    silhouette_avg_hac = silhouette_score(vectorized_content, hac_content_labels)
    # print(silhouette_avg)
    clusternumber.append(k)
    silscore.append(silhouette_avg_hac)
    print("For n_clusters in other content for hac =", k,
          "The average silhouette_score is :", silhouette_avg_hac)
    # print(score)
plt.plot(clusternumber,silscore)
plt.legend(['Other content'])
#print(score)



#Apply kmeans on the generated summary
col_Names=["Filename", "Summary"]
generated_summary_df = pd.read_csv("summarymain.csv", encoding='utf-8', names=col_Names)
#print(generated_summary_df)
#generated_summary_df.head()
vectorizer = TfidfVectorizer(stop_words='english',max_features=25000)
vectorized_summary= vectorizer.fit_transform(generated_summary_df["Summary"])
for k in range(2,10):

    kmeans_summary = KMeans(n_clusters=k, random_state=300).fit(vectorized_summary) #apply kmeans
    #print(kmeans_highlights.labels_)
    summary_labels = kmeans_summary.labels_
    #print(len(summary_labels))
    labelnp=list(summary_labels)
    summary_array=[]
    # array1 = [i for i, x in enumerate(labelnp) if x == 1]
    for j in range(6):
         summary_array.append([all_files[i] for i, x in enumerate(labelnp) if x == j])
    # print("summaryclusters")
    # print(summary_array)
    silhouette_avg = silhouette_score(vectorized_summary, summary_labels)
    # print(silhouette_avg)
    print("For n_clusters in summary =", k,
          "The average silhouette_score is :", silhouette_avg)
# App
clusternumber=[]
silscore=[]
for k in range(2,10):
    hac_clustering_summ = AgglomerativeClustering(affinity='euclidean', linkage='ward', n_clusters=k).fit(vectorized_summary.todense())
    hac_clustering_summ_labels = hac_clustering_summ.labels_
    score = silhouette_score(vectorized_summary, hac_clustering_summ_labels, metric='euclidean')
    silhouette_avg_hac = silhouette_score(vectorized_summary, hac_clustering_summ_labels)
    # print(silhouette_avg)
    clusternumber.append(k)
    silscore.append(silhouette_avg_hac)
    print("For n_clusters in generated summary for hac =", k,
          "The average silhouette_score is :", silhouette_avg_hac)

plt.plot(clusternumber,silscore)
plt.legend(['Abstract','Highlights','Candidate Summary','Other content'])
plt.show()

#print(score)
# hac_summ_labels =hac_clustering_summ.labels_
# score = silhouette_score(vectorized_summary, hac_summ_labels, metric='euclidean')
# print(score)
# for i,label in enumerate(summary_labels):
#      summary_cluster_assignment = (label, all_files[i])
     #print(summary_cluster_assignment)
#Apply dbscan on highlights(yet to do)
# clustering = DBSCAN(eps=3).fit(vectorized_highlights)#apply dbscan
# dbscan_clusters_highlights = clustering.labels_
# #print(dbscan_clusters_highlights)





