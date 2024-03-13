import pandas as pd

# Nome do arquivo .txt
nome_arquivo_txt = "BitRateNAC.txt"

# Ler o conteúdo do arquivo .txt
with open(nome_arquivo_txt, "r") as arquivo:
    texto = arquivo.read()

# Separar as linhas do texto
linhas = texto.split("\n")

# Dividir cada linha em colunas usando o ponto e vírgula como separador
dados = [linha.split(";") for linha in linhas]

# Criar um DataFrame com os dados
df = pd.DataFrame(dados, columns=["Música", "kBits/s", "Hz"])

# Criar um arquivo Excel e salvar os dados nele
nome_arquivo_excel = "dados_musicas.xlsx"
df.to_excel(nome_arquivo_excel, index=False)

print(f"Dados salvos no arquivo {nome_arquivo_excel} com sucesso!")
