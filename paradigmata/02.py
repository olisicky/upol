from pomw import *


#1

name = Label().set_text('Jméno:')

name_entry = Entry().move(0, 20)

last_name = Label().set_text('Příjmení:').move(0, 50)
last_entry = Entry().move(0, 70)

group_1 = Group().set_items([name, name_entry, last_name, last_entry])

w1 = Window()
w1.set_widget(group_1)


# 2

def make_counter():

    entry = Label().set_text('0')
    def counter_click_handler(button):
        '''
        Nevím, jak jinak dosáhnout na entry v tomto případě, kdy to nemám
        zavřené v nějaké třídě. Funguje to :D .
        '''
        button.set_data(button.get_data() + 1)
        entry.set_text(str(button.get_data()))

    button = Button().set_text('+').move(0, 20)
    button.set_data(0)    # set_data nevrací self, nemůžu řetězit!
    button.set_click_handler(counter_click_handler)
    entry.set_text(str(button.get_data()))
    counter = Group().set_items([entry, button])
    return counter

    
w2 = Window()
c1 = make_counter()
c2 = make_counter().move(0, 100)
group_2 = Group().set_items([c1, c2])
w2.set_widget(group_2)

# 3

def make_form():
    name = Label().set_text('Jméno:')
    name_entry = Entry().move(0, 20)

    last_name = Label().set_text('Příjmení:').move(0, 50)
    last_entry = Entry().move(0, 70)

    def click_handler(button):
        button.set_data([name_entry.get_text(), last_entry.get_text()])
        print(button.get_data())

    button = Button().move(0, 100).set_text('Registrace')
    button.set_click_handler(click_handler)
    group = Group().set_items([name, name_entry, last_name, last_entry, button])
    return group
w3 = Window()
form = make_form()
w3.set_widget(form)

#4

def make_form_pass():
    pass1 = Entry()
    pass2 = Entry().move(0, 30)
    label = Label().move(0, 60)
    
    def change_handler_1(entry):
        entry.set_data(entry.get_text())

    def change_handler_2(entry):
        entry.set_data(entry.get_text())
        if pass1.get_data() != entry.get_data():
            label.set_text('Hesla jsou různá')
        else:
            label.set_text('Hesla jsou stejná')

    pass1.set_change_handler(change_handler_1)
    pass2.set_change_handler(change_handler_2)
    
    group = Group().set_items([pass1, pass2, label])
    return group

w4 = Window()
w4.set_widget(make_form_pass())
