from omw import *

# Dědičnost

# 1

#w1 = Window()

class EntryField(Group):
    ''' Group tady má smysl, protože dělám objekt, který má dva prvky. '''
    def __init__(self):
        super().__init__()
        label = Label().set_text('Jméno:').move(10, 20)
        entry = Entry().move(10, 50)
        self.set_items([label, entry])

    

#ef = EntryField()
#w1.set_widget(ef)


# 2

#w2 = Window()

class EntryField2(Group):
    ''' Group tady má smysl, protože dělám objekt, který má dva prvky. '''
    def __init__(self):
        super().__init__()
        self.label = Label().set_text('Jméno:').move(10, 20)
        self.entry = Entry().move(10, 50)
        self.set_items([self.label, self.entry])

    def get_label(self):
        return self.label

    def get_entry(self):
        return self.entry

#ef2 = EntryField2()
#w2.set_widget(ef2)
#ef2.get_label().set_text('Jmééno:')
#ef2.get_entry().set_text('Eliška')

# 3

class EntryField3(Group):
    ''' Group tady má smysl, protože dělám objekt, který má dva prvky. '''
    def __init__(self):
        super().__init__()
        self.label = Label().set_text('Jméno:').move(10, 20)
        self.entry = Entry().move(10, 50)
        self.value = self.entry.get_text()
        self.set_items([self.label, self.entry])

    def get_label(self):
        return self.label

    def get_entry(self):
        return self.entry

    def set_value(self, value):
        self.value = value
        self.entry.set_text(value)
        return self

    def get_value(self):
        return self.entry.get_text()

#w3 = Window()
#ef3 = EntryField3()
#w3.set_widget(ef3)
#ef3.set_value('Nová hodnota')
#print(ef3.get_value())

# 4
class EntryField4(Group):
    ''' Group tady má smysl, protože dělám objekt, který má dva prvky. '''
    def __init__(self):
        super().__init__()
        self.label = Label().set_text('Jméno:').move(10, 20)
        self.entry = Entry().move(10, 50)
        self.value = self.entry.get_text()
        self.label_text = self.label.get_text()
        self.set_items([self.label, self.entry])

    def get_label(self):
        return self.label

    def get_entry(self):
        return self.entry

    def set_value(self, value):
        self.value = value
        self.entry.set_text(value)
        return self

    def get_value(self):
        return self.entry.get_text()

    def set_label_text(self, value):
        self.value = value
        self.label.set_text(value)
        return self

    def get_label_text(self):
        return self.label.get_text()

#w4 = Window()
#ef4 = EntryField4().set_label_text('Nové jmééno:')
#w4.set_widget(ef4)
#print(ef4.get_label_text())

# 5

class IntegerEntry(Entry):
    def __init__(self):
        super().__init__()
        self.value = None

    def set_value(self, value):
        self.value = value
        return self

    def get_value(self):
        return self.value

    def entry_change(self):
        entry = super().entry_change().get_text()
        self.set_value(entry)
        return entry

#w5 = Window()
#ie5 = IntegerEntry()
#w5.set_widget(ie5)

# 6
class IntegerEntry2(Entry):
    def __init__(self):
        super().__init__()
        self.value = None

    def set_value(self, value):
        self.value = value
        return self

    def get_value(self):
        if not self.value.isdigit():
            raise ValueError('Entry is not integer.')
        return self.value

    def entry_change(self):
        entry = super().entry_change().get_text()
        self.set_value(entry)
        return entry

#w6 = Window()
#ie6 = IntegerEntry2()
#w6.set_widget(ie6)

# 7

def is_decimal(value):
    if value.isdigit():
        return True
    else:
        return False

class IntegerEntry3(Entry):
    def __init__(self):
        super().__init__()
        self.value = None

    def set_value(self, value):
        self.value = value
        return self

    def get_value(self):
        if not self.value.isdigit():
            raise ValueError('Entry is not integer.')
        return self.value

    def entry_change(self):
        entry = super().entry_change().get_text()
        self.set_value(entry)
        return entry

    def is_valid(self):
        return is_decimal(self.value)
#w7 = Window()
#ie7 = IntegerEntry3()
#w7.set_widget(ie7)

# 8

class IntegerEntryField(Group):
    
    def __init__(self):
        super().__init__()
        self.label = Label().set_text('Věk:')
        self.entry = Entry().move(0, 30)
        self.validate_label = Label().move(0, 60).set_text('')
        self.label_text = self.label.get_text()
        self.set_items([self.label, self.entry, self.validate_label])

    def get_label(self):
        return self.label

    def get_entry(self):
        return self.entry

    def set_value(self, value):
        self.value = value
        self.entry.set_text(value)
        return self

    def get_value(self):
        return self.entry.get_text()

    def set_label_text(self, value):
        self.value = value
        self.label.set_text(value)
        return self

    def get_label_text(self):
        return self.label.get_text()

#w8 = Window()
#ief8 = IntegerEntryField()
#w8.set_widget(ief8)

# 9

class IntegerEntryField2(Group):
    
    def __init__(self):
        super().__init__()
        self.label = Label().set_text('')
        self.entry = Entry().move(0, 30)
        self.validate_label = Label().move(0, 60).set_text('')
        self.label_text = self.label.get_text()
        self.set_items([self.label, self.entry, self.validate_label])

    def get_label(self):
        return self.label

    def get_entry(self):
        return self.entry

    def set_value(self, value):
        self.value = value
        self.entry.set_text(value)
        return self

    def set_validate_label_text(self, text):
        self.validate_label.set_text(text)
        return self

    def get_value(self):
        return self.entry.get_text()

    def set_label_text(self, value):
        self.value = value
        self.label.set_text(value)
        return self

    def get_label_text(self):
        return self.label.get_text()

    def is_valid(self, value):
        return is_decimal(value)

    def validate(self):
        if self.is_valid(self.entry.entry_change().get_text()):
            self.set_validate_label_text('V pohodě')
        else:
            self.set_validate_label_text('Není číslo.')
w9 = Window()
ief2 = IntegerEntryField2().set_label_text('Věk:')
w9.set_widget(ief2)


# 10 - to je dřívější úkol IntegerEntry, ne? Moc nevím, co chce.

# 11

class Counter(Button):
    def __init__(self):
        super().__init__()
        self.value = 0

    def button_clicked(self):
        self.value += 1
        self.set_text(str(self.value))
w11 = Window()
c = Counter()
w11.set_widget(c)


