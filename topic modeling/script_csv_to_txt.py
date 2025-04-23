import pandas as pd

# Nome do arquivo CSV de entrada
input_csv = (
    "../data/aggregates_unique_links.xls"  # Substitua pelo caminho do seu arquivo CSV
)
output_txt = "./docs/miner_posts/output_file.txt"  # Nome do arquivo de saída .txt

# Carregar o CSV
df = pd.read_csv(input_csv)

# Abrir o arquivo .txt para escrita
with open(output_txt, "w", encoding="utf-8") as file:
    for index, row in df.iterrows():
        # Combinar os valores de cada linha do DataFrame em uma string
        row_text = ", ".join([str(value) for value in row.values])

        # Escrever a linha no arquivo de texto
        file.write(row_text + "\n")

print(f"Conversão concluída. O arquivo foi salvo como '{output_txt}'.")
