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

    # Buscar jogos do dia
    url = f"{API_BASE_URL}/fixtures?date={today}&timezone=America/Sao_Paulo"
    resp = requests.get(url, headers=HEADERS)
    data = resp.json()

    jogos_formatados = []

    if "response" in data:
        for jogo in data["response"]:
            fixture_id = jogo['fixture']['id']
            home = jogo['teams']['home']['name']
            away = jogo['teams']['away']['name']

            # Buscar odds para este jogo
            odds_url = f"{API_BASE_URL}/odds?fixture={fixture_id}&bookmaker=6"  # Bet365 é 6 na API-Football
            odds_resp = requests.get(odds_url, headers=HEADERS)
            odds_data = odds_resp.json()
            odd_home_win = None

            # Decodificando odds (simples: mercado 'Match Winner')
            try:
                # A API pode retornar odds de vários mercados e casas
                # Procurar pelo mercado "Match Winner"
                for result in odds_data['response']:
                    for bookmaker in result.get('bookmakers', []):
                        for bet in bookmaker.get('bets', []):
                            if bet['name'] in ["Match Winner", "1x2"]:
                                for odd in bet['values']:
                                    if odd['value'] == 'Home':
                                        odd_home_win = float(odd['odd'])
                # Se não achou, deixa None
            except Exception as e:
                odd_home_win = None

            jogos_formatados.append({
                'homeTeam': {'name': home},
                'awayTeam': {'name': away},
                'odds': {
                    'homeWin': odd_home_win
                }
            })

    return jogos_formatados

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
