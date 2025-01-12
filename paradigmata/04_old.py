from omw import *


class EntryField(Group):

    def __init__(self):
        super().__init__()
        self.label = Label()
        self.entry = Entry()
        self.value = None
        self.label_text = None
        self.entry.move(5, 30)
        self.label.move(5, 0)
        self.group = self.set_items([self.label, self.entry])

    def get_label(self):
        return self.label

    def get_entry(self):
        return self.entry

    def set_value(self, text):
        self.value = text
        self.items[1].set_text(self.value)
        return self

    def get_value(self):
        return self.items[1].get_text()

    def set_label_text(self, text):
        self.label_text = text
        self.items[0].set_text(self.label_text)
        return self

    def get_label_text(self):
        return self.items[0].get_text()

class IntegerEntry(Entry):
    def __init__(self):
        super().__init__()
        self.value = None

    def set_value(self):
        value = self.get_text()
        # 5, 6
        # if value.isdigit():
        #    self.value = self.get_text()
        # else:
        #    raise ValueError('the entry value must be an integer')
        # 7
        if self.is_digit(value):
            self.value = self.get_text()
        return self

    def is_decimal(self, value):
        return value.isdigit()

    def get_value(self):
        return self.value

    def entry_change(self):
        super().entry_change()
        self.set_value()
        return self


class IntegerEntryField(EntryField):
    def __init__(self):
        super().__init__()
        self.label_error = Label()
        self.label_error.move(5, 70)
        self.items.append(self.label_error)

    def set_value(self):
        value = self.items[1].get_text()
        if self.is_decimal(value):
            self.value = value
        return self

    def is_decimal(self, value):
        return value.isdigit()

    def get_value(self):
        return self.value

    # nefunguje :(
    # Nejsem si zde jistý, zda to zadané číslo má reagovat hned po zadání, nebo až
    # po ief.set_value()
    def entry_change(self):
        self.items[1].entry_change()
        self.set_value()
        return self
    # 9
    def validate(self):
        actual = self.items[1].get_text()
        self.set_value()
        if self.is_decimal(actual):
            message = 'Valid entry'
        else:
            message = 'Není číslo'
        self.items[2].set_text(message)
        
    
# window = Window()
# ef = EntryField()
# if isinstance(ef, Group):
#     print('yes, it is')

# window.set_widget(ef)
# 3
# ef.set_value('Eliška')
# 4
# ef.set_label_text('Jméééno:')

# 5, 6, 7
#ie = IntegerEntry()
#window.set_widget(ie)

# 8
ief = IntegerEntryField()
ief.set_label_text("Věk:")
w = Window().set_widget(ief)


