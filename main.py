import pandas as pd


# Lê os arquivos CSV
esus = pd.read_csv('cadastros_vinculados_esus_sede_1.csv', sep=';', encoding='latin1', skiprows=17)
sisab = pd.read_csv('cadastros_nao_validados_sisab_sede_1.csv', sep=';', encoding='latin1', skiprows=10)

# Lista de nomes exatamente como estão
nomes1 = esus['Nome']
nomes2 = sisab['Nome']

# Verifica se os nomes do primeiro arquivo estão no segundo
sisab['status'] = nomes2.isin(nomes1)

# Salva os resultados se desejar
sisab.to_csv('resultado.csv', sep=';', index=False)