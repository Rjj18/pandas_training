import pandas as pd
import numpy as np
import matplotlib as plt


#criação de um data frame com base em um dicionário

lista = {
    "idDespesa": "string",
    "nomeDespesa": "test",
    "Valor": 123,
    "Descrição:": "descrição do valor",
    "Tipo": "Tipo da despesa",
    "Data": "01/01/2021",
    "Recorrência": "tipo",
    "Responsável": "Roger ou Aline"
}

df1 = pd.DataFrame(lista, index=[0]) # O dataframe é criado usando as chaves nas colunas e os valores como atribuitos. O index seria a quantidade de linhas que serão criadas.

df1


#criando o data frame do "0"
df2 = pd.DataFrame ({
    "Grupos": ["PEA_I","PEA_II", "PEA_III"],
    "Coordenador": ["Gianne", "Sueli", "Roger"],
    "Horário Inicio": ["11:55", "13:45", "19:00 "],
    "Horário Final": ["13:25", "15:15", "20:30"]
})


#inserindo linhas - com essa função insiro uma linha no final do dataframe
df2.loc[len(df2)] = ["test","test","test","test"]

#inserindo colunas - no final do dataframe
df2.insert(len(df2),"Local",["sala 15", "Sala SRM", "Sala Led", "test"])


#removendo colunas
df2.pop("Local")

#removendo linhas

df2.drop(index=0)

print(df2)
