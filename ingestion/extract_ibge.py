# Fluxo de execução deste arquivo

# Inicia a execução da aplicação.
# main()

# Gera um timestamp único da execução.

# Chama extrair_dados_ibge().

# Faz uma requisição HTTP para a API do IBGE.

# Recebe os dados em formato JSON (lista).

# Chama salvar_raw(dados, timestamp).

# Salva o JSON bruto na pasta data/raw.

# Chama salvar_metadados(caminho, quantidade, timestamp).

# Atualiza o arquivo _metadata.json.

# Exibe a mensagem:
# "Ingestão concluída com sucesso."

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



# FUNÇÃO RESPONSÁVEL POR BUSCAR DADOS DA API

# Define uma função chamada extrair_dados_ibge().
# Ela retorna um objeto do tipo dict.
def extrair_dados_ibge() -> dict:

    # Exibe qual URL será consultada.
    print(f"Buscando dados em: {SIDRA_URL}")

    # Faz uma requisição HTTP GET para a API.
    # timeout=30 significa aguardar no máximo 30 segundos.
    resposta = requests.get(
        SIDRA_URL,
        timeout=30
    )

    # Caso a resposta seja diferente de 200,
    # gera automaticamente uma exceção.
    resposta.raise_for_status()

    # Converte o JSON recebido em um objeto Python.
    dados = resposta.json()

    # Exibe quantos registros foram retornados.
    print(
        f"Requisição concluída. Registros retornados: {len(dados)}"
    )

    # Retorna os dados para quem chamou a função.
    return dados



# FUNÇÃO RESPONSÁVEL POR SALVAR O JSON BRUTO

# Recebe os dados e o timestamp.
# Retorna o caminho do arquivo salvo.
def salvar_raw(
    dados: list,
    timestamp: str
) -> str:

    # Cria a pasta RAW caso ela ainda não exista.
    # exist_ok=True evita erro caso a pasta já exista.
    os.makedirs(
        RAW_DIR,
        exist_ok=True
    )

    # Monta o caminho completo do arquivo JSON.
    caminho_arquivo = os.path.join(

        RAW_DIR,

        f"ibge_populacao_{timestamp}.json"
    )

    # Abre o arquivo para escrita.
    with open(

        caminho_arquivo,

        "w",

        encoding="utf-8"

    ) as f:

        # Escreve o conteúdo JSON no arquivo.
        json.dump(

            dados,

            f,

            ensure_ascii=False,

            indent=2
        )

    # Exibe onde o arquivo foi salvo.
    print(
        f"Dados brutos salvos em: {caminho_arquivo}"
    )

    # Retorna o caminho do arquivo criado.
    return caminho_arquivo



# FUNÇÃO RESPONSÁVEL POR SALVAR METADADOS

def salvar_metadados(

    caminho_arquivo: str,

    quantidade_registros: int,

    timestamp: str

) -> None:

    # Define o caminho do arquivo de metadados.
    caminho_metadados = os.path.join(

        RAW_DIR,

        "_metadata.json"
    )

    # Cria um dicionário contendo informações da execução.
    novo_registro = {

        # Data e hora da execução.
        "timestamp": timestamp,

        # URL da fonte dos dados.
        "fonte": SIDRA_URL,

        # Nome do arquivo JSON salvo.
        "arquivo": os.path.basename(caminho_arquivo),

        # Quantidade de registros retornados.
        "quantidade_registros": quantidade_registros,
    }

    # Cria uma lista vazia.
    historico = []

    # Verifica se o arquivo de metadados já existe.
    if os.path.exists(caminho_metadados):

        # Abre o arquivo existente.
        with open(

            caminho_metadados,

            "r",

            encoding="utf-8"

        ) as f:

            # Carrega o conteúdo JSON para memória.
            historico = json.load(f)

    # Adiciona o novo registro ao histórico.
    historico.append(novo_registro)

    # Abre novamente o arquivo para escrita.
    with open(

        caminho_metadados,

        "w",

        encoding="utf-8"

    ) as f:

        # Salva o histórico atualizado.
        json.dump(

            historico,

            f,

            ensure_ascii=False,

            indent=2
        )

    # Exibe mensagem informando sucesso.
    print(
        f"Metadados atualizados em: {caminho_metadados}"
    )



# FUNÇÃO PRINCIPAL

# Define a função principal do programa.
def main() -> None:

    # Obtém a data e hora atual em UTC.
    # Depois converte para uma string no formato:
    # AAAAMMDDTHHMMSSZ
    timestamp = datetime.now(
        timezone.utc
    ).strftime("%Y%m%dT%H%M%SZ")

    # Busca os dados na API do IBGE.
    dados = extrair_dados_ibge()

    # Salva os dados brutos em arquivo JSON.
    caminho_arquivo = salvar_raw(

        dados,

        timestamp
    )

    # Atualiza o arquivo de metadados.
    salvar_metadados(

        caminho_arquivo,

        len(dados),

        timestamp
    )

    # Exibe mensagem indicando sucesso.
    print(
        "Ingestão concluída com sucesso."
    )


# PONTO DE ENTRADA DA APLICAÇÃO

if __name__ == "__main__":

    # Executa toda a ETL de ingestão.
    main()