import json
#CRIANDO O ARQUIVO
livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "paginas": 256, "lido": True},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "paginas": 328, "lido": True},
    {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "ano": 1937, "paginas": 310, "lido": False},
    {"titulo": "O Chamado de Cthulhu", "autor": "H.P. Lovecraft", "ano": 1928, "paginas": 45, "lido": True},
    {"titulo": "Neuromancer", "autor": "William Gibson", "ano": 1984, "paginas": 271, "lido": False},
]

#Transformar em DataFrame (Pandas)
import pandas as pd
df = pd.DataFrame(livros)

# QUERYS
#ostre a média de páginas
media_paginas = df['paginas'].mean()
print(f"A MEDIA DE PÁGINAS DOS LIVROS É {media_paginas}")

#Filtre apenas os livros lidos
lidos = df[df['lido'] ==  True ]
print(f"APENAS OS LIVROS LIDOS SÃO: ")
print(lidos)

mais_velho = df[df['ano'] == df['ano'].min()]
print(f"O LIVRO MAIS ANTIGO É : {mais_velho}")

#Conte quantos livros por autor
autor_livros = df['autor'].value_counts()
print(autor_livros)

#EXPORTANDO PARA JSON
df.to_json('livros.json', orient='records', force_ascii=False)
print("ARQUIVANDO COM SUCESSSO :)")
