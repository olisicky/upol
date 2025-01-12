from proto import obj
from pmw import *


def swap(f):
    return lambda x, y: f(y,x)
def mod(x, y):
    return x % y

