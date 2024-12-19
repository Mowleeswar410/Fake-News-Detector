# -*- coding: utf-8 -*-
"""DetectingKeywordsAssociatedwithFakeNews.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tjIpCRYYLo_ZepG-1WdtsMUG-1JJeQDd
"""

import pandas as pd
from google.colab import files
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

uploaded = files.upload()

data = pd.read_csv("cleaned_dataset.csv")

data.head()

import nltk
nltk.download("stopwords")
nltk.download("punkt")

stop_words = set(stopwords.words("english"))

title_counter = Counter()
text_counter = Counter()

for index, row in data.iterrows():
  title_words = word_tokenize(row["title"])
  text_words = word_tokenize(row["text"])

  title_words = [word.lower() for word in title_words if word.isalpha() and word.lower() not in stop_words]
  text_words = [word.lower() for word in title_words if word.isalpha() and word.lower() not in stop_words]

  if row["label"] == "Fake":
    title_counter.update(title_words)
    text_counter.update(text_words)

top_keywords_title = title_counter.most_common(5)
top_keywords_text = text_counter.most_common(5)

print("Top 5 Keywords Associated with Fake News Titles:")
for keyword, count in top_keywords_title:
  print(f"{keyword}:{count} times")
print("Top 5 Keywords Associated with Fake News Texts:")
for keyword, count in top_keywords_text:
  print(f"{keyword}:{count} times")