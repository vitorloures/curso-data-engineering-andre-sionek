# Aula 2: Integração Contínua e Testes

Tópicos tratados em aula:   
- Conceitos: Role, Group e Policy (revisão aula 1)
    IAM deve usar princípio de acesso mínimo para cada grupo / usuário.
    Uma boa política de IAM é essencial para proteger a empresa de erros
    do "estagiário" que podem levar a custos desnecessários, perdas ou vazamentos de dados
- Controle de versão com Git
- Conceitos de Integração e Deploy Contínuo - CI/CD
- Templating com Jinja
- CI/CD com Github Actions
- Automação de deploy com AWS CDK (CDK vai substituir o CloudFormation) 
- Testes para a Infra
    1. Teste unitário: testa função ou módulo pequeno; deve explicar comportamento esperado do código. Não captam fluxo de dados na aplicação. Partes devem ser isoladas uma das outras via Mockes e Patches.
    2. Testes de integração: testam fluxo de dados, acesso a rede, banco de dados (ou estrutura similar). Simula situação real de uso da aplicação. Sujeito a falsos negativos por falha de aplicação na rede, na comunicação, etc. 

--- 
## Aprendizados úteis de Git obtidos nessa aula

1) `git rebase -i HEAD~2 é mais simples que git rebase -i $commit_id`
2) Para fundir 2 commits sem mudar mensagem de um deles, fixup é mais fácil que squash

---
## Exemplos de CI/CD

- CI Pipeline (first stage): Automated Compilation, Validation, Code Review, Unit Testing, and Integration Testing. Continuos Build
- CD Pipeline (second stage): Automated Deploy on staging, or production environment

---

## Github Actions

- Organização privada possui 2000 min/mês incluso de deploy
- Ferramenta do Github para fazer testes automatizados, rodar scripts, fazer deploy, e gerenciamento de senhas.

--
## Jinja

- Jinja é uma ferramenta para template web em python
- Casos de uso: (inserção de variáveis)
    1. Setup de diferentes ambientes
    2. Substituição de credenciais durante a execução ou deploy

Nosso CI deve rodar o código em dev num servidor para isso e avaliar segundo um resultado esperado

--
## AWS CDK

- O AWS CDK é um framework, com suporte para várias linguagens, para definição de IaC e provisionamento com AWS Cloud Formation
- Embora CloudFormation seja muito útil, ele não oferece suporte para operações lógicas, por exemplo. Além de ser mais simples inserir variável que template Jinja. 
- Para usar o CDK precisamos:
    1. Instalar Node.JS: `npm install -g aws-cdk`
    2. Instalar AWS CLI: `cdk init --language python`
- CDK criar pacote python para instalar a Infra