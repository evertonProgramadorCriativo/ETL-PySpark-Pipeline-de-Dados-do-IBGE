# ETL com PySpark, SQL e PostgreSQL

Pipeline ETL desenvolvido para praticar conceitos fundamentais de Engenharia de Dados utilizando **PySpark**, **SQL**, **PostgreSQL** e **Docker**.

O projeto realiza todo o fluxo de processamento de dados, desde a extração de informações públicas do IBGE até o carregamento em um banco de dados relacional, simulando um pipeline utilizado em ambientes corporativos.

Todo o ambiente é executado em containers Docker, permitindo que o projeto seja reproduzido sem instalar Spark ou PostgreSQL diretamente na máquina.

---

# Objetivo

O objetivo deste projeto é demonstrar na prática um pipeline de ETL (Extract, Transform and Load), aplicando conceitos comuns em Engenharia de Dados.

Durante a execução são realizadas as seguintes etapas:

- extração de dados da API pública do IBGE;
- armazenamento do arquivo bruto em formato JSON;
- leitura dos dados utilizando PySpark;
- limpeza e transformação dos registros;
- remoção de valores inválidos e duplicados;
- gravação dos dados processados em formato Parquet;
- carregamento dos dados no PostgreSQL;
- validação do resultado utilizando consultas SQL.

Esse projeto foi desenvolvido para praticar:

- PySpark
- SQL
- ETL
- processamento distribuído
- integração entre Spark e PostgreSQL
- documentação de esquemas de dados
- Docker

---

# Fluxo do Pipeline

```text
API do IBGE -> 
Extração dos dados (JSON) -> 
Camada Raw ->
 Transformação com PySpark -> 
 Camada Processada (Parquet) -> 
 Carga no PostgreSQL - 
 Validação utilizando SQL
     
 
```

---

# Tecnologias Utilizadas

## Python

Utilizado para realizar a comunicação com a API do IBGE e iniciar o processo de ingestão dos dados.

---

## PySpark

Responsável por todo o processamento dos dados.

Durante essa etapa são realizadas operações como:

- leitura do JSON
- seleção de colunas
- renomeação
- conversão de tipos
- tratamento de valores nulos
- remoção de registros duplicados
- agregações
- gravação em Parquet

---

## PostgreSQL

Banco de dados utilizado para armazenar os dados processados.

Após a transformação, o Spark grava os registros diretamente em uma tabela PostgreSQL utilizando JDBC.

---

## SQL

Utilizado para validar a carga realizada no banco.

Exemplos:

- contagem de registros
- consultas por município
- verificação de duplicidades
- validação de consistência

---

## Docker

Todo o ambiente é executado utilizando Docker Compose.

Os containers utilizados são:

- Spark
- PostgreSQL
- pgAdmin

---

## Jupyter Notebook

Utilizado para desenvolver e
 executar o pipeline de forma interativa .



# Esquema de Entrada

Origem dos dados:

- API SIDRA do IBGE

Formato recebido:

```
JSON
```

Exemplo de informações obtidas:

- código do município
- nome do município
- população estimada
- ano da estimativa

---

# Esquema de Saída

Após o processamento, os dados são gravados em duas camadas.

### Camada Processada

Formato:

```
Parquet
```

---

### Banco de Dados

Formato:

```
Tabela PostgreSQL
```

Exemplo de colunas:

```
id
codigo_municipio
municipio
ano
populacao
```

---

# Como Executar

## Clonar o repositório

```bash
git clone <url-do-repositorio>

cd etl-pyspark-basico
```

---

## Subir o ambiente

```bash
docker compose up -d
```

Verificar se todos os containers iniciaram corretamente.

```bash
docker compose ps
```

---

## Verificar os logs

```bash
docker compose logs
```

ou

```bash
docker compose logs -f
```

---

## Executar a ingestão

```bash
docker compose exec spark python work/ingestion/extract_ibge.py
```

Os arquivos JSON serão armazenados em:

```
data/raw
```

---

## Executar a transformação

Abrir o navegador:

```
http://localhost:8888
```

Token:

```
etl123
```

Executar o notebook:

```
notebooks/transformacao_dados.ipynb
```

---

## Executar a carga

Abrir:

```
notebooks/carga_dados.ipynb
```

Executar todas as células.

---

## Validar os dados

Abrir o pgAdmin:

```
http://localhost:5050
```

Login:

```
admin@admin.com
```

Senha:

```
admin
```

Consultar a tabela criada no PostgreSQL.

---

# Comandos Utilizados

### Subir os containers

```bash
docker compose up -d
```

### Parar os containers

```bash
docker compose down
```

### Remover containers e volumes

```bash
docker compose down -v
```

### Verificar containers

```bash
docker compose ps
```

### Verificar logs

```bash
docker compose logs
```

### Acompanhar logs em tempo real

```bash
docker compose logs -f
```

### Entrar no container Spark

```bash
docker compose exec spark bash
```

### Executar o script de ingestão

```bash
docker compose exec spark python work/ingestion/extract_ibge.py
```

### Entrar no PostgreSQL

```bash
docker compose exec postgres psql -U etl_user -d etl_db
```

### Listar tabelas

```sql
\dt
```

### Consultar registros

```sql
SELECT * FROM populacao_municipios;
```

### Contar registros

```sql
SELECT COUNT(*) FROM populacao_municipios;
```

---

# Validação dos Dados

Durante a execução do pipeline são realizadas verificações para garantir a qualidade dos dados.

São verificadas:

- valores nulos;
- registros duplicados;
- quantidade de registros antes e depois da transformação;
- consistência da carga no PostgreSQL.

---

## Autor

Desenvolvido por Everton Eduardo  