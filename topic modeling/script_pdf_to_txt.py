import os
from io import BytesIO
import aspose.words as aw

# Caminho para a pasta com os PDFs
input_folder = "./docs/data/articles_test"
output_folder = "./docs/text/test"

# Certifique-se de que a pasta de saída existe
os.makedirs(output_folder, exist_ok=True)

# Percorrer todos os arquivos .pdf na pasta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        # Caminho completo do arquivo PDF
        pdf_path = os.path.join(input_folder, filename)

        try:
            # Criar o fluxo de bytes a partir do arquivo PDF
            with open(pdf_path, "rb") as file:
                file_stream = BytesIO(file.read())

            # Carregar o documento PDF usando o fluxo de bytes
            pdf = aw.Document(file_stream, None)

            # Criar o caminho para salvar o arquivo de texto, com o mesmo nome do arquivo PDF
            output_filename = f"{os.path.splitext(filename)[0]}.txt"
            output_path = os.path.join(output_folder, output_filename)

            # Salvar o conteúdo do PDF em um arquivo de texto
            with open(output_path, "wb") as output_file:
                pdf_stream = BytesIO()

                # Salve o conteúdo em formato texto (SaveFormat.TEXT)
                pdf.save(pdf_stream, aw.SaveFormat.TEXT)

                # Escreva o conteúdo no arquivo de saída
                output_file.write(pdf_stream.getvalue())

            print(f"Arquivo convertido e salvo: {output_path}")

        except Exception as e:
            # Em caso de erro, imprimir o erro e continuar com o próximo arquivo
            print(f"Erro ao processar o arquivo {filename}: {e}")
            continue
