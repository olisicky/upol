

# pomocné z přednášek

empty = []
def cons(val, lst):
    ''' konstruktor seznamu '''
    return [val, lst]

def is_empty(lst):
    return lst == empty

def first(lst):
    return lst[0]

def rest(lst):
    return lst[1]

def list_map(fun, lst):
    return (empty
        if is_empty(lst)
        else cons(fun(first(lst)),
            list_map(fun, rest(lst))))

def list_filter(predicate, lst):
    return (empty
            if is_empty(lst)
            else (cons(first(lst), list_filter(predicate, rest(lst)))
                  if predicate(first(lst))
                  else list_filter(predicate, rest(lst))))


def list_reduce(function, init, lst):
    return (init
            if is_empty(lst)
            else function(first(lst),
                          list_reduce(function,
                                      init,
                                      rest(lst))))

# 1
def list_nth(lst, index):
    return (first(lst) if index == 0
            else list_nth(rest(lst), index - 1))

l1 = cons(1, cons(2, cons(3, cons(4, empty))))
list_nth(l1, 2)

# 2
# první jsem to měl naopak, ale stačí jen popřemýšlet nad argumenty a pořadím
def list_range(m, n):
    return (empty if n == m else
            cons(m, list_range(m + 1, n)))


# 3

def is_every(p, lst):
    return (
        (True if is_empty(lst) else p(first(lst)))
            if (is_empty(lst) or not p(first(lst))) 
            else is_every(p, rest(lst))
    )

# 4

def list_find(p, lst):
    return (
        ([first(lst)] if not is_empty(lst) else empty) if (is_empty(lst) or p(first(lst)))
        else list_find(p, rest(lst))
    )

# 5

l5 = cons(-1, cons(2, cons(-3, cons(4, empty))))
lst_abs = list_map(lambda x: abs(x), l5)

# 6

lst_kladna = list_filter(lambda x: x>0, l5)

# 7

lst_sum = list_reduce(lambda x, y: (x)**2 + y, 0, l5)
# y je tam zamýšlený aktuální součet

# 8

def sum_sou(lst):
    return list_reduce(lambda x, y: x*y, 1, list_filter(lambda x: x % 2 == 0, lst))


# 9

#def list_every_second(lst):
#    return cons(first(lst), ) if list_nth(lst, 2)

# 10

def length(lst):
    return (0 if is_empty(lst)
        else 1 + length(rest(lst)))

def list_last(lst):
    return (first(lst) if length(lst) == 1
            else list_last(rest(lst))
    )

# 11

def list_append(l1, l2):
    return (cons(first(l1), l2) if length(l1) == 1
            else list_append(list_filter(lambda x: x != list_last(l1), l1), cons(list_last(l1), l2))
    )
# tady nechci rest ale jakoby rest bez posledního, což dělám přes list_filter

# 12

#def list_reverse(lst):
#    return (lst if 
#            else cons(list_last(lst), list_filter(lambda x: x != list_last(lst), lst))
#    )





