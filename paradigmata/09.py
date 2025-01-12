
from fmw import *
# label, moved, button, entry, group(přímo items, ale jenom 2!)

# 2

def counter(value):
    ''' Definovaná bez akce pro to, aby to něco udělalo. ?? '''
    return group(
        label(str(value)),
        group(
            moved(button("+", action=value + 1), 0, 20),
            moved(button("Reset", 0), 0, 40)
        )
    )
# display_window(counter, 0)


def counter2(values):
    ''' S využitím akcí, ale přes nex_state u display_window '''
    counter_ = action_changed(
        group(
            label(str(values[0])),
            button("+", True, 0, 20)
        ),
        0    # ID
    )
    reset = action_changed(
        button("Reset", 1, 0, 40),
        1   # ID
    )
    return group(counter_, reset)

def values_change(values, action):
    '''
    action vrací [ID, nastavená hodnota action u widget]
    V mém případu [0, True] u counter button a [1, 1] u reset button.
    Vracím values, se kterýma pracuji u těch widgets. Tím, že vždy v label
    vykresluji values[0], tak záleží, co tam kdy nastavím. Proto když je
    zmáčknutý reset, tak tam musím nastavit jiné hodnoty. 
    '''
    return [values[0] + 1, 0] if action[0] == 0 else [0, 0]
    
# display_window(counter2, [0 , 0], values_change)


# 3
def counter3(value):
    ''' Definovaná bez akce pro to, aby to něco udělalo. ?? '''
    return group(
        label(str(value)),
        group(
            moved(button("+", action=value + 1), 0, 20),
            moved(button("-", action=(lambda x: (0 if x<1 else x-1))(value)), 0, 40)
        )
    )
#display_window(counter3, 0)

# 4
'''
Ta akce u každoho widgetu je navázaná s akcí, kterou definuji
u display_window. Když mám více akcí u více widgetů, tak musím říct, která se děje.
U té akce nemusí být True viz skripta ale jakákoliv nenulová hodnota,
třeba 0 nebo i False :D.
'''

def next_string(string, action):
    return action[1]

def pole4(value):
    return group(
        entry(value, 'cokoliv co není None :D'),
        label(str(len(value)), 0, 30)
    )

# display_window(pole4, "", next_string)

# 5

def dve_pole(strings):
    return group(
        action_changed(entry(strings[0], True), 0),
        action_changed(entry(strings[1], True, 0, 30), 1)
    )

def palindrom(strings, actions):
    '''
    Tady je matoucí, že vlastně ty změny jsou v akcích (což není vlastně matoucí),
    jen ty strings reálně nenesou nic :D 
    '''
    return [actions[1], actions[1][::-1]] if actions[0][0] == 0 else [actions[1][::-1], actions[1]]

# display_window(dve_pole, ['', ''], palindrom)


# 6

def dve_pole_soucet(strings):
    entry_1 = action_changed(entry(strings[0], True), 0)
    entry_label = action_changed(
        group(
            entry(strings[1], True, 0, 20),
            label(str(len(strings[0]) + len(strings[1])), 0, 50)
        ),
        1
    )
    return group(entry_1, entry_label)

def count_words(strings, actions):
    return [actions[1], strings[1]] if actions[0][0] == 0 else [strings[0], actions[1]]

# display_window(dve_pole_soucet, ["", ""], count_words)


# 7
def dve_pole_swap(inputs):
    '''
    podle toho, kolik těch action_change nadefinujeme, tolik
    akcí potom bude na kontrolu. Je to trochu debilní hlavně na indexy, protože
    výstup akce z tlačítka má jiné pořadí než z entry, ale nějak se to dá ještě
    pohlídat, ale je to teda nepřehledné :D .
    '''
    entry_1 = action_changed(entry(inputs[0], True), 0)
    entry_button = action_changed(
        group(
            entry(inputs[1], True, 0, 30),
            action_changed(button("swap", True, 0, 60), 2)
        ),
        1
    )
    return group(entry_1, entry_button)

def swap(inputs, actions):
    return (([actions[1], inputs[1]] if actions[0][0] == 0 else [inputs[0], actions[1]]) if actions[1][0] != 2
        else ([inputs[1], inputs[0]]))

display_window(dve_pole_swap, ["", "", 0], swap)


