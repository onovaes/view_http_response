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

                if cf_cache_status == 'HIT':
                    cf_cache_status = f"{Fore.GREEN}{cf_cache_status} {Style.RESET_ALL}"
                elif cf_cache_status == 'EXPIRED':
                    cf_cache_status = f"{Fore.BLUE}{cf_cache_status} {Style.RESET_ALL}"
                elif cf_cache_status == 'DYNAMIC':
                    cf_cache_status = f"{Fore.YELLOW}{cf_cache_status} {Style.RESET_ALL}"
                else:
                    cf_cache_status = f"{Fore.BLUE}{cf_cache_status} {Style.RESET_ALL}"

                bests_cf_ray_datacenter = ['GIG', 'GRU']
                if not cf_ray in bests_cf_ray_datacenter:
                    cf_ray = f"{Fore.YELLOW}{cf_ray} {Style.RESET_ALL}"

                if max_age > 200:
                    max_age = f"{Fore.RED}Max-age: {max_age} {Style.RESET_ALL}"
                elif max_age > 100:
                    max_age = f"{Fore.YELLOW}Max-age: {max_age} {Style.RESET_ALL}"
                else:
                    max_age = "Max-age: " + str(max_age)
                
                
                print(f"{url} | Cache-Control: {cache_control} | {max_age} | CF-Cache-Status: {cf_cache_status} | CF-Ray: {cf_ray} | Tempo de Resposta: {response_time:.2f}s")
            
        except Exception as e:
            print(f"Erro ao acessar {url}: {e}")

# Caminho do arquivo de URLs
file_path = 'urls.txt'
verifica_cache_control(file_path)