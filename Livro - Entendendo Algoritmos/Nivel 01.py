def contar (n):
    if n == 0: # CASO BASE
        print("FIM")
    else:
        print(n)
        contar(n-1) # CHAMADA RECURSIVA