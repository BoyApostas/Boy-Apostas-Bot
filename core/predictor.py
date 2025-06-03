# Gera sugestões de apostas com base nas análises
import requests
from config.config import API_FOOTBALL_KEY
from datetime import datetime

API_BASE_URL = "https://v3.football.api-sports.io"
HEADERS = {"x-apisports-key": API_FOOTBALL_KEY}

def get_fixtures_today():
    today = datetime.now().strftime("%Y-%m-%d")
    url = f"{API_BASE_URL}/fixtures?date={today}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        return data["response"]
    else:
        print(f"Erro ao buscar jogos do dia: {response.status_code}")
        return []

def get_team_statistics(team_id):
    url = f"{API_BASE_URL}/teams/statistics?team={team_id}&season=2024&league=39"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json().get("response", {})
    else:
        print(f"Erro ao buscar estatísticas: {response.status_code}")
        return None

def gerar_aposta_segura():
    return {
        "jogos": ["Time A", "Time B"],
        "odd_total": 2.5,
        "descricao": "Exemplo de aposta segura."
    }
