"""
JednoduchĂĄ knihovna na paralelnĂ­ vĂ˝poÄty.


co_call(function1, ..., functionN)

    ParalelnÄ zavolĂĄ funkce <function1>, ..., <functionN> bez argumentĹŻ.

    TÄlo kaĹždĂŠ z uvedenĂ˝ch funkcĂ­ se vykonĂĄvĂĄ v samostatnĂŠm procesu.

    ÄekĂĄ, neĹž volĂĄnĂ­ funkcĂ­ skonÄĂ­.


random_sleep(duration=0.01)

    ÄekĂĄ nĂĄhodnĂ˝ Äas. NevĂ­ĹĄe <duration> sekund.


safe_print(value1, ..., valueN)

    Vytiskne hodnoty <value1>, ..., <valueN>.

    Nutno pouĹžĂ­t mĂ­sto print pĹi tisku v paralelnĂ­m programu.


make_lock()

    VytvoĹĂ­ zĂĄmek.

    PouĹžitĂ­:

    lock = make_lock()
    with lock:
        <block>
      
    
TĹĂ­da Queue:

   Instance je fronta.

   queue.put(item) => None
       VloĹžĂ­ hodnotu <item> nakonec fronty.

   queue.get() => value
       Odebere a vrĂĄtĂ­ prvek ze zaÄĂĄtku fronty. PĹĂ­padnÄ ÄekĂĄ, aĹž je to moĹžnĂŠ.
   

"""

import threading as _threading
import time as _time
import random as _random
import queue as _queue 
Queue = _queue.Queue
QueueEmpty = _queue.Empty

def start_process(function, *args):
    process =_threading.Thread(target=function, args=args)
    process.start()
    return process

def join_process(process):
    process.join()
    
def co_call(*functions):
    """ParalelnÄ zavolĂĄ funkce <functions> bez argumentĹŻ."""
    processes = list(map(start_process, functions))
    for process in processes:
        process.join()
        
def random_sleep(duration=0.01):
    """ÄekĂĄ nĂĄhodnĂ˝ Äas. NevĂ­ĹĄe <duration> sekund."""
    _time.sleep(_random.random() * duration)

def make_lock():
    """VytvoĹĂ­ zĂĄmek."""
    return _threading.Lock()

_print_lock = make_lock()

def safe_print(*values):
    """Vytiskne hodnoty <values>. Lze pouĹžĂ­t i ve vlĂĄknech."""
    with _print_lock:
        print(*values)
    
