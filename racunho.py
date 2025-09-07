import pandas as pd

# Carregar as planilhas
sisab = pd.read_excel("SISAB.xlsx")
esus = pd.read_csv("ESUS.csv", skiprows=17, sep=';', encoding='latin1')

# Supondo que a coluna com o nome do paciente se chame "Nome"
coluna_nome = "Nome"

# Verificar se os nomes da planilha A existem na planilha B
sisab["Existe_na_B"] = sisab[coluna_nome].isin(esus[coluna_nome])

# Salvar o resultado em uma nova planilha
sisab.to_excel("resultado_comparacao.xlsx", index=False)


print("Comparação concluída! Resultado salvo em 'resultado_comparacao.xlsx'")