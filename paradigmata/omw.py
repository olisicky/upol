# Knihovna Object Micro Widget
import micro_widget as mw

class OMWObject:
    def __init__(self):
        self.delegate = None
    
    def get_delegate(self):
        return self.delegate

    def set_delegate(self, delegate):
        self.delegate = delegate
        return self

    def propagate_event(self, sender, event, event_args):
        if hasattr(self, event):
            handler = getattr(self, event)
            handler(sender, *event_args)
        delegate = self.get_delegate()
        if delegate:
            delegate.propagate_event(sender, event, event_args)
        return self
    
    def send_event(self, event, *event_args):
        self.propagate_event(self, event, event_args)
        return self

        
class MWValue:
    def __init__(self):
        super().__init__()
        self.mw_value = None

    def get_mw_value(self):
        return self.mw_value

    def set_mw_value(self, mw_value):
        self.mw_value = mw_value
        return self

    def destroy_mw_value(self):
        raise NotImplementedError("Method has to be rewritten.")
        
    def delete_mw_value(self):
        self.destroy_mw_value()
        self.set_mw_value(None)
        return self

    def make_mw_value(self, root):
        raise NotImplementedError("Method has to be rewritten.")

    def create_mw_value(self):
        self.set_mw_value(self.make_mw_value(self.get_mw_window()))
        return self


class Widget(OMWObject):
    def __init__(self):
        super().__init__()
        self.mw_window = None

    def get_mw_window(self):
        return self.mw_window

    def set_mw_window(self, mw_window):
        self.mw_window = mw_window
        return self

    def create_mw_values(self, mw_window):
        self.set_mw_window(mw_window)
        self.create_mw_value()
        return self

    def destroy_mw_values(self):
        self.destroy_mw_value()
        self.set_mw_window(None)
        return self

    def is_mw_displayed(self):
        return self.get_mw_window() != None
        
class AtomicWidget(MWValue, Widget):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x
        if self.is_mw_displayed():
            self.mw_update_position()
        return self

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y
        if self.is_mw_displayed():
            self.mw_update_position()
        return self

    def mw_set_position(self, x, y):
        raise NotImplementedError("Method has to be rewritten.")

    def mw_update_position(self):
        return self.mw_set_position(self.get_x(), self.get_y())
        
    def move(self, dx, dy):
        self.set_x(self.get_x() + dx)
        self.set_y(self.get_y() + dy)
        return self

    def create_mw_value(self):
        super().create_mw_value()
        self.mw_update_position()
        return self

    def destroy_mw_value(self):
        raise NotImplementedError("Method has to be rewritten.")
        
    
    
class Window(MWValue, OMWObject):
    def __init__(self):
        super().__init__()
        self.widget = None
        self.create_mw_value()

    # micro widget
    def get_mw_window(self):
        return self.get_mw_value()
    
    def make_mw_value(self, root):
        return mw.display_window()
    
    # vlastnost widget
    
    def get_widget(self):
        return self.widget

    def set_widget(self, widget):     
        old_widget = self.get_widget()
        if old_widget:
            old_widget.destroy_mw_values()
            old_widget.set_delegate(None)

        self.widget = widget
        
        if widget:
            widget.set_delegate(self)
            widget.create_mw_values(self.get_mw_value())
        return self

    def main_loop(self):
        mw.main_loop(self.get_mw_value())
        return self

    def update(self):
        mw.update_window(self.get_mw_value())
        return self

    def is_opened(self):
        return mw.is_window_opened(self.get_mw_value())

    def destroy(self):
        mw.destroy_window(self.get_mw_value())
        return self

class TextedWidget(AtomicWidget):
    def __init__(self):
        super().__init__()
        self.text = ""

    # micro widget
    def mw_set_text(self, text):
        raise NotImplementedError("Method has to be rewritten.")
    
    def mw_update_text(self):
        self.mw_set_text(self.get_text())
        return self
        
    def create_mw_value(self):
        super().create_mw_value()
        self.mw_update_text()
        return self

    # vlastnosti
    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text
        if self.is_mw_displayed():
            self.mw_update_text()
        return self


class Label(TextedWidget):
    # micro widget
    def make_mw_value(self, mw_window):
        return mw.make_label(mw_window)

    def mw_set_text(self, text):
        mw_label = self.get_mw_value()
        mw.set_label_text(mw_label, text)
        return self

    def mw_set_position(self, x, y):
        mw_label = self.get_mw_value()
        mw.set_label_x(mw_label, x)
        mw.set_label_y(mw_label, y)
        return self

    def destroy_mw_value(self):
        mw.destroy_label(self.get_mw_value())
        return self

