# api-credit-card-fraud
#### Api adminstrativa e pré-processamento do dataset Credit Card Fraud.

## Recriando o banco
Para reacriar o banco é necessario o postgres de forma local ou em nuvem. Criar tabela com nome padrão `api_credit_card_fraud`.

Após rodar os seguintes comandos dentro da pasta do projeto:

```
pip install
```
```
alembic init alembic
```

Vá no arquivo `alembic.ini` na raiz do projeto e adicione:
```python
sqlalchemy.url = postgresql://postgres:{senha}@{host}:{porta}/{nomedobanco}
```

Entre no arquivo `alembic/env.py`, e cole o trecho:
```python
from api.models.users_model import Users

from api.models.database import Base
target_metadata = Base.metadata
```

Feito isso rode o comando para a `migration`:
```
alembic revision --autogenerate -m 'create tables'
```
```
alembic upgrade head
```

## Start
Criar na raiz um arquivo `.env`

```
Executar pelo depurador do VsCode
```

### Variáveis de ambiente

Descrição das variáveis de ambiente a serem configuradas no projeto.

|Env name         |Tipo    |Valor Padrão |Descricao                          |
|-----------------|--------|-------------|-----------------------------------|
|DATABASE_UPGRADE |`string`|False        |Controla a atualização do banco    |
|URL_BASE         |`string`|             |Url base do projeto local          |
|DATABASE_HOST    |`string`|             |Host do banco local ou em nuvem    |
|DATABASE_NAME    |`string`|postgres     |Username do banco                  |
|DATABASE_PASSWORD|`string`|             |Password do banco                  |
|DATABASE_DB_NAME |`string`|             |Nome do banco                      |
|DATABASE_PORT    |`string`|5432         |Porta a ser usada pelo postgres    |
|DATABASE_UPGRADE |`string`|False        |Atualiza o banco ao reiniciar      |
|SECRET_KEY       |`string`|             |String aleatória para criar o token|
|ALGORITHM        |`string`|             |Algoritmo usado na criptografia    |

## Apêndice
Para informações de rotas segui a documentação da API no swagger ``--->``

*url padrão*
```
http://127.0.0.1:8000/docs
```

## Licença

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)