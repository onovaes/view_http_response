# Verificação de Cache-Control para URLs

Este script em Python verifica o cabeçalho `Cache-Control` de uma lista de URLs fornecidas em um arquivo de texto, ajudando a analisar informações de cache e desempenho de páginas web que usam cloudflare ou outros serviços de cache.

## Funcionalidades

- **Leitura de URLs**: Lê URLs a partir de um arquivo `.txt`, ignorando linhas de comentário (`#`) e linhas em branco.
- **Requisições HTTP**: Realiza uma requisição GET para cada URL e obtém cabeçalhos HTTP.
- **Verificação do Cache-Control**: Analisa o cabeçalho `Cache-Control` para verificar `max-age`.
- **Exibição de Resultados com Cores**: Exibe os resultados com cores para facilitar a visualização.

## Pré-requisitos

Python 3



1. **Clone o repositório**:

    ```bash
    git clone https://github.com/onovaes/view_http_response.git
    cd view_http_response
    ```
## Instalação (opção 1)

    Instale as dependências 

    ```bash
    pip install -r requirements.txt
    ```

## Instalação com virtualenv (opção 2)

    
    Use um ambiente virtual para instalar seus pacotes, assim você evita mexer no sistema e mantém o projeto isolado:

    ```bash
    # Crie o ambiente virtual (uma vez)
    python3 -m venv .venv

    # Ative o ambiente virtual
    source .venv/bin/activate

    # Instale os pacotes a partir do arquivo de requisitos
    pip3 install -r requirements.txt
    ```

## Uso do Script

1. **Configurar o arquivo de URLs**: Crie um arquivo `urls.txt` contendo URLs, uma por linha. Linhas que começam com `#` serão ignoradas, assim como linhas em branco.

2. **Executar o Script**: Salve o código no arquivo `verifica_cache.py` e execute:

    ```bash
    python verifica_cache.py
    ```

## Exemplo de Arquivo `urls.txt`

```plaintext
# Lista de URLs para verificação
https://exemplo.com
https://outro-exemplo.com
```
