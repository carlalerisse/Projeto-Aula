# Projeto Aula - Trilha Python

Projeto realizado na aula de **Trilha Python**. Uma aplicação de linha de comando que busca fatos aleatórios de uma API externa e exube junto com informações do sistema.

## Funcionalidades

- Busca fatos aleatórios da API [Useless Facts](https://uselessfacts.jsph.pl/)
- Exibe informações do sistema (plataforma, diretório atual, data/hora)
- Interface via linha de comando

## Instalação

### Pré-requisitos

- Python >= 3.12
- [Poetry](https://python-poetry.org/)

### Passos

```bash
# Instale as dependências
poetry install
```

## Uso

```bash
poetry run projeto_aula
```

A saída será um dicionário com as seguintes informações:

| Campo         | Descrição                          |
|----------------------------------------------------|
| `fato`        | Um fato aletatório obtido da API   |
| `sistema`     | Plataforma do sistema operacional  |
| `diretório`   | Diretório de trabalho atual        |
| `data`        | Data e hora da execução (ISO 8601) |

## Desenvolvimento

### Ferramentas

O projeto utiliza as seguintes ferramentas de desenvolvimento:

- **Ruff** - Linter e formatador
- **Pytest** - Testes unitários com cobertura
- **Taskipy** - Atalhos de tarefas

### Comandos úteis

```bash
# Formatar código
poetry run task format

# Verificar linting
poetry run task lint

# Executar testes
poetry run task tests
```

## Estrutura do Projeto

```
projeto_aula/
|-- docs/
|   |__ index.md
|-- src/
|   |__ projeto_aula/
|       |-- __init__.py
|       |__ main.py
|-- tests/
|   |__ unit/
|       |__ test_E2E.py
|-- mkdocs.yml
|__ pyproject.toml
```
