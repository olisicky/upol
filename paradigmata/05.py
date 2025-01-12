from omw import *

# 1

class Buttons(Group):

    def ev_button_clicked(self, sender):
        '''
        Ta třída umí obsluhovat eventy, proto ví, co dát jako sender.
        Každopádně tam musí být i správný type... třeba ev_but_clicked nefunguje.
        '''
        print(sender.get_text())

#w1 = Window()
#b1 = Button().set_text('A')
#b2 = Button().set_text('B').move(0, 30)
#butts = Buttons().set_items([b1, b2])
#w1.set_widget(butts)


# 2

class Palindrom(Group):

    def __init__(self):
        super().__init__()
        entry = Entry()
        label = Label().move(0, 30)
        self.set_items([entry, label])

    def ev_entry_change(self, sender):
        ''' Musí být ...._change, a ne changed! :D '''
        text = self.get_items()[0].get_text()
        if text == text[::-1]:
            self.get_items()[1].set_text("Je palindrom")
        else:
            self.get_items()[1].set_text("Není palindrom")

#w2 = Window()
#p2 = Palindrom()
#w2.set_widget(p2)

# 3

class PalindromEntry(Group):

    def __init__(self):
        super().__init__()
        entry1 = Entry()
        entry2 = Entry().move(0, 30)
        self.set_items([entry1, entry2])

    def ev_entry_change(self, sender):
        group_items = self.get_items()

        text = sender.get_text()
        for item in self.get_items():
            if item != sender:
                item.set_text(text[::-1])

#w3 = Window()
#p3 = PalindromEntry()
#w3.set_widget(p3)

# 4

class Counter(Group):

    def __init__(self):
        super().__init__()
        self.value = 0
        label = Label()
        button = Button().move(0, 20).set_text('+')
        self.set_items([label, button])

    def set_value(self, value):
        self.value = value
        return self

    def get_value(self):
        return self.value

    def ev_button_clicked(self, sender):
        self.set_value(self.get_value() + 1)
        self.get_items()[0].set_text(str(self.get_value()))
        # zasíláme nový event a hledáme, kdo tomu rozumí
        # zasílá to tento object celý a ne jenom Button
        # hlavně pro další úkol!
        self.send_event("ev_counter_add")    # každá třída rozumí send_event

#w4 = Window()
#c = Counter()
#w4.set_widget(c)

    
# 5

class CounterGroup(Group):

    def __init__(self):
        super().__init__()
        c1 = Counter()
        c2 = Counter().move(0, 50)
        label = Label().move(0, 100)
        self.set_items([c1, c2, label])

    #def ev_button_clicked(self, sender):
    #    sender_value = sender.get_data()

    #    for item in self.get_items():
    #        if isinstance(item, Counter) and item != sender:
    #            other_c_value = item.get_data()
    #            if sender_value == other_c_value:
    #                text = 'Jsou stejné'
    #            else:
    #                text = 'Jsou stejné'
    #            self.get_items(2).set_text(text)

    def ev_counter_add(self, sender):
        '''
        Tohle je důležitý prvek, že já mohu i odesílat eventy a čekám,
        kdo tomu bude rozumnět. Odesílám to za ten danný objekt.

        '''
        sender_value = sender.get_value()

        for item in self.get_items():
            if isinstance(item, Counter) and item != sender:
                other_c_value = item.get_value()
                if sender_value == other_c_value:
                    text = 'Jsou stejné'
                else:
                    text = 'Nejsou stejné'
                self.get_items()[2].set_text(text)

'''
Funguje to trochu jinak, než je zadané. Mám ty items už definované ve třídě,
ale on je chtěl asi první inicializovat bokem a pak až je přidat. Stačilo by
smazat v init to přidání prvnů a při definování té třídy CounterGroup ještě
přidat set_items(), ale to mi přijde zbytečný a nepěkný :D. 
'''
#w5 = Window()
#c5 = CounterGroup()
#w5.set_widget(c5)

# 6

class Form(Group):

    def __init__(self):
        super().__init__()
        name = Label().set_text('Jméno:')
        name_e = Entry().move(0, 20)
        email = Label().set_text('E-mail:').move(0, 50)
        email_e = Entry().move(0, 70)
        tel = Label().set_text('Tel:').move(0, 100)
        tel_e = Entry().move(0, 120)
        error = Label().move(0, 150)

        self.set_items([name, name_e, email, email_e, tel, tel_e, error])

    def ev_entry_change(self, sender):
        ''' Tohle by mohlo jít vyřeěit asi elegantněji, ale nevím. '''
        for i, item in enumerate(self.get_items()):
            if item == sender:
                label = self.get_items()[i-1].get_text()
                if label == 'Tel:':
                    if not sender.get_text().isdigit():
                        self.get_items()[-1].set_text('Musí obsahovat pouze čísla')
                    else:
                        self.get_items()[-1].set_text('')
                elif label == 'E-mail:':
                    if '@' not in sender.get_text():
                        self.get_items()[-1].set_text('Musí obsahovat @')
                    else:
                        self.get_items()[-1].set_text('')
                else:
                    self.get_items()[-1].set_text('')

w6 = Window()
f = Form()
w6.set_widget(f)

# 7
# - nedělám, protože nemá ukázku a není to tedy možné nijak zkontrolovat
