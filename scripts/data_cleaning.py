import pandas as pd

# Caminho do CSV original e do CSV limpo
input_csv = "posts_with_test_tools_and_methods.csv"  # Altere para o seu arquivo
output_csv = "cleaned_posts_with_test_tools_and_methods.csv"  # CSV com as linhas limpas

# Carregar o CSV original
df = pd.read_csv(input_csv)

# Excluir as linhas onde tanto 'ferramentas' quanto 'metodo' estão vazias
df_cleaned = df.dropna(subset=["ferramentas", "metodo"], how="all")

# Salvar o CSV limpo
df_cleaned.to_csv(output_csv, index=False)

print(
    f"CSV limpo salvo como '{output_csv}'. Total de linhas restantes: {len(df_cleaned)}"
)
