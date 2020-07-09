

def determinaraproado(promedio):
    if promedio>=11:
        resultado="aprobado"
    
    else:
        resultado="desaprobado"
        
    return resultado

promedio= int(input("promedio: "))
print (determinaraproado(promedio))