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
        "evaluation",
        "systems",
        "development",
        "created",
        "processing",
        "application",
        "approaches",
        "aspose.words",
        "information",
        "copyright",
        "input",
        "aspose",
        "case",
        "2003-2024",
        "ltd",
        "results",
        "cases",
        "proposed",
        "applications",
        "approach",
        "however",
        "technology",
        "large",
        "research",
        "storage",
        "ieee",
        "engineering",
        "height",
        "program",
        "control",
        "mapreduce",
        "patient",
        "patients",
        "output",
        "datasets",
        "clinical",
        "market",
        "level",
        "management",
        "data",
        "analysis",
        "healthcare",
        "medical",
        "health",
        "clinical",
        "dataset",
        "clinical",
        "healthcare",
        "medical",
        "health",
        "clinical",
        "weight",
        "values",
        "ltd.",
        "layer",
        "frameworks",
        "section",
        "module",
        "measurements",
        "execution",
        "unstructured",
        "therefore",
        "whether",
        "database",
        "since",
        "based",
        "journal",
        "flight",
        "investment",
        "models",
        "internet",
        "network",
        "stream",
        "architecture",
        "recommendation",
        "rois",
    ]
)

# ----- Carregar documentos -----
documents = []
directory = "docs/text/test"

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(
            os.path.join(directory, filename), "r", encoding="utf-8", errors="ignore"
        ) as f:
            documents.append(f.read())

print(f"📄 Total de documentos carregados: {len(documents)}")

# ----- Tokenização e remoção de stopwords -----
words = [
    [
        word
        for word in word_tokenize(text.lower())
        if word not in stop_words and len(word) > 3 and not word.isdigit()
    ]
    for text in documents
]

dictionary = corpora.Dictionary(words)
corpus = [dictionary.doc2bow(text) for text in words]

# ----- Treinamento do modelo LDA com ajustes -----
lda_model = gensim.models.LdaModel(corpus, id2word=dictionary, num_topics=3, passes=3)

# ----- Visualização interativa com pyLDAvis -----
lda_display = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
pyLDAvis.save_html(lda_display, "lda-topics-article-tests-v3-p3.html")

print("✅ Visualização gerada: lda-topics-article-tests.html")
