import pandas as pd

def df_perguntas(perguntas, df):


    pergunta_df = df.copy()    
    colunas_a_manter = [pergunta_df.columns[0]]
    # Primeiro vou manter somente as colunas que possuem o prefixo desejado para cada pergunta
    # Também vou manter o ID para manter uma referência única
    for pergunta in perguntas:
        colunas = [coluna for coluna in pergunta_df.columns if f'{pergunta}' in coluna]
        colunas_a_manter.extend(colunas)
    pergunta_df = pergunta_df[colunas_a_manter]
    # Agora vou retirar os prefixo do início do nome das colunas
    #Além disso farei diversos filtros para manter uma DF com colunas o mais limpas possiveis 
    novas_colunas = {}
    for coluna in pergunta_df.columns:
        palavras = coluna.split("',")
        aux_coluna = palavras[-1].strip("')")
        aux_coluna_2 = aux_coluna.replace("'","")
        aux_coluna_3 = aux_coluna_2.strip()
        coluna_nova = aux_coluna_3.replace('_',' ')
        novas_colunas[coluna] = coluna_nova
    pergunta_df = pergunta_df.rename(columns=novas_colunas)

    return pergunta_df 