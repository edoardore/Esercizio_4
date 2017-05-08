from test import TestA

import pickle, matplotlib.pyplot as plt, numpy as np

lista_test = [1000, [10, 20, 30, 40, 50, 60, 70, 75, 85, 87, 89, 90, 91, 92, 93, 94, 95, 97, 98, 99, 100]]
pickle.dump(lista_test, open("list.p", "wb"))


def plot_test_hash_open():
    TestA()
    A = pickle.load(open("medie.p", "rb"))
    B = pickle.load(open("min.p", "rb"))
    C = pickle.load(open("max.p", "rb"))
    plt.plot(A, 'r--', B, 'b--', C, 'g--')
    plt.show()


plot_test_hash_open()
