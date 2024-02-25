
test = [1, 2, 3, 4, 5]
f = lambda x, y: x + y
# f = lambda x, y: x * y
# f = lambda x, y: x / y
# f = lambda x, y: x + (3*y)

def aplikuj(f, sekvence):

    for i, element in enumerate(sekvence):
        if i == 0:
            res = element
        else:
            res = f(res, element)
    return res

print(aplikuj(f, test))