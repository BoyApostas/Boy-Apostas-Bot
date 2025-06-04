# Gera sugestões de apostas com base nas análises
import random
from utils.api_client import get_today_matches

def gerar_aposta_segura():
    partidas = get_today_matches()
    if not partidas:
        return "⚠️ Nenhuma partida relevante encontrada hoje para análise segura. Aguarde novas oportunidades!"

    favoritas = []
    for jogo in partidas:
        home = jogo.get('homeTeam', {}).get('name', 'Time A')
        away = jogo.get('awayTeam', {}).get('name', 'Time B')
        odds = jogo.get('odds', {})
        home_win = odds.get('homeWin')

        # Critérios: odds seguras e presença de times favoritos
        if home_win and home_win <= 1.35:
            favoritas.append({
                'time': home,
                'contra': away,
                'odd': home_win
            })

    favoritas = sorted(favoritas, key=lambda x: x['odd'] or 99)

    combinadas = []
    total_odd = 1.0
    for f in favoritas:
        combinadas.append(f)
        total_odd *= f['odd']
        if total_odd >= 2.3:
            break

    if not combinadas or total_odd < 2.0:
        return (
            "❌ Hoje não encontramos uma aposta *realmente segura* (odd baixa e múltiplos confiáveis).\n\n"
            "Aguarde amanhã para uma nova análise automática!\n"
            "Seu saldo e banca agradecem 😉"
        )

    mensagem = (
        "🔥 *Aposta Segura do Dia* 🔥\n"
        "Acompanhe nossa múltipla de favoritos selecionada por estatísticas avançadas:\n\n"
    )
    for c in combinadas:
        mensagem += f"✅ *{c['time']}* vence o *{c['contra']}* _(odd: {c['odd']})_\n"
    mensagem += f"\n*Odd Total:* `{round(total_odd, 2)}`\n"
    mensagem += (
        "\n⏳ Aposta enviada automaticamente pelo Boy Apostas, baseada em dados reais e análise estatística. "
        "Aposte com responsabilidade!\n"
    )

    return mensagem
