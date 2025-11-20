def invertir(cadena):
    if len(cadena)<=1:
        return cadena
    return cadena[-1]+invertir(cadena[:-1])
def plm(cadena):
    return cadena==invertir(cadena)
print(plm("radar"))   
print(plm("python")) 
print(plm("Estiven"))
