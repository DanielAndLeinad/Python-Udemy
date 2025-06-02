def fib(n):
    if n == 0 or n == 1: # CASO BASE    
        return n
    return fib(n-1) + fib(n-2) # CHAMADA RECURSIVA

'''
fib(4)
├── fib(3)
│   ├── fib(2)
│   ├── fib(1)
└── fib(2)
    ├── fib(1)
    ├── fib(0)

etc


CASO DE MEMOIZAÇÃO

é uma técnica de otimização que armazena os resultados de chamadas de funções para que possam ser 
reutilizados em chamadas futuras com os mesmos argumentos, evitando cálculos repetidos

 
'''