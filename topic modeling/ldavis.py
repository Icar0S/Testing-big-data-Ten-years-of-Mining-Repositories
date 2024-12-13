import gensim
from gensim import corpora
import pyLDAvis.gensim_models
import os
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Baixar recursos
nltk.download("stopwords")
nltk.download("punkt_tab")

stop_words = set(stopwords.words("english"))

stop_words.update(list(string.punctuation))

stop_words.update([str(n) for n in range(10)])

stop_words.add("’")
stop_words.add("also")
stop_words.add("would")
stop_words.add("one")
stop_words.add("use")
stop_words.add("”")
stop_words.add("“")
stop_words.add("–")
stop_words.add("sp")
stop_words.add("fig")
stop_words.add("x")
stop_words.add("et")
stop_words.add("c")
stop_words.add("al")
stop_words.add("data")
stop_words.add("sign")
stop_words.add("like")
stop_words.add("comment")
stop_words.add("copy")
stop_words.add("link")
stop_words.add("follow")
stop_words.add("need")

texts = []

directory = "docs/miner_posts"

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(
            os.path.join(directory, filename), "r", encoding="utf-8", errors="ignore"
        ) as f:
            text = f.read()
            words = word_tokenize(text)
            texts.append(text)

words = [
    [
        word
        for word in word_tokenize(text.lower())
        if word not in stop_words and len(word) > 3 and not word.isdigit()
    ]
    for text in texts
]

dictionary = corpora.Dictionary(words)
corpus = [dictionary.doc2bow(text) for text in words]

lda_model = gensim.models.LdaModel(corpus, num_topics=6, id2word=dictionary, passes=2)

lda_display = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
pyLDAvis.save_html(lda_display, "lda-topics-miner-posts.html")
