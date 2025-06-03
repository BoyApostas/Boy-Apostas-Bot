# Analisa estatísticas de jogos anteriores
import requests
from config.config import API_FOOTBALL_KEY

API_URL = "https://v3.football.api-sports.io"

headers = {
    "x-apisports-key": API_FOOTBALL_KEY
}

def buscar_estatisticas_time(team_id, last=5):
    url = f"{API_URL}/teams/statistics?team={team_id}&season=2024&league=39"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    dados = response.json()
    return dados

def analisar_jogos_recentes(team_id):
    stats = buscar_estatisticas_time(team_id)
    if not stats:
        return "Erro ao buscar estatísticas."
    
    gols_marcados = stats["response"]["goals"]["for"]["total"]["total"]
    media_gols = gols_marcados / stats["response"]["fixtures"]["played"]["total"]
    
    if media_gols >= 1.5:
        return "Time tem média alta de gols. Boa opção para 'marca 1 gol' ou 'ambos marcam'."
    else:
        return "Time com média baixa. Evitar mercado de gols diretos."

