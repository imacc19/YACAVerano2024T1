def plot_poligono(clases, fa_sorted,marcas_texto, labelx, labely, titulo):
    import matplotlib.pyplot as plt

# Datos
    plt.figure(figsize=(12, 6))  # Ancho, Alto del gráfico


    # Ajustes para el graficado del polígono
    datos_x = [0] + clases + [len(clases) + 1]
    datos_y = [0] + fa_sorted + [0]

    plt.plot(datos_x, datos_y, 
        linewidth=5, color="g", linestyle="--", 
        marker="v", markersize=10, markerfacecolor="y", markeredgecolor="r")

    plt.xticks(clases, marcas_texto, fontsize=12, rotation=45)
    plt.xlabel(labelx, fontsize=15)  # Etiqueta del eje x
    plt.ylabel(labely, fontsize=15)  # Etiqueta del eje y
    plt.title(titulo, fontsize=20)  # Etiqueta del título
    plt.grid()  # Activar cuadrícula
    plt.show()  # Mostrar gráfico
    return clases, fa_sorted, marcas_texto