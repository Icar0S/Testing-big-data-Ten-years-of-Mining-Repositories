# 🧪 Ten Years of Big Data Testing: Mining Platforms Used by Developers
All scripts and data related to this research will be made publicly available.
## Mining Testing Tools and Practices for Big Data Systems

## 📌 Overview and Goal
This research investigates the evolution of software testing tools and practices in Big Data systems by systematically mining gray literature from Stack Overflow, Medium, LinkedIn, and Dev.to (2015–2024). The goal is to extract and analyze industry-adopted testing frameworks (e.g., Apache Spark, dbt, Great Expectations), testing types (e.g., Unit Testing, Integration Testing, Data Quality Testing), and strategies employed in practical environments.

The study combines automated repository mining with clustering techniques (K-Means, Bisecting K-Means, DBSCAN) and topic modeling (LDA), alongside a comparative analysis against systematic literature review findings from white literature. This offers a replicable framework for future studies in software quality, data-intensive systems, and testing trends, bridging academic and practical perspectives.

---

## 🧠 Research Questions
1. **Which testing tools and frameworks for Big Data systems are most mentioned and recommended within developer communities (Stack Overflow, Medium, LinkedIn, Dev.to)?**
2. **What testing methods and approaches for Big Data systems are frequently discussed on these platforms, emphasizing aspects such as quality, performance, and reliability?**
3. **Which identified tools and methods require further investigation in the formal scientific literature?**

---
## 📊 Key Findings
- Tools: Apache Spark and dbt emerged as the most cited, followed by Great Expectations, Deequ/PyDeequ, and PySpark. These reflect a focus on scalable distributed processing and data validation.
- Methods: Unit Testing, Integration Testing, and Data Quality Testing dominate discussions, adapted for Big Data challenges like pipelines and anomaly detection.
- Gaps: Tools like dbt and Great Expectations, along with methods such as end-to-end pipeline testing, are underrepresented in academic literature, highlighting areas for future research.
- Thematic Insights: Clustering and LDA revealed themes around data quality validation, ETL pipelines, and distributed testing, with a pragmatic industry focus complementing academic explorations.
Detailed results, including cluster analyses and datasets, are available in the repository.

---

## 🚀 How to Replicate

1. Data Collection:
Run scripts/ten-years-bigdata-testing.ipynb to mine links from platforms (2015–2024).
Execute scripts/extract_content.py to fetch post texts.
2. Preprocessing and Analysis:
- Run scripts/ten-years-bigdata-testing.ipynb 
- For clustering: scripts/ten-years-bigdata-testing.ipynb
- For LDA: topic modeling/ (optimize topics via coherence).
3. Manual Analysis:
- Review selected clusters/topics in /data/clusters/ for tool/method extraction.
4. Visualizations:
- Generate plots with images/
Full pipeline execution time: ~2-3 hours on a standard machine (Intel i7, 16GB RAM).

---
## 🌐 Data Sources & Collection Methods
Data was gathered from:
   - Stack Exchange API: Stack Overflow, Software Engineering, and SQA forums.
   - Google Custom Search API: Scraping of LinkedIn, Medium, and Dev.to posts.
   - Time span: 2015 to 2024
   - Resulting in 3,301 unique links.

The data was processed and filtered to ensure high quality, focusing on content published from 2014 to 2024 that discusses tools, methods, and best practices for Big Data testing.

---

## 🛠️ Repository Structure
```bash
.
├── data/                # Cleaned and structured datasets
├── documents/           # Protocols and methodology descriptions
├── images/              # Charts, graphs, and figures
├── scripts/             # Python scripts for scraping, mining, and processing
├── topic modeling/      # LDA topic modeling files and visualization
├── LICENSE              # Licensing information
└── README.md            # Project overview
```

---

## 📈 Figures
This folder contains visualizations and charts related to the analysis of the data:
- [**Methodology.png**](images/method-MSR.png) The methodology
- [**Top-Testing-Tools.png**](images/Frequency-Tools.png): A bar chart showing the most frequently mentioned testing tools, such as Selenium, JUnit, Postman, etc.
- [**Top-Testing-Methods.png**](images/Frequency-Methods.png):  A bar chart depicting the most commonly mentioned testing methods, including Unit Testing, Regression Testing, and Load Testing.
- [**Data-Source-Distribution.png**](images/Posts-Source.png):  A bar chart showing the distribution of data collected from each source (e.g., StackExchange, LinkedIn, Medium, Dev.to).

- The graphs showing the trends in Big Data testing practices over time (2014-2024).
- ![image](https://github.com/user-attachments/assets/9aa2b5a1-f5d9-4458-b7e3-f31cbaa0a38e) : Topic modeling visualization of mined posts using LDAvis
- ![image](https://github.com/user-attachments/assets/0273fca3-ec44-426d-9202-685242e1e5af) : Topic modeling visualization of the white literature corpus using LDAvis


- The graphs showing the clusters kmeans, bkmeans, dbscan e a modelagem de tópicos lda
<img width="1000" height="600" alt="cluster_viz" src="https://github.com/user-attachments/assets/9e3aca00-5275-447b-b02a-80e023f53cf5" /> : KMEANS

<img width="1000" height="600" alt="cluster_viz_BKMEANS" src="https://github.com/user-attachments/assets/95ed5e30-771d-4854-a5f6-f581f0c9a20f" /> : BKMEANS

<img width="1000" height="600" alt="cluster_viz_dbscan" src="https://github.com/user-attachments/assets/8b781708-f5fe-40a9-9a5b-fde80e67c461" /> : DBSCAN

<img width="800" height="500" alt="lda_coherence_scores" src="https://github.com/user-attachments/assets/2ca4b3e1-3f26-432b-9d23-415026437ec3" /> : LDA scores



---

## 📜 Documentation
This folder contains the relevant documents detailing the methodology and protocols used in this study:
- [**Data-Mining-Protocol.pdf**](documents/Protocol Research - Testing big data_ Ten years of Mining Repositories.pdf): Detailed methodology, inclusion/exclusion criteria, data cleaning pipeline, and validation steps.

---

## 🛠️ Methodology Summary
- Keyword-Based Scraping: Defined based on prior systematic reviews (e.g., Oliveira et al. 2024).
- Automated Crawling: Python + BeautifulSoup + Requests for page content.
- Classification: Regex-based detection of tools and testing types.
- Topic Modeling: LDA + Gensim + PyLDAvis for semantic insights.
- Clusterization: KMEANS, BKMEANS, DBSCAN
- Comparison: Integration with systematic literature review to highlight alignment or divergence.

---

## ⚖️ Ethical Considerations

- Only public content was mined.
- No login-restricted or private data was accessed.
- API Terms of Use (Google, StackExchange) were followed.
- No personal user data was retained or stored.

---

## 🚀 Future Work
- Expand mining to additional platforms (e.g., GitHub Discussions, Reddit, Substack).
- Apply Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) to:
   - Automatically summarize and contextualize testing practices.
   - Classify emerging tool types and methods across domains.
   - Generate real-time dashboards to track trends in testing and quality assurance.

- Integrate ISO/IEC 25010 attributes for semantic classification of quality aspects.

Enrich the topic modeling pipeline with hybrid unsupervised + embedding-based methods (e.g., BERTopic).
For any inquiries or collaborations, please feel free to contact the repository owner.

---
