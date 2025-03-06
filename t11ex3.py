def Paraules_que_comencen(per, lletra):
    return list(filter(lambda paraula: paraula.startswith(lletra), per))
llista = ["maria", "manta", "peu", "mà"]
print(Paraules_que_comencen(llista, 'p'))