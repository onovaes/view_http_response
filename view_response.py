import requests
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

def verifica_cache_control(file_path):
    # Abrir o arquivo e ler as URLs, exceto as que começam com #
    with open(file_path, 'r') as file:
        urls = [line for line in file if not line.startswith('#') and line.strip() != '']
    
    # Para cada URL, realizar a requisição e verificar o cache-control
    for url in urls:
        url = url.strip()  # Remover espaços em branco e quebras de linha
        try:
            response = requests.get(url, timeout=5)
            # Tempo de resposta em segundos
            response_time = response.elapsed.total_seconds()
            
            # Obter o cabeçalho Cache-Control
            cache_control = response.headers.get('Cache-Control', '')
            cf_cache_status = response.headers.get('cf-cache-status', '')
            cf_ray = response.headers.get('cf-ray', '')
            # Extrair apenas os últimos 3 caracteres do cf-ray
            cf_ray = cf_ray[-3:]
            
            if 'max-age' in cache_control:
                # Extrair o valor de max-age
                max_age = int(cache_control.split('max-age=')[1].split(',')[0])
                
                # Verificar condições de max-age e definir cor
                if max_age > 100:
                    print(f"{Fore.YELLOW}{url} | Cache-Control: {cache_control} | CF-Cache-Status: {cf_cache_status} | CF-Ray: {cf_ray} | Tempo de Resposta: {response_time:.2f}s")
                elif max_age == 60:
                    print(f"{Fore.GREEN}{url} | Cache-Control: {cache_control} | CF-Cache-Status: {cf_cache_status} | CF-Ray: {cf_ray} | Tempo de Resposta: {response_time:.2f}s")
                else:
                    print(f"{url} | Cache-Control: {cache_control} | CF-Cache-Status: {cf_cache_status} | CF-Ray: {cf_ray} | Tempo de Resposta: {response_time:.2f}s")
        except Exception as e:
            print(f"Erro ao acessar {url}: {e}")

# Caminho do arquivo de URLs
file_path = 'urls.txt'
verifica_cache_control(file_path)
