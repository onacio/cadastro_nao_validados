import pandas as pd


# Lê os arquivos CSV
df1 = pd.read_csv('esus.csv', sep=';', encoding='latin1', skiprows=17)
df2 = pd.read_csv('sisab.csv', sep=';', encoding='latin1', skiprows=10)

# Lista de nomes exatamente como estão
nomes1 = df1['Nome']
nomes2 = df2['Nome']

# Verifica se os nomes do primeiro arquivo estão no segundo
df2['presente_no_segundo'] = nomes2.isin(nomes1)

# Mostra os resultados
print(nomes1)

# Salva os resultados se desejar
df2.to_csv('comparacao_resultado.csv', index=False)