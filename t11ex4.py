def concatena_llistes(llista1, llista2, connector):
    return [f"{a}{connector}{b}" for a, b in zip(llista1, llista2)]

llista1 = ['sub', 'supra']
llista2 = ['campió', 'campiona']
connector = '-'

resultat = concatena_llistes(llista1, llista2, connector)
print(resultat)
