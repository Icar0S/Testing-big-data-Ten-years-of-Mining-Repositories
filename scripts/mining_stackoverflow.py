import requests
import pandas as pd
from datetime import datetime


def search_stackexchange(query, site, max_results=100, from_date=None, to_date=None):
    """
    Realiza buscas no Stack Exchange (ex. Stack Overflow, QA sites).
    :param query: Termos de busca no campo `intitle`.
    :param site: Nome do site (ex.: 'stackoverflow').
    :param max_results: Máximo de resultados a buscar (até o limite da API).
    :param from_date: Data de início (timestamp Unix).
    :param to_date: Data de fim (timestamp Unix).
    :return: Lista de links para os resultados encontrados.
    """
    print(f"Buscando resultados no {site} com a query: {query}")
    stack_links = []
    page = 1
    results_per_page = 30  # Máximo permitido por página pela API

    while len(stack_links) < max_results:
        try:
            # Configuração da URL e parâmetros da API
            url = "https://api.stackexchange.com/2.3/search"
            params = {
                "order": "desc",
                "sort": "activity",
                "intitle": terms,
                "site": site,
                "pagesize": results_per_page,
                "page": page,
            }

            # Adiciona intervalos de datas, se fornecidos
            if from_date:
                params["fromdate"] = from_date
            if to_date:
                params["todate"] = to_date

            # Requisição à API
            response = requests.get(url, params=params)
            if response.status_code == 200:
                results = response.json()
                items = results.get("items", [])
                stack_links.extend([item["link"] for item in items])
                print(f"Resultados na página {page}: {len(items)}")

                # Se não houver mais resultados, interromper o loop
                if not items or len(items) < results_per_page:
                    print("Todos os resultados foram coletados.")
                    break
            else:
                print(f"Erro na requisição: {response.status_code} - {response.text}")
                break

        except Exception as e:
            print(f"Erro ao buscar na página {page}: {e}")
            break

        # Avançar para a próxima página
        page += 1

    # Limitar a lista ao número máximo de resultados permitido
    return stack_links[:max_results]


# Configuração da busca
terms = [
    "big data",
    "data quality",
    "test",
    "testing",
    "tools",
]  # Termos de busca no título
sites = [
    "stackoverflow",
    "softwareengineering.stackexchange",
    "sqa.stackexchange",
]  # Sites da rede Stack Exchange
max_results = 100  # Número máximo de resultados por termo e site

# Configuração de intervalo de datas (últimos 5 anos)
from_date14 = int(datetime(2014, 1, 1).timestamp())  # Início em 1 de janeiro de 2014
to_date14 = int(datetime(2019, 12, 31).timestamp())  # Fim em 1 de janeiro de 2019

# Configuração de intervalo de datas (últimos 5 anos)
from_date20 = int(datetime(2020, 1, 1).timestamp())
to_date20 = int(datetime(2020, 12, 31).timestamp())

from_date21 = int(datetime(2021, 1, 1).timestamp())
to_date21 = int(datetime(2021, 12, 31).timestamp())

from_date22 = int(datetime(2022, 1, 1).timestamp())
to_date22 = int(datetime(2022, 12, 31).timestamp())

from_date23 = int(datetime(2023, 1, 1).timestamp())
to_date23 = int(datetime(2023, 12, 31).timestamp())

from_date = int(datetime(2024, 1, 1).timestamp())
to_date = int(datetime(2024, 12, 31).timestamp())

all_links = []

for site in sites:
    for term in terms:
        links = search_stackexchange(term, site, max_results, from_date, to_date)
        all_links.extend(links)

# Salvando os resultados em um arquivo CSV
if all_links:
    df = pd.DataFrame(all_links, columns=["Link"])
    output_file = "stackexchange_results_2024.csv"
    df.to_csv(output_file, index=False)
    print(f"Todos os links salvos em '{output_file}'. Total de links: {len(all_links)}")
else:
    print("Nenhum link foi encontrado.")
