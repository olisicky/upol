import micro_widget as mw

# 1
def make_counter_1():
    value = 0
    return ['counter', value]


def get_counter_value(counter):
    return counter[1]

def inc_counter(counter):
    counter[1] += 1


def set_counter_value(counter, value):
    counter[1] = value

# 2
def click_handler(button):
    inc_counter(counter)
    mw.set_button_text(button, str(get_counter_value(counter)))

def make_change_button(window):
    button = mw.make_button(window)
    mw.set_button_text(button, 'initial')
    mw.set_button_click_handler(button, click_handler)

# 3
def entry_handler(entry):
    ''' Note: Tady podle mě špatně používám přístup k datů, protože by měl existovat mw.get_entry_text(entry).
    Já to jenom odrbal přístupem přímo k datů, protože je to list, ale tak bych to dělat neměl. Platí i dále. '''
    if entry[5].isdigit():
        mw.set_label_text(label, entry[5])

def _make_integer_entry(window):
    entry = mw.make_entry(window)
    text = entry[1]
    mw.set_entry_change_handler(entry, entry_handler)
# 4
def make_integer_entry(window):
    entry = mw.make_entry(window)
    text = entry[1]
    mw.set_entry_change_handler(entry, entry_handler)
    return entry

def set_integer_entry(integer_entry, value):
    mw.set_entry_text(integer_entry, str(value))

def get_integer_entry(integer_entry):
    return mw.get_entry_text(integer_entry)

def is_integer_entry_valid(integer_entry):
    if (mw.is_entry(integer_entry)) and (integer_entry[5].isdigit()) and (int(integer_entry[5]) > 0):
        return True
    else:
        return False

# 5
def  (window):
    entry = mw.make_entry(window)
    button = mw.make_button(window)
    mw.set_button_text(button, 'reset')
    mw.set_button_y(button, 40)
    res_entry = ['resetable_entry', entry, button]
    mw.set_button_data(button, res_entry)    # přidání celku do dat tlačítka
    return res_entry
# 6
def set_resetable_entry_x(resetable_entry, x):
    entry_x = mw.get_entry_x(resetable_entry[1])
    mw.set_entry_x(resetable_entry[1], x + entry_x)
    button_x = mw.get_button_x(resetable_entry[2])
    mw.set_button_x(resetable_entry[2], x + button_x)

def set_resetable_entry_y(resetable_entry, y):
    entry_y = mw.get_entry_y(resetable_entry[1])
    mw.set_entry_y(resetable_entry[1], y + entry_y)
    button_y = mw.get_button_y(resetable_entry[2])
    mw.set_button_y(resetable_entry[2], y + button_y)

def get_resetable_entry_x(resetable_entry):
    return mw.get_entry_x(resetable_entry[1])

def get_resetable_entry_y(resetable_entry):
    return mw.get_entry_y(resetable_entry[1])


# 7
def counter_click_handler(button):
    current_data = mw.get_button_data(button)
    current_data[1] += 1
    mw.set_button_data(button, current_data)
    mw.set_entry_text(current_data[0], str(current_data[1]))

def make_counter(window):
    entry = mw.make_entry(window)
    button = mw.make_button(window)
    mw.set_button_y(button, 40)
    mw.set_button_text(button, '+')
    mw.set_button_data(button, [entry, 0])
    mw.set_button_click_handler(button, counter_click_handler)
    return ['counter', button, entry]
    
def set_counter_x(counter, x):
    entry_x = mw.get_entry_x(counter[2])
    mw.set_entry_x(counter[2], x + entry_x)
    button_x = mw.get_button_x(counter[1])
    mw.set_button_x(counter[1], x + button_x)

def set_counter_y(counter, y):
    entry_y = mw.get_entry_y(counter[2])
    mw.set_entry_y(counter[2], y + entry_y)
    button_y = mw.get_button_y(counter[1])
    mw.set_button_y(counter[1], y + button_y)


window = mw.display_window()
label = mw.make_label(window)
mw.set_label_x(label, 10)
mw.set_label_y(label, 50)
counter = make_counter_1()
# 4
w4 = mw.display_window()
integer_entry = make_integer_entry(w4)
set_integer_entry(integer_entry, 5)
get_integer_entry(integer_entry)
print(is_integer_entry_valid(integer_entry))

# 5 + 6
w5 = mw.display_window()
resetable_entry1 = make_resetable_entry(w5)
resetable_entry2 = make_resetable_entry(w5)
set_resetable_entry_y(resetable_entry2, 80)

# 7
w7 = mw.display_window()
counter1 = make_counter(w7)
