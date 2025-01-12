# Functional Micro Widget
#
# MalĂĄ knihovna funkcionĂĄlnĂ­ho uĹživatelskĂŠho rozhranĂ­

import micro_widget as mw

# TĹĂ­da Widget
class Widget:
    def mw_render(self, window, old_widget, mw_widget):
        if self.is_same_type(old_widget):
            if self != old_widget:
                self.mw_update(window, old_widget, mw_widget)
            return mw_widget
        else:
            if old_widget:
                old_widget.mw_destroy(mw_widget)
            return self.mw_create(window)

    def is_same_type(self, value):
        return False

    def __eq__(self, value):
        return self.is_same_type(value)

# TĹĂ­da AtomicWidget
class AtomicWidget(Widget):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def mw_update(self, window, old_widget, mw_widget):          
        if old_widget.get_x() != self.get_x():
            mw.set_widget_x(mw_widget, self.get_x())

        if old_widget.get_y() != self.get_y():
            mw.set_widget_y(mw_widget, self.get_y())

    def mw_destroy(self, mw_widget):
        mw.destroy_widget(mw_widget)

    def __eq__(self, value):
        return (super().__eq__(value)
                and self.get_x() == value.get_x()
                and self.get_y() == value.get_y())

    def action_changed(self, change):
        return self

# TĹĂ­da TextedWidget
class TextedWidget(AtomicWidget):
    def __init__(self, text="", x=0, y=0):
        super().__init__(x, y)
        self.text = text

    def get_text(self):
        return self.text

    def __eq__(self, value):
        return (super().__eq__(value)
                and self.get_text() == value.get_text())

# TĹĂ­da Label
class Label(TextedWidget):
    def __repr__(self):
        text = self.get_text()
        x = self.get_x()
        y = self.get_y()
        return f"label({repr(text)}, {x}, {y})"

    def is_same_type(self, value):
        return isinstance(value, Label)

    def mw_update(self, window, old_widget, mw_widget):
        if old_widget.get_text() != self.get_text():
            mw.set_label_text(mw_widget, self.get_text())
        super().mw_update(window, old_widget, mw_widget)
            
    def mw_create(self, window):
        mw_window = window.get_mw_window()
        mw_widget = mw.make_label(mw_window)
        self.mw_update(window, label(""), mw_widget)
        return mw_widget

    def moved(self, dx, dy):
        text = self.get_text()
        x = self.get_x()
        y = self.get_y()
        return label(text, x + dx, y + dy)

# Prvek label
label = Label

# TĹĂ­da Entry
def entry_change_handler(mw_entry):
    data = mw.get_entry_data(mw_entry)
    window = data[0]
    text = data[1]
    action = data[2]
    new_text = mw.get_entry_text(mw_entry)
    mw.set_entry_text(mw_entry, text)
    if action != None:
        window.process_action([action, new_text])    

class Entry(TextedWidget):
    def __init__(self, text="", action=None, x=0, y=0):
        super().__init__(text, x, y)
        self.action = action

    def get_action(self):
        return self.action   
        
    def __repr__(self):
        text = self.get_text()
        action = self.get_action()
        x = self.get_x()
        y = self.get_y()
        return f"entry({repr(text)}, {repr(action)}, {x}, {y})"

    def is_same_type(self, value):
        return isinstance(value, Entry)

    def mw_set_data(self, window, mw_widget):
        mw.set_entry_data(mw_widget, [window, self.get_text(), self.get_action()])
        return self
          
    def mw_update(self, window, old_widget, mw_widget):
        if (old_widget.get_text() != self.get_text()
            or old_widget.get_action() != self.get_action()):
            self.mw_set_data(window, mw_widget)
            
        if old_widget.get_text() != self.get_text():
            mw.set_entry_text(mw_widget, self.get_text())
   
        super().mw_update(window, old_widget, mw_widget)

    def mw_create(self, window):
        mw_window = window.get_mw_window()
        mw_widget = mw.make_entry(mw_window)
        mw.set_entry_change_handler(mw_widget, entry_change_handler)
        self.mw_set_data(window, mw_widget)
        self.mw_update(window, entry(), mw_widget)
        return mw_widget

    def __eq__(self, value):
        return (super().__eq__(value)
                and self.get_action() == value.get_action())

    def moved(self, dx, dy):
        text = self.get_text()
        action = self.get_action()
        x = self.get_x()
        y = self.get_y()
        return entry(text, action, x + dx, y + dy)

    def action_changed(self, change):
        action = self.get_action()
        if action:
            text = self.get_text()
            x = self.get_x()
            y = self.get_y()
            return entry(text, change(action), x, y)
        else:
            return self

# Prvek entry
entry = Entry

# TĹĂ­da Button
def button_click_handler(mw_button):
    data = mw.get_button_data(mw_button)
    button = data[0]
    window = data[1]
    action = button.get_action()
    if action != None:
        window.process_action(action)
    
