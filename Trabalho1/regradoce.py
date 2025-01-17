import json
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

arquivo_json = r'.\exerc2.json'

meuSet = set()
data = []

with open(arquivo_json, 'r', encoding='utf-8') as f:
    dados = json.load(f)

for i, item in enumerate(dados):
    for compra in item["produtos"]:
        meuSet.add(compra)

itens_ordenados = sorted(list(meuSet))

for i, item in enumerate(dados):
    data.append([False] * len(itens_ordenados))
    for j, produto in enumerate(itens_ordenados):
        if(produto in item["produtos"]):
            data[i][j] = True

df = pd.DataFrame(data, columns=itens_ordenados)

df.to_csv('dataFrameDoce.csv', index=False)

itens_frequentes = apriori(df, min_support=0.03, use_colnames=True)

rules = association_rules(itens_frequentes, metric='confidence', min_threshold=0.5)

regras_consequentes = rules[rules['consequents'].apply(lambda x: 'Doce' in x)]

print("Conjuntos frequentes:")
print(itens_frequentes)

print("\nRegras onde 'Doce' é um consequente:")
print(regras_consequentes)