def coincideix_valor_i_index(llista):
    return sum(1 for index, valor in enumerate(llista) if index == valor)

llista = [0, 2, 3, 3, 4]
resultat = coincideix_valor_i_index(llista)
print(resultat)
