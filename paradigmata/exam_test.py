# z ukázkové zkoušky
from lst import (
    cons,
    first,
    rest,
    is_empty,
    NonEmpty,
    Empty
)

empty = Empty()
l1 = cons(1, cons(2, cons(3, cons(4, empty))))


def all_even(lst):
    return (
        empty if is_empty(lst)
        else
        (cons(first(lst), all_even(rest(lst))) if first(lst) % 2 == 0 else all_even(rest(lst)))
    )


