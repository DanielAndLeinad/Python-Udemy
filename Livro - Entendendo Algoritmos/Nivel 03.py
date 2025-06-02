def soma (n):
    if n == 1: # CASO BASE
        return 1
    return n + soma(n-1) # CHAMADA RECURSIVA


'''
soma(5) = 5 + soma(4)
soma(4) = 4 + soma(3)
...
soma(1) = 1


'''