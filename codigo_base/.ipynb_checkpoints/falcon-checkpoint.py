def clases_str_sort(datos_formated):
    ordenamiento = 0
    for elemento in range(0,len(datos_formated) - 1):
        for orden in range(0,len(datos_formated) - 1):
            if datos_formated[orden] > datos_formated[orden + 1]:
                ordenamiento = datos_formated[orden]
                datos_formated[orden] = datos_formated[orden + 1]
                datos_formated[orden + 1] = ordenamiento

    return datos_formated

