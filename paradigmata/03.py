from omw import Label, Group

# 1

class Window:

    def __init__(self):
        self.widget = None

    def set_widget(self, widget):
        if isinstance(widget, Label) or isinstance(widget, Group):
            self.widget = widget
        else:
            raise TypeError('Widget should be of type Label or Group')
        return self

    def get_widget(self):
        return self.widget

w1 = Window()
l1 = Label()
l1.set_text('A')
l11 = Label()
l11.set_text('B')
g1 = Group()
g1.set_items([l1, l11])
w1.set_widget(g1)

# 2

class RadioButton:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = False

    def set_x(self, x):
        if type(x) != int:
            raise TypeError("X should be integer.")
        else:
            self.x = x
        return self

    def set_y(self, y):
        if type(y) != int:
            raise TypeError("Y should be integer.")
        else:
            self.y = y
        return self

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_state(self, state):
        if not isinstance(state, bool):
            raise TypeError("State should be of type bool")
        else:
            self.state = state
        return self

    def get_state(self):
        return self.state

    def move(self, dx, dy):
        if type(dy) != int or type(dx) != int:
            raise TypeError("X and Y should be of type int")

        else:
            self.set_x(self.get_x() + dx)
            self.set_y(self.get_y() + dy)
        return self

    def is_selected(self):
        return self.get_state()

    def toogle(self):
        self.set_state(not self.get_state())
        return self

rb = RadioButton()
rb.get_state()
rb.toogle().get_state()
rb.move(20, 30)
print(rb.get_x(), rb.get_y())


# 3

class RadioButtonGroup:

    def __init__(self):
        self.items = []

    def set_items(self, items):
        for item in items:
            if not isinstance(item, RadioButton):
                raise TypeError("All items should be of type RadioButton")
            else:
                self.items.append(item)
        return self

    def get_items(self):
        return self.items

    def move(self, dx, dy):
        for item in self.get_items():
            item.move(dx, dy)
        return self

rbg = RadioButtonGroup()
rbg.set_items([RadioButton(), RadioButton().move(0, 20)])
rbg.get_items()

# 4

class RadioButtonGroup4:

    def __init__(self):
        self.items = []
        self.selected = None
        self.x = 0
        self.y = 0

    def set_items(self, items):
        for item in items:
            if not isinstance(item, RadioButton):
                raise TypeError("All items should be of type RadioButton")
            else:
                self.items.append(item)
        self.deselect_all()   # 4b
        return self

    def get_items(self):
        return self.items

    def move(self, dx, dy):
        for item in self.get_items():
            item.move(dx, dy)
        return self

    def set_selected(self, rb):
        if self.selected:
            self.get_selected().set_state(False)

        self.selected = rb
        if rb:
            rb.set_state(True)
        return self

    def get_selected(self):
        return self.selected

    def deselect_all(self):
        for item in self.get_items():
            item.set_state(False)
        return self

    def set_x(self, x):
        if type(x) != int:
            raise TypeError("X should be integer.")
        else:
            self.x = x
        return self

    def set_y(self, y):
        if type(y) != int:
            raise TypeError("Y should be integer.")
        else:
            self.y = y
        return self

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

r1 = RadioButton()
r2 = RadioButton()
rbg4 = RadioButtonGroup4().set_items([r1, r2])
print(r1.is_selected(), r2.is_selected())
rbg4.get_selected()
rbg4.set_selected(r1)
rbg4.set_selected(r2)
rbg4.set_selected(None)

    
