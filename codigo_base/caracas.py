def plot_hist(clases, freq_absoluta, mrks, labelx, labely, titulo):
    import matplotlib.pyplot as plt

     # Ajustar el ancho de las barras según el tamaño de los datos
    plt.figure(figsize=(30, 21))
    
    if max(mrks) > 500:
        bar_width = 30.0
    else:
        bar_width = 15.0

    plt.bar(mrks, freq_absoluta,
           width=bar_width, edgecolor="k",
           color=["#14BF48", "#33FFBE", "#333CFF", "#FF3349", "#F6FF33", "#33FFBE"])
    
    plt.xticks(mrks,  fontsize=12)
    plt.xlabel(labelx, fontsize=15)  
    plt.ylabel(labely, fontsize=15)  
    plt.title(titulo, fontsize=20)  
    plt.grid()  
    plt.show()      