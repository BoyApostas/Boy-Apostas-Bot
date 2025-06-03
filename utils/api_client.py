# Conecta e consulta a API-Football
import requests
from config.config import API_FOOTBALL_KEY

API_BASE_URL = "https://v3.football.api-sports.io"
HEADERS = {
    "x-apisports-key": API_FOOTBALL_KEY
}
def get_today_matches():
    from datetime import datetime
    today = datetime.now().strftime('%Y-%m-%d')

    url = f"https://v3.football.api-sports.io/fixtures?date={today}&timezone=America/Sao_Paulo"

    headers = {
        'x-apisports-key': API_FOOTBALL_KEY
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if "response" in data:
        return data["response"]
    return []

def get_fixture_statistics(fixture_id):
    url = f"{API_BASE_URL}/fixtures/statistics?fixture={fixture_id}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar estatísticas: {response.status_code}")
        return None

def get_live_fixtures():
    url = f"{API_BASE_URL}/fixtures?live=all"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar jogos ao vivo: {response.status_code}")
        return None
