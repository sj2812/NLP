import csv
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics.cluster import adjusted_rand_score
import pandas as pd
from sklearn.metrics.cluster import adjusted_mutual_info_score
from sklearn import metrics


import numpy as np
directory=('articlesinXML')

labelfilenames=pd.DataFrame()
col_Names=["Filename"]
validfiles = (pd.read_csv("validfiles.csv",encoding='utf-8',names=col_Names))


col_Names=["Filename", "Abstract"]
abstract_df = pd.read_csv("abstract.csv",encoding='utf-8',names=col_Names)
labelfilenames["Filename"]=abstract_df["Filename"]

clean_abstract_df = abstract_df.dropna()


col_Names=["Filename", "Highlight"]
highlights_df = pd.read_csv("HighlightmainMorelength.csv",encoding='utf-8',names=col_Names)

clean_highlights_df = highlights_df.dropna()



vectorizer = TfidfVectorizer(stop_words='english',max_features=25000)
vectorized_abst= vectorizer.fit_transform(clean_abstract_df["Abstract"])

terms = (vectorizer.get_feature_names())

# kmeans_abstract = KMeans(n_clusters=7, random_state=300).fit(vectorized_abst)
# labels = kmeans_abstract.labels_
hac_clustering = AgglomerativeClustering(affinity='euclidean', linkage='ward', n_clusters=7).fit(vectorized_abst.todense())  # linkage is ward
labels = hac_clustering.labels_
clean_abstract_df["labels"]=labels

labelarray={}

labelnp=list(labels)
abstract_array=[]

for j in range(6):
     abstract_array.append([validfiles["Filename"][i] for i, x in enumerate(labelnp) if x == j])




print("abstractclusters")
print(abstract_array)

#Apply tfidf vectorizer and kmeans on Highlights
vectorizer = TfidfVectorizer(stop_words='english',max_features=25000)
clean_highlights_df['Highlight']=clean_highlights_df['Highlight'].replace(' ', np.nan)
clean=clean_highlights_df.dropna(axis=0,subset=["Highlight"])

vectorized_highlights= vectorizer.fit_transform(clean["Highlight"])
#kmeans_highlights = KMeans(n_clusters=7).fit(vectorized_highlights)#apply kmeans

hac_clustering_high = AgglomerativeClustering(affinity='euclidean', linkage='ward', n_clusters=7).fit(vectorized_highlights.todense())

#print(kmeans_highlights.labels_)
#highlights_labels = kmeans_highlights.labels_
highlights_labels = hac_clustering_high.labels_

labelnp=list(highlights_labels)
print(len(highlights_labels))
highlights_array=[]
clean_highlights_df["labels"]=highlights_labels

for j in range(6):
     highlights_array.append([validfiles["Filename"][i] for i, x in enumerate(labelnp) if x == j])
print("highlightclusters")
print((highlights_array))



col_Names=["Filename", "Content"]
content_df= pd.read_csv("content.csv", encoding='utf-8',names=col_Names)

clean_content_df = content_df.dropna()

vectorizer = TfidfVectorizer(stop_words='english',max_features=25000)
vectorized_content= vectorizer.fit_transform(clean_content_df["Content"])

#kmeans_content = KMeans(n_clusters=7, random_state=300).fit(vectorized_content)#apply kmean

hac_clustering_content = AgglomerativeClustering(affinity='euclidean', linkage='ward', n_clusters=7).fit(vectorized_content.todense())
labels=hac_clustering_content.labels_
#labels = kmeans_content.labels_

clean_content_df["labels"]=labels
print(len(labels))
labelnp=list(labels)
array=[]

for j in range(7):
     array.append([validfiles["Filename"][i] for i, x in enumerate(labelnp) if x == j])
print("contentclusters")
print(array)



#Apply kmeans on the generated summary
col_Names=["Filename", "Summary"]
generated_summary_df = pd.read_csv("summarymain.csv", encoding='utf-8', names=col_Names)

vectorizer = TfidfVectorizer(stop_words='english',max_features=25000)
vectorized_summary= vectorizer.fit_transform(generated_summary_df["Summary"])
#kmeans_summary = KMeans(n_clusters=7, random_state=300).fit(vectorized_summary) #apply kmeans
hac_clustering_summ = AgglomerativeClustering(affinity='euclidean', linkage='ward', n_clusters=7).fit(vectorized_summary.todense())
hac_clustering_summ_labels = hac_clustering_summ.labels_

