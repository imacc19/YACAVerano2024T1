def plot_hist(clases, freq_absoluta, mrks, labelx, labely, titulo):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 6))  # Set the figure size

    plt.bar(mrks, freq_absoluta,
           width=0.3, edgecolor="k",
           color=["#14BF48", "#33FFBE", "#333CFF", "#FF3349", "#F6FF33", "#33FFBE"])
    
    plt.xticks(mrks,  fontsize=12)
    plt.xlabel(labelx, fontsize=15)  # X-axis label
    plt.ylabel(labely, fontsize=15)  # Y-axis label
    plt.title(titulo, fontsize=20)  # Title
    plt.grid()  # Enable grid
    plt.show()  # Display the plot
    
    return clases, freq_absoluta, mrks