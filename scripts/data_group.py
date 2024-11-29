import pandas as pd
import os

# Diretório onde estão os arquivos CSV
csv_directory = (
    "/content/CSVs"  # Altere para o caminho correto onde seus CSVs estão localizados
)

# Lista de arquivos CSV no diretório
csv_files = [f for f in os.listdir(csv_directory) if f.endswith(".csv")]

# Inicializa uma lista para armazenar os dataframes
dfs = []

# Carrega cada CSV e adiciona à lista de dataframes
for csv_file in csv_files:
    file_path = os.path.join(csv_directory, csv_file)
    print(f"Lendo o arquivo {csv_file}...")
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatena todos os dataframes em um único dataframe
all_posts_df = pd.concat(dfs, ignore_index=True)

# Salva o dataframe concatenado em um único CSV
output_file = "all_posts_mined.csv"
all_posts_df.to_csv(output_file, index=False)

print(
    f"Todos os links foram combinados em '{output_file}'. Total de links: {len(all_posts_df)}"
)
