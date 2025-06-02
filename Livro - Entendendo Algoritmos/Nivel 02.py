def fatorial (n):
    if n ==0: #CASO BASE
        return 1
    return n * fatorial(n-1) # CHAMADA RECURSIVA

'''
fatorial de (5)
    n = 5 * fatorial(4)
    n = 4 * fatorial(3)
    n = 3 * fatorial(2)
    n = 2 * fatorial(1)
    n = 1 * fatorial(0)
    n = 1 # CASO BASE
    
    OU // MESMA COISA
    
    5! = 5 x 4 x 3 x 2 x 1
    5! = 20 * 3 x 2 x 1
    5! = 60 * 2 x 1
    5! = 120 * 1
    5! = 120 # CASO BASE


'''