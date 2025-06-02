def contar_dig(n):
    if n < 10:
        return 1
    return 1 + contar_dig(n // 10)