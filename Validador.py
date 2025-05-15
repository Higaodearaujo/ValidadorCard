def validar_bandeira_cartao(numero_cartao):
    """
    Valida a bandeira de um cartão de crédito com base no número inicial.
    
    Args:
        numero_cartao (str): Número do cartão de crédito como string.
    
    Returns:
        str: Nome da bandeira do cartão ou "Bandeira desconhecida" se não for identificado.
    """
    if numero_cartao.startswith("4"):
        return "Visa"
    elif numero_cartao[:2] in [str(i) for i in range(51, 56)] or 2221 <= int(numero_cartao[:4]) <= 2720:
        return "MasterCard"
    elif numero_cartao[:4] in ["4011", "4312", "4389"]:  # Adicione outros intervalos Elo conforme necessário
        return "Elo"
    elif numero_cartao[:2] in ["34", "37"]:
        return "American Express"
    elif numero_cartao.startswith("6011") or numero_cartao.startswith("65") or 644 <= int(numero_cartao[:3]) <= 649:
        return "Discover"
    elif numero_cartao.startswith("6062"):
        return "Hipercard"
    else:
        return "Bandeira desconhecida"

# Exemplo de uso
numero = input("Digite o número do cartão de crédito: ")
bandeira = validar_bandeira_cartao(numero)
print(f"A bandeira do cartão é: {bandeira}")