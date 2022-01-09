# Aula 5: Orquestrando tarefas com Airflow 

Tópicos tratados em aula:
- Finalização de processamento com Spark e Databricks
- Airflow: Operator, DAG, Containers, Deploy.

---
## Bizu de conexão com RDS Amazon

RDS -> Databases -> db_name:

### NAT Gateway

NAT Gateway é o recurso que permite a conexão de uma SubNet privada com uma Subnet pública.

Comentários bizu do André:

Uso de notebook do Databricks para prototipar, e pycharm para realizar o projeto com controle de versão e testes unitários
Projeto é exportado como package, e executado com um job no cluster. 

### Airflow

O Airflow é uma ferramenta de criação, agendamento e monitoramento de workflows. 

Workflows são criados como Directed Acyclic Graphs (DAGs) de tarefas, o que significa 
que a tarefa possui começo, meio e fim. Não pode haver depedência circular
entre suas etapas. 

A definição da DAG é capaz de evitar que, durante a paralelização da execução, 
não ocorra de começar a se executar uma etapa sem que suas dependências estejam
devidamente concluídas. 

Conceitos:

- Task: Nó no grafo do DAG. Cada task é implementação de um operator.
- Operator: De que forma a tarega a ser executada está escrita (e.g. 
  PythonOperator, BashOperator). Podemos também definir operadores. Isso é útil
  especialmente quando temos uma parte de código que deve ser repetida várias vezes,
  ao longo de diversas tasks.
  
### Containers

Usamos containers contendo:

- Postgres
- Redis (Messaging Queue)
- Airflow (server / scheduler)
- Airflow (workers)


### Deploy 

O deploy do Airflow é uma tarefa com várias etapas, as quais possuem setup complicado.
Para agilizar esse processo, existem soluções de Airflow-as-a-Service fornecidas
tanto pelos provedores de nuvem (e.g. MWAA-AWS, Cloud Compose-GCP) ou de 
fornecedores independentes (e.g. Astronomer). O Astronomer é mais barato, mais 
simples de usar e mais eficiente que os serviços das nuvems.



