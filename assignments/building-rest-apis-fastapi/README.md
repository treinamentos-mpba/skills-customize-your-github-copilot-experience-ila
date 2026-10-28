# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando FastAPI, praticando rotas HTTP, operações CRUD, validação de dados e códigos de status.

## 📝 Tarefas

### 🛠️ Criar a primeira rota

#### Descrição

Prepare o ambiente, execute o código inicial e crie uma rota de verificação para confirmar que a API está funcionando.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `python -m pip install fastapi uvicorn`.
- Criar uma aplicação FastAPI com o título `Task API`.
- Implementar `GET /health`, retornando o JSON `{"status": "ok"}`.
- Iniciar o servidor com `uvicorn starter-code:app --reload` e permitir testar a API em `/docs`.


### 🛠️ Implementar operações de criação e leitura

#### Descrição

Adicione à API operações para criar tarefas e consultar a lista ou uma tarefa específica. Cada tarefa deve ter um identificador, um título e um estado de conclusão.

#### Requisitos
O programa concluído deve:

- Manter as tarefas em memória durante a execução do servidor.
- Implementar `GET /tasks` para retornar todas as tarefas.
- Implementar `POST /tasks` para criar uma tarefa com título e estado de conclusão.
- Atribuir um identificador único a cada tarefa criada.
- Implementar `GET /tasks/{task_id}` para consultar uma tarefa pelo identificador.

Exemplo de corpo para criar uma tarefa:

```json
{
  "title": "Estudar FastAPI",
  "completed": false
}
```


### 🛠️ Completar o CRUD e tratar erros

#### Descrição

Expanda a API para atualizar e remover tarefas. Use validação do FastAPI e respostas HTTP adequadas para operações concluídas, dados inválidos e identificadores inexistentes.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /tasks/{task_id}` para atualizar o título e o estado de conclusão de uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa existente.
- Retornar o código `201 Created` ao criar uma tarefa.
- Retornar `404 Not Found` quando o identificador solicitado não existir.
- Retornar `204 No Content` ao remover uma tarefa com sucesso.
- Rejeitar corpos inválidos, como uma tarefa sem título, usando a validação do FastAPI.