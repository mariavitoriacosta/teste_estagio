import pandas as pd

dfDataset = pd.read_excel('dataset.xlsx')
print(dfDataset)

porcentagem = 75

valor_correspondente = (dfDataset[dfDataset['Quality'].max() * (porcentagem/100)])

Quality_ok = (dfDataset[dfDataset['Quality'] > valor_correspondente ])

Status = dfDataset['Quality_ok']
print(Status)