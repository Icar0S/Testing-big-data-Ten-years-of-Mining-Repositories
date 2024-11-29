import pandas as pd

# Nome do arquivo de entrada (CSV original)
input_file = "all_posts_mined.csv"

# Nome do arquivo de saída (CSV limpo)
output_file = "cleaned_all_posts_mined.csv"

# Lendo o arquivo CSV
try:
    data = pd.read_csv(input_file)

    # Verificando se o arquivo possui apenas uma coluna
    if data.shape[1] != 1:
        raise ValueError("O arquivo CSV deve conter exatamente uma coluna.")

    # Removendo duplicatas
    cleaned_data = data.drop_duplicates()

    # Salvando os dados limpos em um novo arquivo CSV
    cleaned_data.to_csv(output_file, index=False)
    print(
        f"Arquivo limpo salvo como '{output_file}'. Total de linhas: {len(cleaned_data)}"
    )

except FileNotFoundError:
    print(f"Erro: Arquivo '{input_file}' não encontrado.")
except ValueError as ve:
    print(f"Erro: {ve}")
except Exception as e:
    print(f"Erro inesperado: {e}")
