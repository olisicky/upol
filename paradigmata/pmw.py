# Prototyp Micro Widget

from proto import obj
import micro_widget as mw


# prototyp pmw_object
pmw_object = obj.clone()
pmw_object.add_slot("delegate")

def pmw_object_send_event(resend, self, event, *args):
    delegate = self
    while delegate:
        if delegate:
            if delegate.understand(event):
                delegate.send(event, self, *args)
        delegate = delegate.delegate()

pmw_object.set_slot("send_event", pmw_object_send_event)

# prototyp window
window = pmw_object.clone()
window.set_name("window")
window.add_slot("widget")
window.add_slot("mw_window")

def window_create_mw(resend, self):
    widget = self.widget()
    if self.is_displayed() and widget != None:
        widget.create_mw(self.mw_window())
    return self

window.set_slot("create_mw", window_create_mw)

def window_display(resend, self):
    mw_window = mw.display_window()
    self.set_mw_window(mw_window)
    self.create_mw()
    return self

window.set_slot("display", window_display)

def window_redisplay(resend, self):
    self.destroy_mw()
    self.create_mw()
    return self

window.set_slot("redisplay", window_redisplay)

def window_is_displayed(resend, self):
    return self.mw_window() != None

window.set_slot("is_displayed", window_is_displayed)

def window_clone(resend, self):
    clone = resend()
    clone.set_mw_window(None)
    widget = self.widget()
    if widget != None:
        clone.set_widget(widget.clone())
    return clone

window.set_slot("clone", window_clone)

def window_destroy_mw(resend, self):
    if self.is_displayed() and self.widget():
        self.widget().destroy_mw()    
    return self

window.set_slot("destroy_mw", window_destroy_mw)


def window_set_widget(resend, self, widget):
    self.destroy_mw()
    self.set_slot("widget", widget)
    if widget:
        widget.set_delegate(self)
    self.create_mw()
    return self

window.set_slot("set_widget", window_set_widget)

def window_main_loop(resend, self):
    mw.main_loop(self.mw_window())
    return self

window.set_slot("main_loop", window_main_loop)

# prototyp widget
widget = pmw_object.clone()
widget.set_name("widget")

# prototyp atomic_widget
atomic_widget = widget.clone()
atomic_widget.set_name("atomic_widget")
atomic_widget.add_slot("x")
atomic_widget.add_slot("y")
atomic_widget.add_slot("mw_widget")
atomic_widget.set_x(0)
atomic_widget.set_y(0)

def atomic_widget_move(resend, self, dx, dy):
    self.set_x(self.x() + dx)
    self.set_y(self.y() + dy)
    return self
    
atomic_widget.set_slot("move", atomic_widget_move)

def atomic_widget_destroy_mw(resend, self):
    mw.destroy_widget(self.mw_widget())
    self.set_mw_widget(None)
    return self

atomic_widget.set_slot("destroy_mw", atomic_widget_destroy_mw)

def atomic_widget_update(resend, self):
    mw_widget = self.mw_widget()
    if mw_widget:
        mw.set_widget_x(mw_widget, self.x())
        mw.set_widget_y(mw_widget, self.y())    
    return self

atomic_widget.set_slot("update", atomic_widget_update)

def atomic_widget_set_x(resend, self, x):
    self.set_slot("x", x)
    self.update()
    return self

atomic_widget.set_slot("set_x", atomic_widget_set_x)

def atomic_widget_set_y(resend, self, y):
    self.set_slot("y", y)
    self.update()
    return self

atomic_widget.set_slot("set_y", atomic_widget_set_y)

# prototyp texted_widget
texted_widget = atomic_widget.clone()
texted_widget.set_name("texted_widget")
texted_widget.add_slot("text")
texted_widget.set_text("")

def texted_widget_set_text(resend, self, text):
    self.set_slot("text", text)
    self.update()
    return self

texted_widget.set_slot("set_text", texted_widget_set_text)
    

# prototyp label
label = texted_widget.clone()
label.set_name("label")

