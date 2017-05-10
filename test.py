from hash import HashOpen, HashChained
import pickle, random


def random_list(max, size):
    rands = [random.randint(0, max) for x in range(size)]
    return rands

def TestOpen():
    lista_test = pickle.load(open("list.p", "rb"))
    j = 0
    lista_collisioni_medie = range(len(lista_test[1]))
    lista_collisioni_min = range(len(lista_test[1]))
    lista_collisiini_max = range(len(lista_test[1]))
    length = len(lista_test[1])
    while j < length:
        print ">>>>>>>>>>>>> Test con ", (lista_test[0] * lista_test[1][j]) / 100, "elementi caricati:"
        collisioni = range(20)
        sequenze = range(20)

        k = 0
        while k < 20:
            hash_open = HashOpen(lista_test[0])
            A = random_list(100 * lista_test[0], (lista_test[0] * lista_test[1][j]) / 100)
            size = len(A)

            for i in range(0, size):
                hash_open.insert(A[i])
            collisioni[k] = hash_open.collisions
            sequenze[k] = hash_open.sequenze / size
            k += 1

        k = 0
        collisioni_medie = 0
        sequenze_medie = 0
        while k < 20:
            collisioni_medie += collisioni[k]
            sequenze_medie += sequenze[k]
            k += 1
        collisioni_medie = collisioni_medie / 20
        sequenze_medie = sequenze_medie / 20

        k = 0
        sequenze_min=sequenze[0]
        collisioni_min = collisioni[0]
        while k < 20:
            if collisioni[k] < collisioni_min:
                collisioni_min = collisioni[k]
            if sequenze[k] < sequenze_min:
                sequenze_min = sequenze[k]
            k += 1

        k = 0
        sequenze_max = sequenze[0]
        collisioni_max = collisioni[0]
        while k < 20:
            if collisioni[k] > collisioni_max:
                collisioni_max = collisioni[k]
            if sequenze[k] > sequenze_max:
                sequenze_max = sequenze[k]
            k += 1

        print "Collisioni Medie:", collisioni_medie, "Minimo delle Collisioni:", collisioni_min, "Massimo delle Collisioni:", collisioni_max
        print "Sequenze Medie:", sequenze_medie, "Sequenza Minima:", sequenze_min, "Sequenza Massima:", sequenze_max
        lista_collisioni_medie[j] = collisioni_medie
        lista_collisioni_min[j] = collisioni_min
        lista_collisiini_max[j] = collisioni_max

        j += 1
    pickle.dump(lista_collisioni_medie, open("medie.p", "wb"))
    pickle.dump(lista_collisioni_min, open("min.p", "wb"))
    pickle.dump(lista_collisiini_max, open("max.p", "wb"))

def TestChained():
    lista_test = pickle.load(open("list.p", "rb"))
    j = 0
    lista_collisioni_medie = range(len(lista_test[1]))
    lista_collisioni_min = range(len(lista_test[1]))
    lista_collisioni_max = range(len(lista_test[1]))
    length = len(lista_test[1])
    while j < length:
        print ">>>>>>>>>>>>> Test con ", (lista_test[0] * lista_test[1][j]) / 100, "elementi caricati:"
        collisioni = range(20)

        k = 0
        while k < 20:
            hash_chained = HashChained(lista_test[0])
            A = random_list(100 * lista_test[0], (lista_test[0] * lista_test[1][j]) / 100)
            size = len(A)

            for i in range(0, size):
                key = random.randint(0, hash_chained.size)
                hash_chained.insert(A[i], key)
            collisioni[k] = hash_chained.collision
            k += 1
        k = 0

        collisioni_medie = 0
        while k < 20:
            collisioni_medie += collisioni[k]
            k += 1
        collisioni_medie = collisioni_medie / 20

        k = 0
        collisioni_min = collisioni[0]
        while k < 20:
            if collisioni[k] < collisioni_min:
                collisioni_min = collisioni[k]

            k += 1

        k = 0
        collisioni_max = collisioni[0]
        while k < 20:
            if collisioni[k] > collisioni_max:
                collisioni_max = collisioni[k]
            k += 1

        print "Collisioni Medie:", collisioni_medie, "Minimo delle Collisioni:", collisioni_min, "Massimo delle Collisioni:", collisioni_max
        lista_collisioni_medie[j] = collisioni_medie
        lista_collisioni_min[j] = collisioni_min
        lista_collisioni_max[j] = collisioni_max
        j += 1

    pickle.dump(lista_collisioni_medie, open("cmedie.p", "wb"))
    pickle.dump(lista_collisioni_min, open("cmin.p", "wb"))
    pickle.dump(lista_collisioni_max, open("cmax.p", "wb"))
