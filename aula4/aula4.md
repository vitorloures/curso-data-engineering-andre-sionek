# Aula 4: Transformação de dados com PySpark

Tópicos tratados em aula:
- Criação de cluster EMR em IaC
- Change Data Capture (CDC)
- Técnicas de replicação de banco de dados
- AWS GLUE e ATHENA
- DataBricks

---
## Bizu de conexão com RDS Amazon

RDS -> Databases -> db_name:

- endpoint = host

---

## RDMS

- Podemos usar um recurso chamado binlog, para gravar todas as mudanças 
feitas num banco de dados. A partir do binlog, um Database Migration Service
  (DMS) - Logminer ou Debezium - ajuda na migração para um Data Lake 
  (append only) ou Data Warehouse. 
  Não é uma boa estratégia armazenar todos os dados no DW, porque
  esse serviço de armazenamento é mais caro. 
  
### Change Data Capture (CDC)

Leitura de binlogs para detectar mudanças na Db.

### Replication Instance

Instância de máquina virtual responsável por ler mudanças numa Db e escreve-las
em outra. É constituída por:

- Endpoint Source
- Replication Task 
- Endpoint Target

Num estágio de negócios em que não se justifica a criação de um Data Lake, o
qual é custoso de criar e manter, para DBs focadas em Online Transactional
Processing (OLTP), devemos manter uma cópia dos bancos de produção, de forma 
que os analistas de dados nunca façam queries nos bancos de produção. Queries 
criam Locks nas tabelas em questão, e podem impedir registros de serem feitos 
e comitados pela aplicação. 

A tarifa do Replication Instance, operada pelo AWS DMS é feita pelo número de horas
e tamanho da instância escolhida, semelhante ao EC2. 

---

## AWS GLUE e AWS ATHENA

O AWS GLUE Data Catalog implementará um crawler que lê 
metadados do Bucket S3 e registra num catálogo
de dados. Ele também pode ser usado como ferramenta serverless de ETL (análogo ao Dataflow). 
Na IaC devemos explicitar que Glue depende da existência do 
"Raw Database". O GLUE é uma implementação da AWS do Hive. 

O AWS Athena é uma ferramenta interligada com o Glue. Ele permite fazer queries 
diretamente em Buckets. O preço desse serviço é pela quantidade de Dados escaneado. 

---

## DataBricks

Usamos no curso, um cluster da Databricks para o processamento em Spark. 
A Databricks oferece um excelente serviço e facilidades que a configuração de cluster
na AWS não dispõe. A máquinas rodam na AWS, porém gerenciadas pelo Databricks. 

DataBricks cluster possui um próprio sistema de arquivos (databricks file system - DBFS)
baseado no HDFS. Possui também serviço de notebook conectado ao cluster.

Nessa aula, usamos o Spark para inferir esquema de arquivo JSON, 
criar views a partir disso, transformar arquivos originais num PARQUET,
e particionar pela data no processamento em Batch. Vimos também o modo de 
processamento em "Streaming" do Databricks, que na verdade é um processamento 
em mini-Batches, não streaming, de fato. 

Para o processamento em streaming, precisamos de antemão, especificar o esquema. 
O Stream salva um arquivo checkpoint, onde mostra o que já foi, e o que não foi 
processado. Isso ajuda na recuperação no caso de falhas. 

### Comparação DataBricks e EMR:

(https://www.confessionsofadataguy.com/databricks-vs-aws-emr-theory-and-real-life/)

TL;DR:

- Making using Spark at scale so easy anyone can do it. 
- Provide less technical people access to the power of Spark at scale. Think DS and other Analysts via Notebooks.
- Provide built in Data Warehouse support (Delta Lake).
- Provide tools for developers to make life easy. (APIs, Integrations, features.)

---

### Extra:

- Ferramenta de Desenho usada em aula: excalidraw.io

---
