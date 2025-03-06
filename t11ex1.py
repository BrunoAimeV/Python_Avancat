def lenp(frase):
    return list(map(len, frase.split()))
frase = "N'Alejandro té la tita petita"
print(lenp(frase))