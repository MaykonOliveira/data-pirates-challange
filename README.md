# Informações do Projeto

# Ambiente de Desenvolvimento

## Requisitos
- Python 3.6
- Python 3.6-dev
- setuptools
- VirtualEnv
- Make

## Ambiente Linux
Criar virtualenv dentro do projeto:
```
virtualenv -p /usr/bin/python3.6 .venv
```

Ativar virtualenv:
```
source .venv/bin/activate
```

## Ambiente Windows
Criar diretório da virtualenv dentro do projeto:
```
mkdir .venv
```

Criar virtualenv:
```
virtualenv.exe .venv
```

Ativar virtualenv:
```
.venv\Scripts\activate
```

# Testes
Efetuar o download do projeto:
```
git clone https://github.com/MaykonOliveira/data-pirates-challange.git
```

Instalar as dependências:
```
make init
```

### Fluxo de Execução da Aplicação para saída JSON
```
cd imdb/imdb/spiders
scrapy runspider top500.py -o saida.json
```

### Fluxo de Execução da Aplicação para saída JSONL
```
cd imdb/imdb/spiders
scrapy runspider top500.py -o saida.jsonl -t jsonlines
```

