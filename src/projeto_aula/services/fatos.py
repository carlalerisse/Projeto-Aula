import requests

def buscar_fato_aleatorio() -> str:
    resposta = requests.get(
        "https://uselessfacts.jsph.pl/api/v2/facts/random?language=pt-br"
    )
    return resposta.json()["text"]