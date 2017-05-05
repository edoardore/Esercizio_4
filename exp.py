from hash import HashChained, HashOpen
import random
import pickle

def random_list(max, size):
    rands = [random.randint(0, max) for x in range(size)]
    return rands

def TestB(HashOpen):
    collisioni = []
    collisioni_medie = 0
    test = pickle.load(open("save.p", "rb"))
    i = 0
    while i < len(test[1]):
        A = random_list(100 * test[0], (test[0] * test[1][i] / 100))
        size = len(A)
        k = 0
        while k < 20:
            for i in range(0, size):
                HashOpen.insert(A[i])
            collisioni.append(HashOpen.collisions)
            k += 1
        k = 0
        while k < 2:
            collisioni_medie += collisioni[k]
            k += 1
        print collisioni_medie / 20
        i += 1

test = [1000, [10, 20, 30, 40, 50, 60, 70, 75, 85, 87, 89, 90, 91, 92, 93, 94, 95, 97, 98, 99, 100]]
pickle.dump(test, open("save.p", "wb"))
t_indirizzamento_aperto = HashOpen(1000)
TestB(t_indirizzamento_aperto)