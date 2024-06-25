import math

def clases_grouped(datos):
    amplitud = round(max(datos) - min(datos), 2)
    nclases = 1 + (3.3*math.log10(len(datos)))
    anc_clas = round(amplitud / math.floor(nclases), 2)

    marc_clase = []
    lim_inf = []
    lim_sup = []

    for i in range(int(nclases)):
        marc_clase.append(round(min(datos) + i*anc_clas + anc_clas/2, 3))
        lim_inf.append(round(min(datos) + i*anc_clas, 2))
        lim_sup.append(round(min(datos) + (i+1)*anc_clas, 2))

    return lim_inf, lim_sup, marc_clase
    '''
datos = [0, 0, 0.33, 0.33, 0.33, 0.33, 0.66, 0.66, 0.66, 0.66, 0.99, 0.99, 0.99, 1.32,
         1.32, 1.32, 1.65, 1.65, 1.65, 1.65]

lim_inf, lim_sup, mrks = clases_grouped(datos)
print("Límites Inferiores:", lim_inf)
print("Límites Superiores:", lim_sup)
print("Marcas de Clase:", mrks)
    '''