#print(kmeans_highlights.labels_)
#summary_labels = kmeans_summary.labels_
summary_labels = hac_clustering_summ_labels
generated_summary_df["labels"]=summary_labels
print(len(summary_labels))
labelnp=list(summary_labels)
summary_array=[]

for j in range(7):
     summary_array.append([validfiles["Filename"][i] for i, x in enumerate(labelnp) if x == j])
print("summaryclusters")
print(summary_array)

print("Rand Index")
print(adjusted_rand_score(clean_content_df["labels"],clean_highlights_df["labels"]))
print(adjusted_rand_score(clean_content_df["labels"],clean_abstract_df["labels"]))
print(adjusted_rand_score(clean_content_df["labels"],generated_summary_df["labels"]))
print(adjusted_rand_score(clean_highlights_df["labels"],generated_summary_df["labels"]))
print(adjusted_rand_score(clean_abstract_df["labels"],generated_summary_df["labels"]))

print("mutual-info-score")
print(adjusted_mutual_info_score(clean_content_df["labels"],clean_highlights_df["labels"]))
print(adjusted_mutual_info_score(clean_content_df["labels"],clean_abstract_df["labels"]))
print(adjusted_mutual_info_score(clean_content_df["labels"],generated_summary_df["labels"]))
print(adjusted_mutual_info_score(clean_highlights_df["labels"],generated_summary_df["labels"]))
print(adjusted_mutual_info_score(clean_abstract_df["labels"],generated_summary_df["labels"]))

print("completeness")
print(metrics.completeness_score(clean_content_df["labels"],clean_highlights_df["labels"]))
print(metrics.completeness_score(clean_content_df["labels"],clean_abstract_df["labels"]))
print(metrics.completeness_score(clean_content_df["labels"],generated_summary_df["labels"]))
print(metrics.completeness_score(clean_highlights_df["labels"],generated_summary_df["labels"]))
print(metrics.completeness_score(clean_abstract_df["labels"],generated_summary_df["labels"]))

print("fowlkesscore")
print(metrics.fowlkes_mallows_score(clean_content_df["labels"],clean_highlights_df["labels"]))
print(metrics.fowlkes_mallows_score(clean_content_df["labels"],clean_abstract_df["labels"]))
print(metrics.fowlkes_mallows_score(clean_content_df["labels"],generated_summary_df["labels"]))
print(metrics.fowlkes_mallows_score(clean_highlights_df["labels"],generated_summary_df["labels"]))

fig, ax = plt.subplots()
plt.rcParams['font.size'] = 6
ax.scatter(clean_highlights_df["Filename"],clean_highlights_df["labels"],c="black",label="Highlight")
for i, txt in enumerate(clean_highlights_df["Filename"]):
     txt=str(txt).replace(".xml","")
     txt=txt.replace("s","")
     txt=txt.replace("S","")
     txt=txt[-5:]
     ax.annotate(txt, (clean_highlights_df["Filename"][i], clean_highlights_df["labels"][i]))
plt.xticks(rotation=90)

fig1, ax1 = plt.subplots()
ax1.scatter(clean_abstract_df["Filename"],clean_abstract_df["labels"],c="red",label="Abstract")
for i, txt in enumerate(clean_abstract_df["Filename"]):
     txt=str(txt).replace(".xml","")
     txt=txt.replace("s","")
     txt=txt.replace("S","")
     txt=txt[-5:]
     ax1.annotate(txt, (clean_abstract_df["Filename"][i], clean_abstract_df["labels"][i]))

plt.xticks(rotation=90)

fig2, ax2 = plt.subplots()
ax2.scatter(generated_summary_df["Filename"],generated_summary_df["labels"],c="blue",label="Summary")
for i, txt in enumerate(generated_summary_df["Filename"]):
     txt=str(txt).replace(".xml","")
     txt=txt.replace("s","")
     txt=txt.replace("S","")
     txt=txt[-5:]
     ax2.annotate(txt, (generated_summary_df["Filename"][i], generated_summary_df["labels"][i]))

plt.xticks(rotation=90)

fig3, ax3 = plt.subplots()
ax3.scatter(clean_content_df["Filename"],clean_content_df["labels"],c="orange",label="Content")
for i, txt in enumerate(clean_content_df["Filename"]):
     txt=str(txt).replace(".xml","")
     txt=txt.replace("s","")
     txt=txt.replace("S","")
     txt=txt[-5:]
     ax3.annotate(txt, (clean_content_df["Filename"][i], clean_content_df["labels"][i]))


plt.xticks(rotation=90)
plt.show()




