from proto import obj
from pmw import *

# 1
counter_1 = obj.clone()
counter_1.set_name('counter')
counter_1.add_slot('value')    # vytvoří i `set_value`
counter_1.set_value(0)


c1 = counter_1.clone()
c1.value()
c1.set_value(2)
c1.value()

# counter tady zatím neumí být zobrazem až dále bude dědit vlastnosti

# 2
# pokračujeme s prototypem counter z 1

def counter_inc_value(resend, self):
    self.set_value(self.value() + 1)
    return self

counter_1.set_slot('inc', counter_inc_value)
c2 = counter_1.clone()
c2.inc()    # teď už rozumí i zprávě inc

# 3
# create clones of label and button for the group
l1 = label.clone().set_text("0")
b1 = button.clone().set_text("+").move(0, 20)
b1.set_name('button')
# create group which consists label and the button
counter_group = group.clone().set_items([l1, b1])
# set name for the group. This is probably badly writen (the names)
counter_group.set_name('counter_group')
# set initial value and name
counter_group.add_slot('value')
counter_group.set_value(0)

counter_3 = counter_group.clone()
counter_3.set_name('counter')


c3 = counter_3.clone()
w3 = window.clone()
w3.set_widget(c3)
w3.display()

# 4
# pokračujeme z counter_3. Není to ideální furt takhle dědit, ale je to dementí
# pro řešení všeho v jednom souboru...
counter_4 = counter_3.clone()
counter_4.add_slot('button')
counter_4.add_slot('label')
counter_4.set_button(counter_4.items()[1])
counter_4.set_label(counter_4.items()[0])
c4 = counter_4.clone()
c4.label()
c4.button()

# 5

def counter_value(resend, self):
    print(self.value())
    self.label().set_text(str(self.value()))
    return self.value()

counter_4.set_slot('value', counter_value)

c5 = counter_4.clone()
# ____________________ 6 _______________________
'''
I have a problem with set_value, because as I rewrite it
then it stops working properly :D.

counter_inc_value calls set_value which will only change the label
but not the self.value() which is set through set_value which is then
recursively calling self

ŘEŠENÍ: self.set_slot('value', value)

Tohle už je hrozně zamotané, co se vůbec chce. Podle mě mám až moc kopií, což
není vůbec dobře... raději končím, nebo se do toh zamotám :D 

'''
# add counter increments.
def counter_inc_value(resend, self):
    return self.set_value(self.value() + 1)

def counter_dec_value(resend, self):
    return self.set_value(self.value() - 1)

counter.set_slot('inc', counter_inc_value)
counter.set_slot('dec', counter_dec_value)

# add event when button is clicked
def counter_ev_button_clicked(resend, self, button):
    self.inc()    # increment value when the button is clicked
    self.items()[0].set_text(str(self.value()))
    return self

counter.set_slot("ev_button_clicked", counter_ev_button_clicked)



counter1 = counter.clone()
counter2 = counter.clone().move(100, 0)

#widget_group1 = group.clone().set_items([counter1, counter2])
#window1 = window.clone()
#window1.set_widget(widget_group1)
#window1.display()


# ____________________ 7 _______________________
'''
Nevím, jak řešit ty eventy na více tlačítkách v jedné instanci. Tím, že je tam obecně button, tak nevím.
'''


