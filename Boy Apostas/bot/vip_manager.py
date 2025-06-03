# Gerencia usuários VIP e pagamentos
from datetime import datetime, timedelta

# Simula um banco de dados simples na memória (você pode trocar por um real depois)
usuarios_vip = {}

def ativar_vip(user_id: int):
    hoje = datetime.today().date()
    vencimento = hoje + timedelta(days=30)
    usuarios_vip[user_id] = vencimento
    return vencimento

def check_vip_status(user_id: int) -> bool:
    hoje = datetime.today().date()
    vencimento = usuarios_vip.get(user_id)
    if vencimento and vencimento >= hoje:
        return True
    return False

def verificar_vencimentos():
    hoje = datetime.today().date()
    avisos = []
    for user_id, vencimento in usuarios_vip.items():
        dias_restantes = (vencimento - hoje).days
        if dias_restantes in [2, 1, 0]:
            avisos.append((user_id, dias_restantes))
    return avisos
