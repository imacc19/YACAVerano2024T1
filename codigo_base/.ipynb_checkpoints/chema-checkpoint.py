def fa_grouped(datos, lim_inf, lim_sup):

    fa = [0] * len(lim_inf)
    clases = [0] * len(lim_inf)
    
    for i in range(len(lim_inf)):
        clases[i] = i + 1 
    
    for elemento in datos:
        for j in range(0, len(lim_inf)):
            if j == 0:
            # if j == len(lim_inf)-1:
                if lim_inf[j] <= elemento <= lim_sup[j]:
                    fa[j] += 1
                    break
            else:
                if lim_inf[j] < elemento <= lim_sup[j]:
                #if lim_inf[j] <= elemento < lim_sup[j]:
                    fa[j] += 1
                    break
    return fa, clases