import pandas as pd

df = pd.read_json(r'C:\Users\Thiago\OneDrive\Desktop\teiu\pandas_json\countries.json')
# Os dados estão dentro da chave 'countries'

#QUERYS
"""
Exercício 1 — Explorar
Quantos países existem?

Quais são as colunas?

Qual país tem a maior população?

Qual país tem a menor população?
"""
print(f"QUANTIDADE DE PAÍSES É : {len(df['countries'])} ")
pais_mais_gente = df[df['population'] == df['population'].max()]
print(pais_mais_gente[['name', 'capital', 'population']])

pais_menos_gente = df[df['population'] == df ['population'].min()]
print(pais_menos_gente[['name', 'capital', 'population']])