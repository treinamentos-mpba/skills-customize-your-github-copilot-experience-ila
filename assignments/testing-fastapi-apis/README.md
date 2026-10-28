# 📘 Atividade: Testando APIs com FastAPI

## 🎯 Objetivo

Escreva testes automatizados para uma API FastAPI usando `pytest` e `TestClient`. Pratique verificar códigos de status, dados retornados e respostas para recursos inexistentes.

## 📝 Tarefas

### 🛠️ Preparar o ambiente de testes

#### Descrição

Instale as dependências e prepare o código inicial da API para que possa ser importado pelos testes.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `python -m pip install fastapi pytest httpx`.
- Renomear `starter-code.py` para `app.py`.
- Criar um arquivo `test_api.py` e importar `app` de `app.py`.
- Criar um `TestClient` usando a aplicação importada.
- Executar os testes com `pytest -q`.


### 🛠️ Testar respostas bem-sucedidas

#### Descrição

Escreva testes para verificar as rotas de status e de consulta de tarefas, conferindo tanto o código HTTP quanto o conteúdo JSON.

#### Requisitos
O programa concluído deve:

- Testar `GET /health` e confirmar o código `200` e o JSON `{"status": "ok"}`.
- Testar `GET /tasks` e confirmar que a resposta contém a tarefa de exemplo.
- Testar `GET /tasks/1` e confirmar os campos `id`, `title` e `completed` da tarefa.
- Usar asserções do pytest para verificar cada resultado.


### 🛠️ Testar respostas de erro

#### Descrição

Verifique como a API responde quando o cliente solicita uma tarefa que não existe.

#### Requisitos
O programa concluído deve:

- Testar `GET /tasks/999`.
- Confirmar que a resposta tem o código `404`.
- Confirmar que o JSON de erro contém a mensagem `Task not found`.
- Executar todos os testes com `pytest -q` e confirmar que passam.