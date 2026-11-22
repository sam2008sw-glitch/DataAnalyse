
import matplotlib.pyplot as plt

def show_histogram(data):
    plt.hist(data, bins=10)

    plt.title("Värden i min lista")

    plt.xlabel("Värde")

    plt.ylabel("Antal")

    plt.show()
