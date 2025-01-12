from co import *

x = None

def f1():
    global x
    random_sleep()
    x = 1

def f2():
    global x
    random_sleep()
    x = 2
    
co_call(f1, f2)

# 1


x = 1
y = 1

def f1():
    global x
    random_sleep()
    x = 2
    random_sleep()
    x = 3

def f2():
    global y
    y = x
    
co_call(f1, f2)

# 3


x = 1
y = 1

def f1():
    global x
    random_sleep()
    x = x + 1

def f2():
    global y
    y = y + 1
    

# 5

x5 = 0
y5 = 0
lock5 = make_lock()

def f1():
    global x5
    random_sleep()
    with lock5:
        x5 = 1

def f2():
    global y5
    with lock5:
        y5 = x5 + x5

co_call(f1, f2)

# 7

q = Queue()
def f1():
    x = 0
    while x < 11:
        x = x + 1
        random_sleep()
        q.put(x)

def f2():
    res = 1
    while res:
        res = q.get()
        if res < 10:
            print(res)
        else:
            res = False

# co_call(f1, f2)

# 8

q = Queue()
def f1():
    x = 0
    while x < 11:
        x = x + 1
        random_sleep()
        q.put(x)

def f2():
    cont = True
    while cont:
        try:
            res = q.get()
            print(res)
            print(q.get(False))
        except:
            cont = False


# co_call(f1, f2)

# 9 - hm nefunguje :D 




def run_9():
    q1 = Queue()
    q2 = Queue()

    def f1():
        x = 0
        while x < 10:
            x = x + 1
            q1.put(x)

    def f2():
        x= 0
        while x < 10:
            x = x + 1
            q2.put(x)


    def f3():
        random_sleep(0.1)
        x = 0
        y = 0

        while (x<0 and y<0):
            x = q1.get()
            y = q2.get()
            print(x + y)
    co_call(f1, f2, f3)



