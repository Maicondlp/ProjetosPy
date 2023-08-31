#!/usr/bin/python3
import requests, sys, urllib3, socket,re,pyfiglet

texto = "GENGAR"
fonte = pyfiglet.Figlet()
banner = fonte.renderText(texto)
print(f'\033[94m{banner}\033[0m')

parametro_1 = sys.argv[1]

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
r = requests.get(parametro_1,verify=False)
print("\033[94m--------------------------------------------------------------------\033[0m")
print("\033[92mSite/Aplicação: \033[0m" + parametro_1)
print("\033[92mStatus code: \033[0m" + str(r.status_code))
############################ VERIFICAR MÉTODOS HTTP PERMITIDOS ############################
r = requests.options(parametro_1,verify=False)
if r.status_code == 200:
    allowed_methods = r.headers.get("allow")
    if allowed_methods:
        methods_list = allowed_methods.split(", ")
        print("\033[92mMétodos HTTP permitidos: \033[0m", methods_list)
    else:
        print("\033[92mMétodo Options desabilitado.\033[0m")
else:
    print("\033[91mNão foi possível obter a lista de métodos permitidos.\033[0m")
print("-----------------------------------------------------------")
############################ VERIFICAÇÃO DO SERVIDOR WEB ############################
servidor = r.headers["Server"]
print("\033[92mServidor Web: \033[0m" + str(servidor))
if servidor[:8] == "Apache/2":
    if servidor[:12] != "Apache/2.4.6":
        print("\033[91mVersão desatualizada do servidor Apache - Atualize-o para a última versão disponível no repositório do CTIM\033[0m")
print("-----------------------------------------------------------")

############################ VERIFICAÇÃO DOS CABEÇALHOS HTTP ############################
cabecalhos = r.headers.items()

cabecalho_XCTO,cabecalho_XFO,cabecalho_XSS = False,False,False

for key,value in cabecalhos:
    print(f"\033[92m{key}\033[0m: {value}")
    if (key == "X-Content-Type-Options"):
        cabecalho_XCTO = True
    if (key == "X-Frame-Options"):
        cabecalho_XFO = True
    if (key == "X-XSS-Protection"):
        cabecalho_XSS = True

if (cabecalho_XCTO == False):
    print("\033[91m***** Ausência de cabecalho_XCTO\033[0m")
if (cabecalho_XFO == False):
    print("\033[91m***** Ausência de cabecalho_XFO\033[0m")
if (cabecalho_XSS == False):
    print("\033[91m***** Ausência de cabecalho_XSS\033[0m")

print("-----------------------------------------------------------")

############################ VERIFICAÇÃO DE ARQUIVO ROBOTS.TXT ############################
robots = parametro_1 + "/robots.txt"
r = requests.get(robots,verify=False)
if r.status_code == 200:
    diretorios = re.findall(r'Disallow: (.*?)\n', r.text)
    print("\033[92mDiretórios desabilitados no arquivo robots.txt\033[0m")
    for diretorio in diretorios:
        print(f'\033[92m{diretorio}\033[0m')
else:
    print("\033[91mNão foi possível encontrar o arquivo robots.txt\033[0m")