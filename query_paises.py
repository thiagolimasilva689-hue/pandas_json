import pandas as pd

df = pd.read_json(r'C:\Users\Thiago\OneDrive\Desktop\teiu\pandas_json\countries.json')
# Os dados estão dentro da chave 'countries'


"""
Exercício 1 — Explorar
Quantos países existem?

Quais são as colunas?

Qual país tem a maior população?

Qual país tem a menor população?
"""
#

# Os dados estão dentro da chave 'countries' - use json_normalize
df = pd.json_normalize(df['countries'])

pais_mais_gente = df[df["population"] == df["population"].max()]
#print(pais_mais_gente[['name', 'capital', 'population']])

pais_menos_gente = df[df['population'] == df ['population'].min()]
#print(pais_menos_gente[['name', 'capital', 'population']])

"""
Exercício 2 — Filtrar por região
Filtre apenas países da Europa (region == 'Europe')

Quantos são?

Mostre nome, capital e população
"""
europa = df[df['region'] == 'Europe']
#print(f"QUANTIDADE DE PAÍSES NA EUROPA : {len(europa)} ")

#print(europa[['name', 'capital', 'population']])




#Exercício 3 — Agrupar por região
#Agrupe por region e:
#Conte quantos países por região
#Some a população total por região
#Qual região tem mais países? E mais população?
regioes = df.groupby('region')
# Agrupar por região
regioes = df.groupby('region')

# Contar países por região
paises_por_regiao = regioes['name'].count()
#print("PAÍSES POR REGIÃO:")
#print(paises_por_regiao)

# Somar população por região
populacao_por_regiao = regioes['population'].sum()
#print("\nPOPULAÇÃO POR REGIÃO:")
#print(populacao_por_regiao)

# Qual tem mais países?
#print(f"\nMais países: {paises_por_regiao.idxmax()} ({paises_por_regiao.max()})")

# Qual tem mais população?
#print(f"Mais população: {populacao_por_regiao.idxmax()} ({populacao_por_regiao.max()})")



#Exercício 4 — Buscar
#Filtre países com população acima de 100 milhões

#Quantos são?
 #100000000
#Mostre nome, região e população, ordenado do maior para o menor

# Filtrar os países com população > 100 milhões
paises_grandes = df[df["population"] > 100000000]
#print(f"Quantidade de países: {len(paises_grandes)}")
#
ordenado = paises_grandes.sort_values(by='population', ascending=False)
#print(ordenado[['name', 'capital', 'population']])
"""



Exercício 5 — Moeda
Quantos países usam o Euro (EUR)?

Liste os nomes
"""
moeda_euro = df[df['currency'] == 'EUR']
print(f"QUANTIDADE DE PAISES AONDE SE USAR O EURO COMO MOEDA PRINCIPAL É : {len(moeda_euro)}")


print("OS PAISES QUE USAM O EURO SÃO : ")
print(moeda_euro[['name', 'capital', 'population']])
