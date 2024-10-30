# Verificação de Cache-Control para URLs

Este script em Python verifica o cabeçalho `Cache-Control` de uma lista de URLs fornecidas em um arquivo de texto. Utilizando a biblioteca `requests` para fazer requisições HTTP e `colorama` para destacar visualmente os resultados no terminal, o script exibe as informações sobre `Cache-Control`, `CF-Cache-Status`, `CF-Ray` e tempo de resposta de cada URL.

## Funcionalidades

- **Leitura de URLs:** Lê URLs a partir de um arquivo `.txt`, ignorando linhas que começam com `#` (comentários) e linhas em branco.
- **Requisições HTTP:** Realiza uma requisição GET para cada URL, obtendo os cabeçalhos da resposta.
- **Verificação do Cache-Control:** Analisa o cabeçalho `Cache-Control` para verificar a presença e o valor do parâmetro `max-age`.
- **Exibição de Resultados com Cores:**
  - **Amarelo:** Para `max-age` superior a 100 segundos.
  - **Verde:** Para `max-age` de exatamente 60 segundos.
  - **Sem cor:** Para outros valores de `max-age` ou quando `Cache-Control` está ausente.

## Pré-requisitos

O script requer Python 3.x e as seguintes bibliotecas:

- `requests`
- `colorama`

### Instalação das Dependências

Você pode instalar as dependências usando o `pip`:

```bash
pip install requests colorama
```

## Uso

1. **Configurar o arquivo de URLs:** Crie um arquivo `urls.txt` contendo uma lista de URLs, uma por linha. As linhas que começam com `#` serão ignoradas, sendo tratadas como comentários.

2. **Executar o Script:**

   Salve o script em um arquivo Python, por exemplo `verifica_cache.py`, e execute-o com o seguinte comando:

   ```bash
   python verifica_cache.py
   ```

   O script exibirá o `Cache-Control`, `CF-Cache-Status`, `CF-Ray` (três últimos caracteres) e tempo de resposta de cada URL.

## Exemplo de Arquivo `urls.txt`

```plaintext
# Lista de URLs para verificação
https://exemplo.com
https://outro-exemplo.com
```

## Observações

- O valor de `max-age` em `Cache-Control` é usado para determinar a cor do texto exibido.
- O cabeçalho `CF-Cache-Status` indica o status de cache Cloudflare, e `CF-Ray` representa o identificador de requisição.

## Tratamento de Erros

Em caso de erro ao acessar uma URL, o script exibirá uma mensagem com detalhes sobre o erro.