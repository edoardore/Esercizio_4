class Nodo:
    def __init__(self, nodo):
        self.nodo = nodo
        self.next = None

    def get_nodo(self):
        return self.nodo

    def get_next(self):
        return self.next

    def set_nodo(self, nodo):
        self.nodo = nodo

    def set_next(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.collision = 0

    def is_empty(self):
        return self.head is None

    def __add__(self, other):
        if self.head is not None:
            self.collision = 1
        return self.collision
        t = Nodo(other)
        t.set_next(self.head)
        self.head = t

    def size(self):
        value = self.head
        count = 0
        while value is not None:
            value = value.get_next()
            count += 1
        return count

    def search(self, v):
        value = self.head
        found = False
        while found is False and value is not None:
            if value.get_nodo() == v:
                found = True
            else:
                value = value.get_next()
        return found

    def print_list(self):
        value = self.head
        while value is not None:
            print "...", value.get_nodo()
            value = value.get_next()

    def __delete__(self, other):
        value = self.head
        prev = None
        found = False
        if self.head is None:
            return found
        while found is False and value is not None:
            if value.get_nodo() == other:
                found = True
            else:
                prev = value
                value = value.get_next()
            if found is False:
                return found
            if prev is None:
                self.head = value.get_next()
            else:
                prev.set_next(value.get_next())
            return found


class HashChained:
    def __init__(self, m):
        boolean = True
        while boolean:
            a = True
            i = 2
            while i < m and a:
                if m % i == 0:
                    a = False
                i += 1
            if not a:
                m -= 1
            else:
                boolean = False
        self.size = m
        print "HashChained m is:", self.size
        self.collision = 0
        self.slot = range(self.size)
        for j in range(0, self.size):
            self.slot[j] = LinkedList()

    def insert(self, value, key):
        h = key % self.size
        self.collision += self.slot[h].__add__(value)

    def print_hash(self):
        for i in range(0, self.size):
            print "Slot:", i
            self.slot[i].print_list()

    def search(self, value, key):
        h = key % self.size
        print "Valore presente in slot", h, ":", self.slot[h].search(value)

    def delete(self, value, key):
        h = key % self.size
        found = self.slot[h].__delete__(value)
        if found is False:
            print "Impossibile Cancellare"


class HashOpen:
    def __init__(self, m):
        boolean = True
        while boolean:
            a = True
            i = 2
            while i < m and a:
                if m % i == 0:
                    a = False
                i += 1
            if not a:
                m += 1
            else:
                boolean = False
        self.collisions = 0
        self.size = m
        #print "HashOpen m is:", self.size
        self.list = range(0, self.size)
        for j in range(0, self.size):
            self.list[j] = None

    def insert(self, value):
        i = 0
        a = True
        while i < self.size and a:
            h = (value + i) % self.size
            if self.list[h] is None:
                self.list[h] = value
                a = False
            else:
                i += 1
                self.collisions += 1

    def print_hash(self):
        print self.list

    def delete(self, value):
        delete = False
        i = 0
        while not delete and i < self.size:
            h = (value + i) % self.size
            if self.list[h] == value:
                self.list[h] = None
                delete = True
            else:
                i += 1

    def search(self, value):
        found = False
        i = 0
        while not found and i != self.size:
            if self.list[i] == value:
                found = True
            else:
                i += 1
        if found:
            print "Elemento presente in posizione:", i, "di:", self.size
        else:
            print "Elemento non presente."

