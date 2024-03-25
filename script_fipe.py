import pandas as pd
import requests

df = pd.read_csv(r'D:\Meus Documentos\Projetos Python\scripts\fipe tabela\NOME_DO_ARQUIVO', sep=';', encoding='utf8')

url_base = 'https://brasilapi.com.br/api/fipe/preco/v1/'

precos_veiculos = []

for index, row in df.iterrows():
    codigo_fipe = row['COLUNA_DO_CODIGO']
    ano_veiculo = row['COLUNA_DO_ANO']
    
    url = f'{url_base}{codigo_fipe}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        dados_veiculo = response.json()
        for dados in dados_veiculo:
            if dados['anoModelo'] == ano_veiculo:
                preco_veiculo = dados['valor']
                precos_veiculos.append(preco_veiculo)
                print(f"Preço encontrado para o veículo com código FIPE {codigo_fipe}, ano {ano_veiculo}: {preco_veiculo}")
                break
        else:
            print(f"Preço não encontrado para o veículo com código FIPE {codigo_fipe} e ano {ano_veiculo}")
            precos_veiculos.append(None)
    else:
        print(f"Erro na requisição para o veículo com código FIPE {codigo_fipe}")
        precos_veiculos.append(None)

df['Preço'] = precos_veiculos

df.to_csv(r'I:\# GAB\# Transportes - Dados SIGPlan\script frota python\COLUNA_RETORNO.csv', sep=';', index=False)
