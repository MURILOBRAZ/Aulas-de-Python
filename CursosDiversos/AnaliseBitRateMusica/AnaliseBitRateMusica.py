from tinytag import TinyTag 
import os

#diretorio = str(input("Insira o diretório das músicas:\n"))
#diretorio_lista = str(input("Insira o diretório onde sera salvo o txt:\n"))
diretorio = input("Insira o Diretório das Musicas: ")

# Verifica se o diretório informado existe
if os.path.exists(diretorio):
    print(f"O diretório {diretorio} existe.")
    # Faça alguma ação com o diretório aqui
    def get_file_name_by_position(diretorio, position):
        files = os.listdir(diretorio)
        if 0 <= position < len(files):
            return files[position]
        else:
            return None

    def get_file_names_by_positions(diretorio, positions):
        file_names = [get_file_name_by_position(diretorio, pos) for pos in positions]
        return file_names


    # diretorio = "C:/Users/TECNICA/Documents/MB/INTERNACIONAL"

    lista_musicas = os.listdir(diretorio)

    texto = open('BitRate.txt','w')
    textoERRO = open('Erros.txt', 'w')
    aux = 1
    aux2 = 0
    for arquivo in lista_musicas:
        aux2 += 1
        positions = [aux2]
        file_names = get_file_names_by_positions(diretorio, positions)
        try:
            audio = TinyTag.get(diretorio + "/" + arquivo)
            texto.write(arquivo + ";" + str(round(audio.bitrate)) + " kBits/s;" + str(round(audio.samplerate)) +" Hz" + "\n")
            aux += 1
            if aux == len(lista_musicas):
                print("Ultimo Item Verificado foi o N° " + str(aux))
            #print(arquivo + ";" + str(round(audio.bitrate)) + " kBits/s;" + str(round(audio.samplerate)) +" Hz" + "\n")
        except:
            for i, file_name in enumerate(file_names):
                if file_name:
                    print(f'{positions[i]} {file_name}')
                    print('Error no arquivo n° ' + f'{positions[i]} {file_name}')
                    textoERRO.write('Error no arquivo n° ' + f'{positions[i]} {file_name}' + '\n')
    texto.close()
    textoERRO.close()
    print("Tamanho da Lista é " + str(len(lista_musicas)))
    print('PROGRAMA CONCLUÍDO!!!')
    os.system("PAUSE")
else:
    print("O diretório informado não existe.")
    os.system("PAUSE")