
'''
Moc nechápu, co chce v tom úkolu na konci přednášky, tak vyzkouším jenom nějaké
iterátory tady.
'''


lst = [1, 2, 3, 4, 5]
i = iter(lst)
next(i)   # 1
# když vytvořím nový iterátor z původního, tak pořád "čerpám" stejný  Iterable

ii = iter(i)
next(ii)    # 2


# třeba range není iterator, ale je iterable, takže jej musím první převést
# na iterátor přes iter

ir = iter(range(10))

# map, filter hned vytvoří iterátor, zajímavé
im = map(lambda x: x + 1, [0, 1, 2])



class Ones:

    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        return 1

o = Ones()
next(o)    # 1


class Sentences:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return iter(self.string.split('.'))

s = Sentences("Ahoj Karle. Jsi kočka.")
for i in s:
    print(i)


# Generátory

def gen(lst):
    for i in lst:
        yield i
    # tady se to dostane až po vyčerpání, může napsat hotovo :D 
    print('nečum')

g = gen([0, 1, 2])    # generátor vrací iterátor
next(g)    # 0

# Generující výrazy
# - výhoda, že je to anonymní a lehce definovatelné s podmínkama
# - asi hlavně použití tam, kde mám velká data, která bych nenarval do paměti

gen_e = (x for x in [0, 1, 2, 3] if x > 1)


# Eratosthenovo síto

def get_numbers():
    i = 0
    while True:   # nekonečná smyčka - > generátor čísel
        yield i
        i = i + 1    # vykonáno až při druhém next()

def is_divisor(a, b):
    return (b % a) == 0

def remove_multiples(n, iterable):
    return filter(lambda m: not is_divisor(n, m), iterable)

numbers = get_numbers()

next(numbers)    # odebírám 0 z posloupnosti
next(numbers)    # odebírám 1 z posloupnosti

def get_primes(num):
    while True:
        prime = next(num)
        num = remove_multiples(prime, num)
        yield prime

primes = get_primes(numbers)
next(primes)
# ... atd dostávám primes 