def mw_button_click_handler(mw_button):
    button = mw.get_button_data(mw_button)
    button.button_clicked()
    
class Button(TextedWidget):
    # micro widget
    def make_mw_value(self, window):
        return mw.make_button(window)

    def mw_set_text(self, text):
        mw_value = self.get_mw_value()
        mw.set_button_text(mw_value, text)
        
    def create_mw_value(self):
        super().create_mw_value()
        mw_button = self.get_mw_value()
        mw.set_button_data(mw_button, self)
        mw.set_button_click_handler(mw_button, mw_button_click_handler)
        return self

    def mw_set_position(self, x, y):
        mw_button = self.get_mw_value()
        mw.set_button_x(mw_button, x)
        mw.set_button_y(mw_button, y)
        return self

    def destroy_mw_value(self):
        mw.destroy_button(self.get_mw_value())
        return self

    # udĂĄlosti
    def button_clicked(self):
        self.send_event("ev_button_clicked")
        return self

def mw_entry_change_handler(mw_entry):
    entry = mw.get_entry_data(mw_entry)
    entry.set_text(mw.get_entry_text(mw_entry))
    
class Entry(TextedWidget):
    # micro widget
    def make_mw_value(self, mw_window):
        return mw.make_entry(mw_window)
    
    def create_mw_value(self):
        super().create_mw_value()
        mw_entry = self.get_mw_value()
        mw.set_entry_data(mw_entry, self)
        mw.set_entry_change_handler(mw_entry, mw_entry_change_handler)
        return self

    def mw_set_position(self, x, y):
        mw_entry = self.get_mw_value()
        mw.set_entry_x(mw_entry, x)
        mw.set_entry_y(mw_entry, y)
        return self

    def destroy_mw_value(self):
        mw.destroy_entry(self.get_mw_value())
        return self

    def mw_set_text(self, text):
        mw_entry = self.get_mw_value()
        mw.set_entry_text(mw_entry, text)
        return self

    # vlastnost text
    def set_text(self, text):
        if text != self.get_text():
            super().set_text(text)
            self.entry_change()
        return self

    # zmÄna
    def entry_change(self):
        self.send_event("ev_entry_change")
        return self
        

class Group(Widget):
    def __init__(self):
        super().__init__()
        self.items = []

    def get_items(self):
        return self.items[:]

    def check_item(self, item):
        if not isinstance(item, Widget):
            raise TypeError("Items have to be widgets.")
    
    def check_items(self, items):
        for item in items:
            self.check_item(item)
        return self

    def set_items(self, items):
        self.check_items(items)
        self.set_items_delegate(None)
        self.items = items[:]
        self.set_items_delegate(self)
        return self

    def is_mw_displayed(self):
        return self.get_mw_window() != None
        
    def set_items_delegate(self, delegate):
        for item in self.get_items():
            item.set_delegate(delegate)
        return self

    def create_mw_value(self):
        return self

    def destroy_mw_value(self):
        return self
    
    def move(self, dx, dy):
        for item in self.get_items():
            item.move(dx, dy)
        return self

    def do_set_items(self, items):
        if self.is_mw_displayed():
            self.destroy_items_mw_values()
        super().do_set_items(items)
        if self.is_mw_displayed():
            self.create_items_mw_values(self.get_mw_window())
        return self

    # micro widget
    def create_mw_values(self, mw_window):
        super().create_mw_values(mw_window)
        self.create_items_mw_values(mw_window)
        return self

    def create_items_mw_values(self, mw_window):
        for item in self.get_items():
            item.create_mw_values(mw_window)
        return self
    
    def destroy_mw_values(self):
        super().destroy_mw_values()
        self.destroy_items_mw_values()
        return self

    def destroy_items_mw_values(self):
        for item in self.get_items():
            item.destroy_mw_values()
        return self

"""
class EventTrace:
    def ev_entry_change(self, sender):
        print("ev_entry_change", self, sender)

    def ev_button_clicked(self, sender):
        print("ev_button_clicked", self, sender)
        
class MyWindow(Window, EventTrace):
    pass
        
class MyGroup(Group, EventTrace):
    pass

class MyEntry(Entry, EventTrace):
    pass

class MyButton(Button, EventTrace):
    pass
            
window = MyWindow()
label = Label().set_text("Rostlina").set_x(10).set_y(10)
entry = MyEntry().set_text("Pavla").set_x(10).set_y(30)
group = MyGroup().set_items([label, entry])
button = MyButton().set_text("Klikni na mÄ!").move(10, 50)
group2 = MyGroup().set_items([group, button])
window.set_widget(group2)
"""

