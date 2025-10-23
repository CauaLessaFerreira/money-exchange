import requests
import json

class color:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    END = '\033[0m'
    ORANGE = ' \033[38;2;255;165;0m'

def fetch_data(endpoint, filters={}):
    url = f"https://economia.awesomeapi.com.br/{endpoint}"
    response = requests.get(url , params=filters)

    return response.json() if response.status_code == 200 else None

dinheiro = float(input(color.ORANGE + "Digite o valor que deseja converter: " + color.END))
escolha = int(input(color.ORANGE + "Digite 1 para USD-BRL, 2 para EUR-BRL ou 3 para CNY-BRL: " + color.END))

if escolha == 1:
    moeda = "USD-BRL"
    simbolo = "US$"
elif escolha == 2:
    moeda = "EUR-BRL"
    simbolo = "€"
elif escolha == 3:
    moeda = "CNY-BRL"
    simbolo = "¥"

cambio = fetch_data(f"{moeda}")

if cambio:
    valor = cambio[0]['ask']
    vfloat = float(valor)
    print(f"{color.YELLOW}O valor do {moeda} é:{color.END} {color.GREEN}{simbolo}{valor[:4]}{color.END}")
    print(f"{color.YELLOW}Convertendo daria:{color.END} {color.GREEN}R${dinheiro * vfloat:.2f}{color.END}")
else:
    print('Failed to fetch data')