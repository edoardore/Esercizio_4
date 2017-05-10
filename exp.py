from test import TestOpen, TestChained

import pickle, matplotlib.pyplot as plt, matplotlib.patches as mpatches


def pickling():
    lista_test = [1000, [10, 20, 30, 40, 50, 60, 70, 75, 85, 87, 89, 90, 91, 92, 93, 94, 95, 97, 98, 99, 100]]
    pickle.dump(lista_test, open("list.p", "wb"))


def plot_test_hash_open():
    TestOpen()
    lista_test = pickle.load(open("list.p", "rb"))
    A = pickle.load(open("medie.p", "rb"))
    B = pickle.load(open("min.p", "rb"))
    C = pickle.load(open("max.p", "rb"))
    plt.plot(lista_test[1], A, 'r--', lista_test[1], B, 'b--', lista_test[1], C, 'g--')
    line1, = plt.plot([], label="Min", linewidth=4)
    line2, = plt.plot([], label="Max", linewidth=4)
    line3, = plt.plot([], label="Media", linewidth=4)
    first_legend = plt.legend(handles=[line1], loc=1)
    ax = plt.gca().add_artist(first_legend)
    second_legend = plt.legend(handles=[line2], loc=2)
    ay = plt.gca().add_artist(second_legend)
    plt.legend(handles=[line3], loc=9)
    plt.ylabel('# Collisioni in Hash ad indirizzamento aperto')
    plt.xlabel('Percentuale valori caricati')

    plt.show()


def plot_test_hash_chained():
    TestChained()
    lista_test = pickle.load(open("list.p", "rb"))
    A = pickle.load(open("cmedie.p", "rb"))
    B = pickle.load(open("cmin.p", "rb"))
    C = pickle.load(open("cmax.p", "rb"))
    plt.plot(lista_test[1], A, 'r--', lista_test[1], B, 'b--', lista_test[1], C, 'g--')
    line1, = plt.plot([], label="Min", linewidth=4)
    line2, = plt.plot([], label="Max", linewidth=4)
    line3, = plt.plot([], label="Media", linewidth=4)
    first_legend = plt.legend(handles=[line1], loc=1)
    ax = plt.gca().add_artist(first_legend)
    second_legend = plt.legend(handles=[line2], loc=2)
    ay = plt.gca().add_artist(second_legend)
    plt.legend(handles=[line3], loc=9)
    plt.ylabel('# Collisioni in Hash concatenato')
    plt.xlabel('Percentuale valori caricati')
    plt.show()


pickling()

plot_test_hash_open()

plot_test_hash_chained()
