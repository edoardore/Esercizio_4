from hash import HashOpen, HashChained
import pickle


##idee per funzionamento del pickle
AA = [200, 10, 50, 90]

pickle.dump(AA, open("save.p", "wb"))

BB = pickle.load(open("save.p", "rb"))

A= range(1000)
T = HashChained(100)
for i in range(0, len(A)):
    T.insert(A[i],i)
T.print_hash()
