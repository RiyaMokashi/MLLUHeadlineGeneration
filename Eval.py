import pandas as pd
data_tuples = list(zip(new_labels,new_texts))
df = pd.DataFrame(data_tuples, columns=['labels','texts'])

a = []
from gensim.summarization.summarizer import summarize
for i in df['texts']:

    i= i + str(". This is second sentence. This is third")             # this is to add two more sentences so that gensim summarizes it. These sentence add no value to summary.
    a.append(summarize(i, ratio=0.4, split = True))

df['Summary'] = a

from textblob import TextBlob

b = []
for i in df['texts']:

    i= i + str(".")
    c = TextBlob(i)
    b.append((c).sentiment)

df['Text_Sentiment'] = b

d = []

for i in df['labels']:

    i= i + str(".")
    c = TextBlob(i)
    d.append((c).sentiment)

df['Headline_Sentiment'] = d

df['Summary'] = df['Summary'].astype(str)

e = []

for i in df['Summary']:

    i = i + str("TEST")
    c = TextBlob(i)
    e.append((c).sentiment)

df['Gen_Sentiment'] = e

df2 = df.sample(frac=0.01, replace=True, random_state=1) #Use in case of computational limits

from rouge import Rouge 
f = []

for i in df2['Summary']:
  for k in df2['labels']:
    rouge = Rouge()
    scores = rouge.get_scores(i, k)
    f.append((scores))

#df2['ROUGE'] = f

print(f)