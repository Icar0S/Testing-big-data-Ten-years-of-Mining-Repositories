import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

# Lista de palavras-chave relacionadas a ferramentas e métodos de teste
test_tools = [
    "JUnit",
    "Selenium",
    "TestNG",
    "Mockito",
    "Cucumber",
    "JUnit 5",
    "Appium",
    "Postman",
    "JUnit",
    "RestAssured",
    "Jest",
    "Mocha",
]
test_methods = [
    "Test-Driven Development",
    "Behavior-Driven Development",
    "Exploratory Testing",
    "Regression Testing",
    "Unit Testing",
    "Integration Testing",
    "Acceptance Testing",
    "Smoke Testing",
    "Load Testing",
]


# Função para acessar um link e escanear seu conteúdo
def scan_page_for_keywords(url):
    print(f"Acessando: {url}")
    tools_found = []
    methods_found = []

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            page_content = response.text
            soup = BeautifulSoup(page_content, "html.parser")

            # Convertendo o conteúdo da página para minúsculas para facilitar a busca
            page_text = soup.get_text().lower()

            # Procurando por ferramentas de teste
            for tool in test_tools:
                if re.search(r"\b" + re.escape(tool.lower()) + r"\b", page_text):
                    tools_found.append(tool)

            # Procurando por métodos de teste
            for method in test_methods:
                if re.search(r"\b" + re.escape(method.lower()) + r"\b", page_text):
                    methods_found.append(method)

    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")

    # Retorna as ferramentas e métodos encontrados
    return tools_found, methods_found


# Carregar os links do CSV original
input_csv = (
    "cleaned_all_posts_mined.csv"  # Altere para o caminho correto do seu CSV com links
)
output_csv = "posts_with_test_tools_and_methods.csv"  # Nome do novo CSV

df_links = pd.read_csv(input_csv)

# Lista para armazenar os resultados
results = []

# Iterar sobre os links e buscar as palavras-chave
for index, row in df_links.iterrows():
    url = row["Link"]

    # Escanear o link em busca das palavras-chave
    tools_found, methods_found = scan_page_for_keywords(url)

    # Adicionar os resultados à lista
    results.append(
        {
            "link": url,
            "ferramentas": ", ".join(tools_found),
            "metodo": ", ".join(methods_found),
        }
    )

# Criar um DataFrame com os resultados
df_results = pd.DataFrame(results)

# Salvar os resultados em um novo arquivo CSV
df_results.to_csv(output_csv, index=False)

print(f"Processamento concluído. Os resultados foram salvos em '{output_csv}'.")
