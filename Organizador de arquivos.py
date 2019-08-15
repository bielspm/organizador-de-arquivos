import os
import shutil

caminho = os.path.dirname(os.path.abspath(__file__))
filelist = os.listdir(caminho)
imagens_type = ('.png','.jpeg','.jpg')
word_type = ('.docx','.doc')
#HTML
for arquivo in filelist:
    if arquivo.endswith('.html') and os.path.isfile(arquivo):
        html_dir = os.path.join(caminho,'arquivos\\html')
        try:
            os.makedirs(html_dir)
        except FileExistsError as erro:
            continue
        finally:
            shutil.move(os.path.abspath(arquivo),html_dir)
#Imagem
    elif arquivo.endswith(imagens_type) and os.path.isfile(arquivo):
        imag_dir = os.path.join(caminho,'arquivos\\imagem')
        try:
            os.makedirs(imag_dir)
        except FileExistsError as erro:
            continue
        finally:
            shutil.move(os.path.abspath(arquivo),imag_dir)
#word
    elif arquivo.endswith(word_type) and os.path.isfile(arquivo):
        word_dir = os.path.join(caminho,'arquivos\\word')
        try:
            os.makedirs(word_dir)
        except FileExistsError as erro:
            continue
        finally:
            shutil.move(os.path.abspath(arquivo),word_dir)
