from rouge import Rouge
import pandas as pd
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(8735 * 2080 + 10)
col_Names=["Filename", "Abstract"]
abstract_df = pd.read_csv("abstract.csv", encoding='utf-8', names=col_Names)
#print(abstract_df)
#abstract_df.head()
clean_abstract_df = abstract_df.dropna()
#print(clean_abstract_df)
col_Names=["Filename", "Highlight"]
highlights_df = pd.read_csv("highlights.csv", encoding='utf-8', names=col_Names)
#print(highlights_df)
clean_highlights_df = highlights_df.dropna()
#print(clean_highlights_df)

col_Names=["Filename", "Summary"]
generated_summary_df = pd.read_csv("summarymain.csv", encoding='utf-8', names=col_Names)
#print(generated_summary_df)

rouge = Rouge()
scores = rouge.get_scores(generated_summary_df["Summary"].fillna(" "),clean_abstract_df["Abstract"],avg=True)
print(" Compare summary and abstract")
print(scores)

rouge = Rouge()
scores = rouge.get_scores(generated_summary_df["Summary"].fillna(" "), clean_highlights_df["Highlight"],avg=True)
print(" Compare summary and highlights")
print(scores)

