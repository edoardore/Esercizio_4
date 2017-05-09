from test import TestA

import pickle, matplotlib.pyplot as plt, matplotlib.patches as mpatches

lista_test = [1000, [10, 20, 30, 40, 50, 60, 70, 75, 85, 87, 89, 90, 91, 92, 93, 94, 95, 97, 98, 99, 100]]
pickle.dump(lista_test, open("list.p", "wb"))


def plot_test_hash_open():
    TestA()
    A = pickle.load(open("medie.p", "rb"))
    B = pickle.load(open("min.p", "rb"))
    C = pickle.load(open("max.p", "rb"))
    plt.plot(A, 'r--', B, 'b--', C, 'g--')
    line1, = plt.plot([0, 0, 0], label="Min", linewidth=4)
    line2, = plt.plot([0, 0, 0], label="Max", linewidth=4)
    line3, = plt.plot([0, 0, 0], label="Media", linewidth=4)
    first_legend = plt.legend(handles=[line1], loc=9)
    ax = plt.gca().add_artist(first_legend)
    second_legend = plt.legend(handles=[line2], loc=2)
    ay = plt.gca().add_artist(second_legend)
    plt.legend(handles=[line3], loc=1)
    plt.show()


plot_test_hash_open()
