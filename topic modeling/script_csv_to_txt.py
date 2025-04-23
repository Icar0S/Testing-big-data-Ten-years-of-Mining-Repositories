import pandas as pd

# Nome do arquivo CSV de entrada
input_file = "../data/extracted_posts_with_content.xls"  # Substitua pelo caminho do seu arquivo CSV
output_txt = "./docs/miner_posts/output_file.txt"  # Nome do arquivo de saída .txt

# Carregar o XLS com pandas
df = pd.read_csv(input_file)

# Abrir o arquivo .txt para escrita
with open(output_txt, "w", encoding="utf-8") as file:
    for index, row in df.iterrows():
        # Combinar Titulo e Conteudo com tabulação
        row_text = "\t".join([str(row["Titulo"]).strip(), str(row["Conteudo"]).strip()])
        file.write(row_text + "\n")

print(f"Conversão concluída. O arquivo foi salvo como '{output_txt}'.")
