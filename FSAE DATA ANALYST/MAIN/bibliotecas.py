import os
import shutil


def baixar_arquivo(destino):
    # Caminho do arquivo Segers.pdf no diretório do seu programa
    caminho_origem = "segers.pdf"

    # Verifica se o arquivo de origem existe
    if not os.path.isfile(caminho_origem):
        print("O arquivo Segers.pdf não foi encontrado no diretório do programa.")
        return

    # Verifica se o destino existe, se não, cria
    if not os.path.exists(destino):
        os.makedirs(destino)

    caminho_destino = os.path.join(destino, "segers.pdf")

    # Copia o arquivo para o destino
    shutil.copy(caminho_origem, caminho_destino)

    print(f'O arquivo Segers.pdf foi copiado com sucesso para {caminho_destino}')

    # Chama a função para copiar o arquivo Segers.pdf para o diretório do usuário

    
    # Substitua pelo caminho desejado
