from hash import HashChained, HashOpen
import random

t_concatenamento = HashChained(1000)
t_indirizzamento_aperto = HashOpen(1000)


def TestA(HashChained):
    A = random_list(1000,1000)
    size=len(A)
    for i in range(0, size):
        t_concatenamento.insert(A[i],i)


def TestB(HashOpen):
    A=random_list(1000,1000)
    size=len(A)
    for i in range(0, size):
        t_indirizzamento_aperto.insert(A[i])
    t_indirizzamento_aperto.print_hash()



def random_list(max, size):
    rands = [random.randint(0, max) for x in range(size)]
    return rands


TestB(t_indirizzamento_aperto)