class Button(TextedWidget):
    def __init__(self, text="", action=None, x=0, y=0):
        super().__init__(text, x, y)
        self.action = action

    def get_action(self):
        return self.action        
    
    def __repr__(self):
        text = self.get_text()
        action = self.get_action()
        x = self.get_x()
        y = self.get_y()
        return f"button({repr(text)}, {repr(action)}, {x}, {y})"

    def is_same_type(self, value):
        return isinstance(value, Button)

    def mw_set_data(self, window, mw_widget):
        mw.set_button_data(mw_widget, [self, window])
        return self
        
    def mw_update(self, window, old_widget, mw_widget):
        if old_widget.get_action() != self.get_action():
            self.mw_set_data(window, mw_widget)
            
        if old_widget.get_text() != self.get_text():
            mw.set_button_text(mw_widget, self.get_text())
            
        super().mw_update(window, old_widget, mw_widget)
            
    def mw_create(self, window):
        mw_window = window.get_mw_window()
        mw_widget = mw.make_button(mw_window)
        self.mw_update(window, button(""), mw_widget)
        self.mw_set_data(window, mw_widget)
        mw.set_button_click_handler(mw_widget, button_click_handler)
        return mw_widget

    def __eq__(self, value):
        return (super().__eq__(value)
                and self.get_action() == value.get_action())

    def moved(self, dx, dy):
        text = self.get_text()
        action = self.get_action()
        x = self.get_x()
        y = self.get_y()
        return button(text, action, x + dx, y + dy)

    def action_changed(self, change):
        action = self.get_action()
        if action:
            text = self.get_text()
            x = self.get_x()
            y = self.get_y()
            return button(text, change(action), x, y)
        else:
            return self

# Prvek button
button = Button


# TĹĂ­da Group
class Group(Widget):
    def __init__(self, widget1, widget2):
        self.item1 = widget1
        self.item2 = widget2

    def get_item1(self):
        return self.item1

    def get_item2(self):
        return self.item2

    def __repr__(self):
        item1 = self.get_item1()
        item2 = self.get_item2()
        return f"group({item1}, {item2})"

    def is_same_type(self, value):
        return isinstance(value, Group)
        
    def mw_update(self, window, old_widget, mw_widget):
        self.get_item1().mw_render(window, old_widget.get_item1(), mw_widget[0])
        self.get_item2().mw_render(window, old_widget.get_item2(), mw_widget[1])

    def mw_create(self, window):
        mw_widget1 = self.get_item1().mw_render(window, None, None)
        mw_widget2 = self.get_item2().mw_render(window, None, None)
        return [mw_widget1, mw_widget2]

    def mw_destroy(self, mw_widget):
        self.get_item1().mw_destroy(mw_widget[0])
        self.get_item2().mw_destroy(mw_widget[1])

    def __eq__(self, value):
        return (super().__eq__(value)
                and self.get_item1() == value.get_item1()
                and self.get_item2() == value.get_item2())

    def moved(self, dx, dy):
        return group(self.get_item1().moved(dx, dy),
                     self.get_item2().moved(dx, dy))

    def action_changed(self, change):
        return group(self.get_item1().action_changed(change),
                     self.get_item2().action_changed(change)) 

# Prvek group
group = Group


# TĹĂ­da EmptyWidget
class EmptyWidget(Widget):
    def __repr__(self):
        return "empty_widget"

    def mw_update(self, window, old_widget, mw_widget):
        pass

    def mw_create(self, window):
        return None

    def mw_destroy(self, mw_widget):
        pass
    
    def is_same_type(self, value):
        return isinstance(value, EmptyWidget)

    def moved(self, dx, dy):
        return self

# Prvek empty_widget
empty_widget = EmptyWidget()


# Prvek moved
def moved(widget, dx, dy):
    return widget.moved(dx, dy)

# Prvek action_changed
def action_changed(widget, change):
    change1 = change if callable(change) else lambda action: [change, action]
    return widget.action_changed(change1)
    

# TĹĂ­da Window
class Window:
    def __init__(self, content, init_state=None, next_state=None, process_effect=None, trace=False):
        self.content_function = (content
                                 if callable(content)
                                 else lambda state: content)
        self.trace = trace
        self.process_effect = process_effect if process_effect else lambda effect: None
        self.next_state = next_state if next_state else lambda state, action: action
        self.widget = None
        self.mw_widget = None
        self.mw_window = mw.display_window()
        self.ignore_actions = True
        self.set_state(init_state)
        self.ignore_actions = False

    def get_mw_window(self):
        return self.mw_window
        
    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        self.mw_render()
        return self

    def mw_render(self):
        widget = self.content_function(self.state)
        if self.trace:
            print("State:", repr(self.state))
            print("Content:", repr(widget))
        mw_widget = widget.mw_render(self, self.widget, self.mw_widget)
        self.widget = widget
        self.mw_widget = mw_widget
        
    def process_action(self, action):
        process_effect = False
        effect = None
        if not self.ignore_actions: 
            self.ignore_actions = True
            if action == None:
                new_state = self.get_state()
            else:
                state = self.get_state()
                if self.trace:
                    print("Old state:", repr(state))
                    print("Action:", repr(action))
                result = self.next_state(state, action)
                if isinstance(result, StateWithEffect):
                    new_state = result.get_state()
                    effect = result.get_effect()
                    process_effect = True
                else:
                    new_state = result
            self.set_state(new_state)
            self.ignore_actions = False
        if process_effect:
            if self.trace:
                print("Effect:", repr(effect))
            self.process_effect(effect)
        return self

    def main_loop(self):
        mw.main_loop(self.get_mw_window())
        return self

class StateWithEffect:
    def __init__(self, state, effect):
        self.state = state
        self.effect = effect

    def get_state(self):
        return self.state

    def get_effect(self):
        return self.effect

    def __repr__(self):
        state = self.get_state()
        effect = self.get_effect()
        return f"with_effect({repr(state)}, {repr(effect)})"

def with_effect(state, effect):
    return StateWithEffect(state, effect)
    
# Procedury na zobrazenĂ­ okna
def display_window(content, init_state=None, next_state=None, process_effect=None, trace=False):
    window = Window(content, init_state, next_state, process_effect, trace)
    def emit_action(action):
        window.process_action(action)
    return emit_action 

"""
def display_window_and_loop(content, init_state=None, update=None, trace=False):
    Window(content, init_state, update, trace).main_loop()
"""
