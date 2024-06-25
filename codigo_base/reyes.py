def plot_pie(fr_relativa, marcas_texto, titulo):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 8))
    plt.pie(fr_relativa,
            autopct="%0.1f%%",
            colors=["#14BF48", "#33FFBE", "#333CFF", "#FF3349", "#F6FF33", "#33FFBE"],
            labels=marcas_texto)
    plt.title(titulo, fontsize=20)
    plt.show()

    return fr_relativa 
