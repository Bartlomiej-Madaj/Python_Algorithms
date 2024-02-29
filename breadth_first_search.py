from collections import deque

class Person:
    def __init__(self, name, is_seller=False):
        self.name:str = name.capitalize()
        self.is_seller = is_seller
    
    def person_is_seller(self):
        return self.is_seller
    

you = Person('you')
bob = Person('bob')
claire = Person('claire')
alice = Person('alice')
thon = Person('thon', is_seller=True)
jonny = Person('jonny')
peggy = Person('peggy')
anuj = Person('anuj', )

network = dict()

network[you.name] = [you, bob, alice, claire]
network[alice.name] = [alice, peggy]
network[bob.name] = [bob, you, anuj, peggy]
network[claire.name] = [claire, thon, jonny]
network[anuj.name] = [anuj]
network[peggy.name] = [peggy]
network[thon.name] = [thon]
network[jonny.name] = [jonny]


def BFS(host_name):
    search_queue = deque()
    search_queue.append(host_name)
    searched = []
    while search_queue:
        person_name = search_queue.popleft()
        if person_name in searched:
            continue
        searched.append(person_name)
        person: Person = network[person_name][0]
        if person.is_seller:
            print(f"{person.name} is a seller.")
            return True
        else:
            search_queue.extend(i.name for i in  network[person.name] if i.name != person.name)
    print('No seller')
    return False

BFS(you.name)