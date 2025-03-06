from functools import reduce
def Passar_a_Numero(llista):
    return reduce(lambda x, y: x * 10 + y, llista)
llista = [3, 4, 1, 5]
print(Passar_a_Numero(llista))