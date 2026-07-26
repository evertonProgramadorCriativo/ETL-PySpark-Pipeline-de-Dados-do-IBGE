
# Fluxo de execução deste arquivo

#  Exibe "Ingestão concluída com sucesso."
#  Atualiza o arquivo _metadata.json
#  salvar_metadados(caminho, quantidade, timestamp) ->
#  Salva o JSON bruto na pasta data/raw  ->
#  salvar_raw(dados, timestamp) ->
#  Recebe os dados em formato JSON (lista) ->
#  Faz uma requisição HTTP para a API do IBGE ->
#  extrair_dados_ibge() ->
#  Gera um timestamp único da execução ->
#  main() 

# Importa a biblioteca JSON.
# Será utilizada para converter objetos Python em arquivos JSON
# e também para ler arquivos JSON.
import json

# Importa a biblioteca responsável por manipular
# diretórios, caminhos e arquivos do sistema operacional.
import os

# Importa a classe datetime responsável por trabalhar com datas.
# Importa também timezone para utilizar horário UTC.
from datetime import datetime, timezone

# Importa a biblioteca Requests.
# Ela será utilizada para fazer requisições HTTP para a API do IBGE.
import requests



# CONFIGURAÇÕES DA APLICAÇÃO

# Armazena em uma constante a URL da API SIDRA do IBGE.
# Essa URL retorna a população estimada dos municípios brasileiros.
SIDRA_URL = "https://apisidra.ibge.gov.br/values/t/6579/n6/all/v/9324/p/last"

# Monta automaticamente o caminho da pasta onde os arquivos
# JSON serão armazenados.
RAW_DIR = os.path.join(

    # Obtém a pasta onde este arquivo Python está localizado.
    os.path.dirname(__file__),

    # Volta uma pasta acima.
    "..",

    # Entra na pasta data.
    "data",

    # Entra na pasta raw.
    "raw"
)

print(SIDRA_URL)
print(RAW_DIR)