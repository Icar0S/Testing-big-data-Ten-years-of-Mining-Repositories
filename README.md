# 🧪 Ten Years of Big Data Testing: Mining Platforms Used by Developers
All scripts and data related to this research will be made publicly available.
## Mining Testing Tools and Practices for Big Data Systems

## 📌 Overview and Goal
This research investigates the evolution of software testing tools and practices in Big Data systems by systematically mining gray literature from Stack Overflow, Medium, LinkedIn, and Dev.to (2015–2024). The goal is to extract and analyze industry-adopted testing frameworks (e.g., Selenium, JUnit), testing types (e.g., Unit Testing, Load Testing), and strategies employed in practical environments.

The study combines automated repository mining with a comparative analysis against systematic literature review findings, offering a replicable framework for future studies in software quality, data-intensive systems, and testing trends.

---

## 🧠 Research Questions
1. **Which testing tools and frameworks for Big Data systems are most mentioned and recommended within developer communities (Stack Overflow, Medium, LinkedIn, Dev.to)?**
2. **What testing methods and approaches for Big Data systems are frequently discussed on these platforms, emphasizing aspects such as quality, performance, and reliability?**
3. ** What tools and methods are identified that differ from those found in the white literature?**
4. **What are the key topics in the field of Big Data testing identified by analyzing all posts?**

---

## 🌐 Data Sources & Collection Methods
Data was gathered from:
   - Stack Exchange API: Stack Overflow, Software Engineering, and SQA forums.
   - Google Custom Search API: Scraping of LinkedIn, Medium, and Dev.to posts.
   - Time span: 2015 to 2024
   - Resulting in 3,301 unique links and a filtered set of 760 relevant posts.

The data was processed and filtered to ensure high quality, focusing on content published from 2014 to 2024 that discusses tools, methods, and best practices for Big Data testing.

---

## 📁 Repository Structure
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

## 📊 Dataset
Located in data/:
   - custom_search_links_all_StackExchange.xlsx
   - custom_search_links_all_Medium.xls
   - custom_search_links_all_LinkedIn.xlsx
   - custom_search_links_all_DevTo.xlsx
   - extracted_posts_with_content.xls  #To use in LDAvis
Each file includes source metadata, post excerpts, detected keywords, and classification as "Tool" or "Method".

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

**To see more about the project, click** [here](https://github.com/Icaro0S/testing-tools-bigdata).
