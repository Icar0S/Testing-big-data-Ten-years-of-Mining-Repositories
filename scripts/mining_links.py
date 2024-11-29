import requests
import pandas as pd
import time

queriesM = [
    # 2024 a 2020
    'site:medium.com ("big data" OR "data quality") AND test* daterange:20200101-20211231',
    'site:medium.com ("big data" OR "data quality") AND test* daterange:20210101-20211231',
    'site:medium.com ("big data" OR "data quality") AND test* daterange:20220101-20221231',
    'site:medium.com ("big data" OR "data quality") AND test* daterange:20230101-20231231',
    'site:medium.com ("big data" OR "data quality") AND test* daterange:20240101-20241231',
    # 2019 a 2014
    'site:medium.com ("big data" OR "data quality") AND test* daterange:20140101-20191231',
]
queriesL = [
    # 2024 a 2020
    'site:linkedin.com ("big data" OR "data quality") AND test* daterange:20200101-20211231',
    'site:linkedin.com ("big data" OR "data quality") AND test* daterange:20210101-20211231',
    'site:linkedin.com ("big data" OR "data quality") AND test* daterange:20220101-20221231',
    'site:linkedin.com ("big data" OR "data quality") AND test* daterange:20230101-20231231',
    'site:linkedin.com ("big data" OR "data quality") AND test* daterange:20240101-20241231',
    # 2019 a 2014
    'site:linkedin.com ("big data" OR "data quality") AND test* daterange:20140101-20191231',
]
queriesD = [
    # 2024 a 2020
    'site:dev.to ("big data" OR "data quality") AND test* daterange:20200101-20211231',
    'site:dev.to ("big data" OR "data quality") AND test* daterange:20210101-20211231',
    'site:dev.to ("big data" OR "data quality") AND test* daterange:20220101-20221231',
    'site:dev.to ("big data" OR "data quality") AND test* daterange:20230101-20231231',
    'site:dev.to ("big data" OR "data quality") AND test* daterange:20240101-20241231',
    # 2019 a 2014
    'site:dev.to ("big data" OR "data quality") AND test* daterange:20140101-20191231',
]

all_links = []

for query in queriesD:
    print(f"Buscando resultados para a query: {query}")
    for start in range(1, 101, 10):
        try:
            url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}&start={start}"
            response = requests.get(url)

            if response.status_code == 200:
                results = response.json()
                items = results.get("items", [])
                links = [item["link"] for item in items]
                all_links.extend(links)

                if len(items) < 10:
                    break  # Não há mais resultados
            else:
                print(f"Erro na requisição: {response.status_code} - {response.text}")
                break
        except Exception as e:
            print(f"Erro ao buscar resultados: {e}")
        time.sleep(1)  # Pausa entre requisições

# Salva os links em um CSV
df = pd.DataFrame(all_links, columns=["Link"])
df.to_csv("custom_search_links_all_DevTo.csv", index=False)
print(
    f"Links coletados e salvos em 'custom_search_links_all_DevTo.csv'. Total de links: {len(all_links)}"
)
