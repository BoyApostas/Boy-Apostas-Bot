# Funções auxiliares como cálculo de odds
def calcular_odd_combinada(odds):
    resultado = 1.0
    for odd in odds:
        resultado *= odd
    return round(resultado, 2)

def formatar_mensagem_aposta(times, odds):
    partes = []
    for time, odd in zip(times, odds):
        partes.append(f"{time} (odd {odd})")
    combinada = " + ".join(partes)
    total = calcular_odd_combinada(odds)
    return f"Aposta combinada sugerida:\n\n{combinada}\n\nOdd total: {total}"
