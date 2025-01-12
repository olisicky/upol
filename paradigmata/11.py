from datetime import datetime

import aio
import micro_widget as mw


# 1
'''
U korutiny je yield používán pro příjem i výdej hodnot. Oproti tomu u generátorů
se používá jenom pro výdej hodnot. Příjem hodnot pomocí c.send()

Jestli chci příjmant hodnoty, tak musím použít ten tvar variable = yield
'''

# Nevím, je to pičovina
def memory():
    prev = None
    while True:
        value = yield prev
        prev = value
c = memory()
next(c)

c.send(1)
c.send(2)

# 2 

async def return_after(delay, value):
    sleep = aio.sleep(delay)
    await sleep
    return value

#print(aio.run(return_after(1, 'ahoj')))

# 3


async def corutine_add(c1, c2):
    # pozor, tady není navrácena hodnota z funkce, tu dostanu až z await
    promise1 = aio.arun(c1)
    promise2 = aio.arun(c2)
    num1 = await promise1
    num2 = await promise2
    return num1 + num2

#print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#print(aio.run(corutine_add(return_after(2, 3), return_after(3, 4))))
#print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# 4

async def nekonecna(string, delay):
    while True:
        # bez arun to printilo pořád rychle za sebou
        sleep = aio.sleep(delay)
        promise = aio.arun(sleep)
        await promise
        print(string)

# aio.run(nekonecna("Ahoj Kájo", 5))

# 5

async def print_AB():
    prom1 = aio.arun(nekonecna('A', 1))
    prom2 = aio.arun(nekonecna('B', 2))
    await prom1
    await prom2

# aio.run(print_AB())

# 6

def click_handler(button):
    data = mw.get_button_data(button)
    text = mw.get_entry_text(data[0])
    aio.run(save_to_storage(text, data[1]))
    
    print(aio.run(get_text(data[1])))


async def save_to_storage(text, storage):
    promise = aio.arun(storage.set('text', text))
    await promise

async def get_text(storage):
    promise = aio.arun(storage.get('text'))
    text = await promise
    return text

#storage = aio.Storage().set_max_delay(1)
#w6 = mw.display_window()
#e6 = mw.make_entry(w6)
#b6 = mw.make_button(w6)
#mw.set_button_data(b6, [e6, storage])    # spojíme button a entry pro click handler
#mw.set_button_x(b6, 0)
#mw.set_button_y(b6, 30)
#mw.set_button_text(b6, "Store")
#mw.set_button_click_handler(b6, click_handler)


# 7
# Nějak mi blbne to vytáhnutí hodnoty z úložiště 

async def save_to_storage_7(data):
    text = mw.get_entry_text(data[0])
    promise = aio.arun(storage7.set('text', text))
    mw.set_label_text(data[1], 'saving')
    await promise
    mw.set_label_text(data[1], 'saved')

async def get_text_7(data):
    # nechci tady arun, protože musím mít vše uložené
    text = await storage7.get('text')
    print(text)

def click_handler7(button):
    data = mw.get_button_data(button)
    aio.arun(save_to_storage_7(data))
    mw.set_label_text(data[1], 'saved')
    aio.arun(get_text_7(data))

# funguje to, když pracuji v jednom storage globáním
#storage7 = aio.Storage().set_max_delay(10)
#w7 = mw.display_window()
#e7 = mw.make_entry(w7)
#b7 = mw.make_button(w7)
#l7 = mw.make_label(w7)
#mw.set_label_y(l7, 60)
#mw.set_button_data(b7, [e7, l7])    # spojíme button a entry pro click handler
#mw.set_button_x(b7, 0)
#mw.set_button_y(b7, 30)
#mw.set_button_text(b7, "Store")
#mw.set_button_click_handler(b7, click_handler7)

async def main_7(window):
    while mw.is_window_opened(window):
        mw.update_window(window)
        await aio.sleep(0.05)

#aio.run(main_7(w7))


# 9

import time
def get_current_time():
    return time.strftime("%H:%M:%S", time.gmtime())

# w9 = mw.display_window()
# l9 = mw.make_label(w9)

async def main_9(window):
    while mw.is_window_opened(window):
        mw.update_window(window)
        await aio.sleep(0.05)
        mw.set_label_text(l9, get_current_time())

# aio.run(main(w9))


# 10
def button_click_handler_10(button):
    data = mw.get_button_data(button)
    t1 = mw.get_entry_text(data[0])
    t2 = mw.get_entry_text(data[1])

    aio.arun(save_data(data[2], t1, t2))
    aio.arun(get_data(data))

async def save_data(storage, t1, t2):
    await storage.set('e1', t1)
    await storage.set('e2', t2)

async def get_data(data):
    p2 = aio.arun(data[2].get('e1'))
    p3 = aio.arun(data[2].get('e2'))
    await aio.sleep(0.5)
    t1 = await p2
    t2 = await p3
    mw.set_entry_text(data[0], t2)
    mw.set_entry_text(data[1], t1)
    
async def main_10(window):
    while mw.is_window_opened(window):
        mw.update_window(window)
        await aio.sleep(0.05)
#storage = aio.Storage()
#w10 = mw.display_window()
#e101 = mw.make_entry(w10)
#e102 = mw.make_entry(w10)
#mw.set_entry_y(e102, 30)
#b10 = mw.make_button(w10)
#mw.set_button_y(b10, 60)
#mw.set_button_text(b10, "swap")
#mw.set_button_data(b10, [e101, e102, storage])
#mw.set_button_click_handler(b10, button_click_handler_10)
#aio.run(main_10(w10))


# 12
def entry_change_handler_1(entry):
    aio.arun(save_entry('1', mw.get_entry_text(entry)))

def entry_change_handler_2(entry):
    aio.arun(save_entry('2', mw.get_entry_text(entry)))

async def save_entry(key, text):
    prom = aio.arun(storage12.set(key, text))
    await prom

async def main_12(window):
    while mw.is_window_opened(window):
        mw.update_window(window)
        await aio.sleep(1)

storage12 = aio.Storage()
w12 = mw.display_window()
e12_1 = mw.make_entry(w12)
e12_2 = mw.make_entry(w12)
mw.set_entry_y(e12_2, 30)
mw.set_entry_change_handler(e12_1, entry_change_handler_1)
mw.set_entry_change_handler(e12_2, entry_change_handler_2)


aio.run(main_12(w12))

# 13
# debilně se zjišťuje, jestli to něco dělá, tento vynechávám

