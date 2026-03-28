# pucpr-DevOps-ATV

# API de Monitoramento de Rede 1.0

##  Descrição
Este projeto foi desenvolvido como parte da disciplina de DevOps, com o objetivo de construir uma API simples para simular monitoramento de rede, utilizando FastAPI.

## Tecnologias utilizadas
- Python
- FastAPI
- Uvicorn

## ▶Como executar

```bash
pip install -r requirements.txt
uvicorn main:app --reload

⚙️ CI/CD

Nesta etapa, implementei o fluxo de CI/CD utilizando o GitHub Actions.

Inicialmente, criei uma branch específica para configuração da integração contínua (CI), onde configurei um workflow responsável por instalar dependências, executar testes automatizados e realizar análise de qualidade de código com Pylint.

Em seguida, criei uma segunda branch para configuração da entrega contínua (CD), implementando um workflow para simular o processo de deploy da aplicação.

Após a configuração de cada etapa, foram realizadas pull requests para integração com a branch principal, garantindo que todos os workflows fossem executados com sucesso antes do merge.



Próximos passos

Pretendo evoluir o projeto adicionando funcionalidades mais próximas de um cenário real de monitoramento de rede. Como próximos passos, planejo implementar rotas que simulem verificações de conectividade, como testes de ping, além de retornar informações mais detalhadas sobre o estado de serviços.