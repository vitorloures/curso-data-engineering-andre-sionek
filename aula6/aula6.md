# Aula 6: Modelagem de Dados com DBT 

Tópicos tratados em aula:
- Backoff e Rate Limit
- Poetry
- Black e flake8
- Pre-commit
- DBT Redshift Spectrum

---

### Backoff / Rate Limit

1) Backoff - Técnica para retentar a execução de funções quando ela falha.
Útil para consumo de APIs e acesso a redes.

2) Rate Limit - Técnica de APIs para limitar o número de requests por segundo

Existem decorators em Python, para gerenciar o limite de requests por segundo, 
com as respectivas instruções de espera, e para fazer retentativas de acessos a API. 

### Poetry

Excelente gestor de dependências para projetos de Python. Faz gestão de versão de 
bibliotecas, separação de bibliotecas de dev, e prod, facilitar empacotar projeto 
python, etc. 

### Black / Flake8

Reformata automaticamento arquivos de acordo com os padrões de formatação PEP8, 
ou especificados pelo usuário. Útil para padronizar no time o padrão de formatação.

O black apenas verifica se o código está no padrão de formatação especificado e corrige. 
Já o flake8 faz validações estáticas, verifica há import inútil, variáveis não utilizada, etc. 
Ele apenas indica os erros, e é responsabilidade do dev corrigí-los.

### Pre commit 

Cria Git Hooks, ou seja, executa comandos automaticamente antes de commitar 
determinado código.


### DBT no Redshidt Spectrum

O Redshift é o serviço correspondente apenas ao Datawarehouse. Já o Redshift
Spectrum é o DW conectado ao Data Lake. 

Data build tool (DBT) é uma ferramenta que permite o uso de práticas de engenharia
de software, como testes, controle de versão, etc, no SQL. 