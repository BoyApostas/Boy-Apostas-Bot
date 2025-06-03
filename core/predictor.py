# Gera sugestões de apostas com base nas análises
import random
from utils.api_client import get_today_matches


def gerar_aposta_segura():
    partidas = get_today_matches()

    favoritas = []
    for jogo in partidas:
        home = jogo['homeTeam']['name']
        away = jogo['awayTeam']['name']
        odds = jogo.get('odds', {})
        home_win = odds.get('homeWin')

        # Critérios para times favoritos com baixa odd
        if home_win and home_win <= 1.35:
            favoritas.append({
                'time': home,
                'contra': away,
                'odd': home_win
            })

    favoritas = sorted(favoritas, key=lambda x: x['odd'])

    combinadas = []
    total_odd = 1.0
    for f in favoritas:
        combinadas.append(f)
        total_odd *= f['odd']
        if total_odd >= 2.3:
            break

    if not combinadas or total_odd < 2.0:
        return None  # Nenhuma combinação segura suficiente

    mensagem = "🔥 *Aposta Segura do Dia* 🔥\n\n"
    for c in combinadas:
        mensagem += f"✅ {c['time']} vence o {c['contra']} (odd: {c['odd']})\n"
    mensagem += f"\n*Odd Total:* `{round(total_odd, 2)}`\n"
    mensagem += "\n⏰ Enviada automaticamente pelo bot com base nas análises estatísticas do dia."

    return mensagem
