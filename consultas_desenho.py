import pandas as pd
import json

with open(r'C:\Users\Thiago\OneDrive\Desktop\teiu\pandas_json\rick_morty.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

df = pd.json_normalize(dados['results'])

#Exercício 1 — Quantos personagens?
#print(f"O TOTAL DE PERSONAGENS É : {len(df)}")
#print(df[['id', 'name', 'status', 'species', 'gender']].head())


#Exercício 2 — Filtrar vivos
vivos = df[df['status'] == "Alive"]
#print(f"A QUANTIDADE DE PERSONAGENS VIVOS É : {len(vivos)}")
#print(vivos[['name', 'species']])

#Exercício 3 — Agrupar por espécie
especies = df.groupby('species')['id'].count().sort_values(ascending=False)
print("Quantidade por espécie:")
print(especies) 