# Aula 3: Data Lakes

Tópicos tratados em aula:   
- Conceitos de data lake
- Criação de datalake com IaC + Ingestão com  Firehose (Messaging as a Service)
- AWS Glue para catálogo de dados
- AWS Athena para queries sob demanda
- Redshift Spectrum

---
## Data Lake

Data Lake é um repositório centralizado que permite armazenar dados 
estruturados ou não 
estruturados em qualquer escala, e estabelecer políticas para governança
dos dados armazenados. Podem ser integrados ao DL ferramentas 
de Analytics, Big Data, Dashboards, ou Machine Learning. 

Data Lake mudou o paradigma de ETL para ELT. 

Data Lakes costumam ser organizados em camadas (e.g. Bronze / Raw, 
Silver / Processed, Gold / Curated)
para otimizar leitura de arquivos pela aplicação, pois esses 
sistemas são limitados por essas operações (IO constrained).

Na camada Gold, para dados relacionais, o mais indicado é o formato .parquet
, ou .delta (Databricks). Parquet é um formato comprimido, e possui metadados
para acelerar leitura e processamento de dados do DL. 

Uma boa prática é organizar partições do Bucket Raw (Bronze) por data de extração, 
já no bucket processed (Silver), ele deve ser otimizado para o tipo de data que
a aplicação deverá ler. Já a camada curated (Gold) é otimizada e armazenada segundo
as regras de negócio.

A aplicação de regras de negócio entre a camada processada e a camada curada, 
costuma ser feito por Analytics Engineers em times maiores e mais maduros. 

A camada Bronze armazenada dados com alguma padronização de campos, no formato 
em que foram ingeridos. E.g. csv, json, xml, etc. Essa camada costuma ser
acessadas por engenheiro de dados, jobs Spark e Athena. 

Bucket Raw (Bronze) costuma armazenar:
- parquet vindo de Db (Postgres)
- eventos; e.g. cliques de usuário; em 
- csvs de orquestrador (Airflow)

A camada Silver armazena dados em formato colunar (parquet, Avro, Orc) prontos 
para as regras de negócios serem aplicadas. Jobs Spark, Athena e DBT acessam essa camada.

A camada Gold armazena dados com regras de negócios aplicadas para determinado
propósito. São acessados por vários stakeholders. Podem ser servidos com Spark, 
EMR, Redshift, Presto, Athena, etc. Ferramentas de BI, DW, e Data Scientists
costumam fazer uso dessa camada.

OBS: Arquivos parquet não permitem update e delete. Seria necessário apagar o parquet
e escrever outro arquivo para essas operações. O formato .delta corrige esse 
problema e introduz as propriedades ACID na transação.

## Particionamento de DL

Um bom particionamento ajuda a reduzir custos de processamento ao limitar
a quantidade de arquivos e dados escaneados por ferramentas de Query (Prestom
Spark, Athena, etc). 

Poucas partições = Baixa Performance
Partições bem dimensionadas = Performance Ótima
Muitas partições = Baixa Performance

---

## Ferramentas pagas de ingestão de dados

São conectores que se conectam com várias fontes de dados largamente
usadas (e.g. Facebook Ads, Google Analytcs), cujas APIs mudam com frequência 
e a manutenção do sistema não é tão simples. Além disso, esses conectores
permitem a partir de serviços NoCode, transformações para o formato final
desejado. 

Exemplo de ferramentas: Fivetran, Singer, etc. 

---

## AWS Glue - Catálogo de dados 

O catálogo AWS Glue é um armazenamento persistente de metadados.

---

## Deploy

Para o Deploy, foi usado o AWS CDK. O AWS CDK necessita de uma repositório
vazio para executarmos o comando `cdk init --language python`. Em seguida,
ele criará arquivos de inicialização e um projeto python com suas dependências. 
O melhor uso de técnica de IaC é criarmos um projeto só para fazermos o deploy
da infraestrutura, já que ela não deve mudar com frequência. O código em 
python descreverá a Infra e o GitHub Actions (GA)automatizará o deploy. O
GA possui a feature Environments, que permite gerenciar para cada ambiente
variáveis de ambiente com valores diferentes. Isso nos permite usar uma conta 
diferente para deploy em dev, staging, e prod.

*Requisitos importantes para um DL:*

1. BlockPublicAccess
2. AllowVersioning

---

## Resumo:

- *RAW (DEs)*: bucket_name/fonte/extracted_at_date/files*
		  PARTIÇÃO

- *PROCESSED (DEs + DSs)*: bucket_name/fonte/data=yyyy-mm-dd/*.parquet

- CURATED (semelhante ao que seriam as nossas views) (DEs + DSs + DAs)

	1. Dados seguem regras de negócio para facilitar visualização
	2. Quem aplica regras de negócios nessa camada são os analytic engineers
	3. Dados estão modelados (Data Marts) para servir ferramentas de BI
	4. Ferramentas de BI e DW usam essa camada; Amazon EMR, Redshift, Presto, Athena, etc
	

- Separar em buckets raw e processed é uma boa prática. Ajuda a isolar os ambientes e facilita usar o IAM. 

- bronze/silver/gold data: Convenção de nomes do databricks

- Os arquivos no banco processed ficam sempre salvos como parquet.

### Vantagens do parquet:
	
- Compressão
- Metadados
- Colunar

Delta: Formato open source da Databricks construído sobre o parquet. Adiciona-se maneira de versionar esses arquivos. 

### Particionamento em Data Lake:

O particionamento de dados ajuda a reduzir custos de processamento e a limitar a quantidade de dados escaneados pelas queries. 
150 a 200 Mb é o tamanho ideal para arquivos parquet (rule of thumbs)

			AWS GLUE - Catálogo de dados
			
Armazenamento persistente de metadados. 


CDK serve para definir IaC via código. Boto é mais baixo nível.

			Delta Lake
			
Transactional Storage Layer to some Cloud Storage Solution. 
Adds ACID property to distributed files, data versioning and roolback. 
- ACID on Spark
- Scalable to any scale
- Streaming and Batch unification: Easy to put on lambda architecture
- Delta 10 to 100 times faster than parquet on Spark


			Big Query
			
- Armazenamento no S3, compactação em parquet por conta do Google.
- SQL as a Service
- Suporte para batch ou stream
- Após 90 dias sem atualização, deixa em camada mais fria

OBS: Deploy dessa aula estará no projeto: DataPlatformIaCLearn