def label_create_mw(resend, self, mw_window):
    mw_label = mw.make_label(mw_window)
    self.set_mw_widget(mw_label)
    self.update()
    return self

label.set_slot("create_mw", label_create_mw)

    
def label_update(resend, self):
    resend()
    mw_label = self.mw_widget()
    if mw_label:
        if mw.get_label_text(mw_label) != self.text():
            mw.set_label_text(mw_label, self.text())
    return self
    
label.set_slot("update", label_update)

# prototyp button
button = texted_widget.clone()
button.set_name("button")

def button_click_handler(mw_button):
    button = mw.get_button_data(mw_button)
    button.send_event("ev_button_clicked")
    
def button_create_mw(resend, self, mw_window):
    mw_button = mw.make_button(mw_window)
    self.set_mw_widget(mw_button)
    self.update()
    mw.set_button_data(mw_button, self)
    mw.set_button_click_handler(mw_button, button_click_handler)
    return self

button.set_slot("create_mw", button_create_mw)

    
def button_update(resend, self):
    resend()
    mw_label = self.mw_widget()
    if mw_label:
        mw.set_button_text(mw_label, self.text())
    return self
    
button.set_slot("update", button_update)

# prototyp entry
entry = texted_widget.clone()
entry.set_name("entry")

def entry_change_handler(mw_entry):
    entry = mw.get_entry_data(mw_entry)
    entry.set_text(mw.get_entry_text(mw_entry))
    entry.send_event("ev_entry_text_change")
    
def entry_create_mw(resend, self, mw_window):
    mw_entry = mw.make_entry(mw_window)
    mw.set_entry_data(mw_entry, self)
    mw.set_entry_change_handler(mw_entry, entry_change_handler)
    self.set_mw_widget(mw_entry)
    self.update()
    return self

entry.set_slot("create_mw", entry_create_mw)

    
def entry_update(resend, self):
    resend()
    mw_entry = self.mw_widget()
    if mw_entry:
        if mw.get_entry_text(mw_entry) != self.text():
            mw.set_entry_text(mw_entry, self.text())
    return self
    
entry.set_slot("update", entry_update)


# prototyp group
group = widget.clone()
group.set_name("group")
group.add_slot("items")
group.set_items([])


def group_clone(resend, self):
    clone = resend()
    # Klon skupiny nenĂ­ v oknÄ:
    clone.set_delegate(None)
    clone.set_mw_window(None)
    cloned_items = []
    for item in self.items():
        cloned_items += [item.clone()]
    #clone.set_slot("items", []) # ZamezĂ­ odstranÄnĂ­ pĹŻvodnĂ­ch prvkĹŻ


    clone.set_items(cloned_items)
    return clone

group.set_slot("clone", group_clone)


def group_move(resend, self, dx, dy):
    for item in self.items():
        item.move(dx, dy)
    return self

group.set_slot("move", group_move)

group.add_slot("mw_window")

def group_create_mw(resend, self, mw_window):
    self.create_mw_items(mw_window)
    self.set_mw_window(mw_window)
    return self

group.set_slot("create_mw", group_create_mw)

def group_create_mw_items(resend, self, mw_window):
    for item in self.items():
        item.create_mw(mw_window)
    return self

group.set_slot("create_mw_items", group_create_mw_items)

def group_destroy_mw(resend, self):
    self.destroy_mw_items()
    self.set_mw_window(None)
    return self

group.set_slot("destroy_mw", group_destroy_mw)

def group_destroy_mw_items(resend, self):
    for item in self.items():
        item.destroy_mw()
    return self

group.set_slot("destroy_mw_items", group_destroy_mw_items)

def group_set_items(resend, self, items):
    if self.mw_window():
        self.destroy_mw_items()
    self.set_slot("items", items)
    for item in items:
        item.set_delegate(self)
    if self.mw_window():
        self.create_mw_items(self.mw_window())
    return self

group.set_slot("set_items", group_set_items)

def group_update(resend, self):
    for item in self.items():
        item.update()
    return self

group.set_slot("update", group_update)

"""
w = window.clone()
b = button.clone()
w.set_widget(b)
w.display()
"""