import pandas as pd
# Importando os Dados para Análise
dados = pd.read_csv('aluguel.csv', sep=';')

# Criando uma seleção para tipos de residencias
residencial = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Casa de Vila']
selecao = dados['Tipo'].isin(residencial)
dados_residencial = dados[selecao]
dados_residencial.index = range(dados_residencial.shape[0])

# Exportando os dados
dados_residencial.to_csv('Dados Residenciais', sep=';', index=False)
dados_2 = pd.read_csv('Dados Residenciais', sep=';')

# Seleção de imóveis classificados como: 'Apartamento'
selecao = dados_residencial['Tipo'] == 'Apartamento'
n1 = dados_residencial[selecao].shape[0]
print(f'Existem {n1} apartamentos disponíveis!')

# Seleção de imóveis classificados como: 'Casa', 'Casa de Condomínio' e ' Casa de Vila'
selecao = (dados_residencial['Tipo'] == 'Casa') | (dados_residencial['Tipo'] == 'Casa de Condomínio') | (dados_residencial['Tipo'] == 'Casa de Vila')
n2 = dados_residencial[selecao].shape[0]
print(f'Existem {n2} Casas disponíveis!')

# Seleção de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites:
selecao = (dados_residencial['Area'] >= 60) & (dados_residencial['Area'] <= 100)
n3 = dados_residencial[selecao].shape[0]
print(f'Existem {n3} imóveis entra 60 e 100 metros quadrados disponíveis')

# Seleção de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00:
selecao = (dados_residencial['Quartos'] >= 4) & (dados_residencial['Valor'] < 2000)
n4 = dados_residencial[selecao].shape[0]
print(f'Existem {n4} imóveis com 4 Quartos e Aluguel ate R$ 2.000,00')