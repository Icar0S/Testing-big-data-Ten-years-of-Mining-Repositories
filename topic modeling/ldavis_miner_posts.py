import os
import nltk
import string
import gensim
import pyLDAvis.gensim_models
from gensim import corpora
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Baixar recursos do NLTK
nltk.download("stopwords")
nltk.download("punkt")

# ----- Stopwords personalizadas -----
stop_words = set(stopwords.words("english"))
stop_words.update(string.punctuation)
stop_words.update([str(n) for n in range(10)])
stop_words.update(
    [
        "’",
        "”",
        "“",
        "=",
        "–",
        "//",
        "https",
        "http",
        "also",
        "use",
        "one",
        "two",
        "three",
        "sp",
        "fig",
        "et",
        "al",
        "x",
        "t",
        "s",
        "like",
        "comment",
        "follow",
        "link",
        "copy",
        "data",
        "sign",
        "need",
        "medium",
        "com",
        "data",
        "test",
        "testing",
        "system",
        "use",
        "quality",
        "using",
        "software",
        "create",
        "business",
        "share",
        "mode",
        "contribution",
        "time",
        "code",
        "policy",
        "linkedin",
        "work",
        "learning",
        "privacy",
        "process",
        "jobs",
        "analytics",
        "community",
        "model",
        "engineer",
        "analysis",
        "tests",
        "example",
        "science",
        "fullscreen",
        "user",
        "report",
        "join",
        "help",
        "comments",
        "used",
        "first",
        "make",
        "hide",
        "different",
        "open",
        "reply",
        "menu",
        "would",
        "following",
        "want",
        "many",
        "well",
        "table",
        "file",
        "read",
        "people",
        "ensure",
        "article",
        "enter",
        "value",
        "exit",
        "based",
        "step",
        "best",
        "source",
        "joined",
        "team",
        "teams",
        "name",
        "text",
        "post",
        "blog",
        "content",
        "button",
        "dropdown",
        "search",
        "write",
        "good",
        "important",
        "early",
        "machine",
        "engineering",
        "management",
        "cloud",
    ]
)

# ----- Carregar documentos -----
documents = []
directory = "docs/miner_posts"
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(
            os.path.join(directory, filename), "r", encoding="utf-8", errors="ignore"
        ) as f:
            documents.append(f.read())

# Aviso sobre tamanho médio dos documentos
print(f"📄 Total de documentos carregados: {len(documents)}")

# ----- Tokenização e limpeza -----
processed_docs = [
    [
        word
        for word in word_tokenize(doc.lower())
        if word not in stop_words and len(word) > 3 and not word.isdigit()
    ]
    for doc in documents
]

# ----- Verificação de documentos vazios -----
processed_docs = [doc for doc in processed_docs if len(doc) >= 10]
print(f"📉 Documentos após filtragem (mín. 10 tokens): {len(processed_docs)}")

# ----- Construção do corpus -----
dictionary = corpora.Dictionary(processed_docs)
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

# ----- Treinamento do modelo LDA com ajustes -----
lda_model = gensim.models.LdaModel(corpus, id2word=dictionary, num_topics=6, passes=2)


# ----- Visualização interativa com pyLDAvis -----
lda_display = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
pyLDAvis.save_html(lda_display, "lda-topics-miner-posts.html")

print("✅ Visualização gerada: lda-topics-miner-posts.html")
