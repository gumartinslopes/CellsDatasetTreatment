from PIL import Image
import os

def jpg_to_png(input_dir, output_dir):
    # Verifica se o diretório de saída existe, se não, cria
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Percorre o diretório de entrada
    for root, _, files in os.walk(input_dir):
        for file in files:
            # Verifica se o arquivo é JPEG
            if file.lower().endswith(".jpg"):
                # Caminho completo do arquivo de entrada
                input_path = os.path.join(root, file)
                # Caminho completo do arquivo de saída (com a extensão .png)
                output_path = os.path.join(output_dir, os.path.splitext(file)[0] + ".png")

                # Abre a imagem JPEG
                image = Image.open(input_path)
                # Salva a imagem como PNG
                image.save(output_path, "PNG")
                print(f"{input_path} convertido para PNG.")

# Diretório de entrada (onde estão as imagens JPEG)
input_directory = "../NegativeMasksJpg"
# Diretório de saída (onde as imagens PNG serão salvas)
output_directory = "../NegativeMasks"

# Chama a função para converter as imagens
jpg_to_png(input_directory, output_directory)