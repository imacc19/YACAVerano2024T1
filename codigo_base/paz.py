import matplotlib.pyplot as plt
def plot_barras(clases, fa_sorted,marcas_texto, labelx, labely, titulo):

        plt.figure(figsize=(20, 12))  # Ancho, Alto del gráfico

        # marcas_clase = [0.165, 0.495, 0.825, 1.155, 1.485]  # Datos del eje x
        # frecuencias = [6, 4, 3, 3, 4]  # Datos del eje y
        # marcas_texto = ["0.165", "0.495", "0.825", "1.155", "1.485"]

        plt.barh(clases, fa_sorted,
                height=0.5, edgecolor="k",
                color=["#33FFBE", "#333CFF", "#FF3349", "#F6FF33", "#333CFF", "#33FFBE"])

        plt.yticks(clases, marcas_texto, fontsize=12, rotation=45)
        plt.xlabel(labelx, fontsize=15)  # Etiqueta del eje x
        plt.ylabel(labely, fontsize=15)  # Etiqueta del eje y
        plt.title(titulo, fontsize=20)  # Etiqueta del título
        plt.grid()  # Activar cuadrícula
        plt.show()  # Mostrar gráfico

        return clases, fa_sorted, marcas_texto