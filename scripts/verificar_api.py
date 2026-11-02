# verificar_api.py
import requests

URL = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=pt-br"

def verificar_api():
  try:
    resposta = requests.get(URL, timeout=5)
    resposta.raise_for_status()
    print(f"API online - Status: {resposta.status_code}")
  except requests.ConnectionError:
    print("API offline - Falha na conexao")
  except requests.Timeout:
    print("API offline - Timeout (5s)")
  except requests.HTTPError as e:
    print(f"API com erro - Status: {e.response.status_code}")

if __name__ == "__main__":
    verificar_api()
    