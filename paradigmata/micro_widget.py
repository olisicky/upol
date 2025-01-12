# Knihovna Micro Widget

import tkinter as tk
from tkinter import ttk

# Kontroly typĹŻ
def string_type_check(value):
    if type(value) != str:
        raise TypeError(f"String expected, got {repr(value)}.")

def integer_type_check(value):
    if type(value) != int:
        raise TypeError(f"Integer expected, got {repr(value)}.")
    
# Micro widget value
MW_VALUE_TYPE_INDEX = 0
MW_VALUE_TK_OBJECT_INDEX = 1

def make_mw_value(widget_type, tk_object, *args):
    return [widget_type, tk_object, *args]

def get_value_tk_object(value):
    return value[MW_VALUE_TK_OBJECT_INDEX]

def get_mw_value_type(widget):
    return widget[MW_VALUE_TYPE_INDEX]

def is_mw_value(v):
    return type(v) == list and len(v) >= 2

def destroy_mw_value(value):
    tk_object = get_value_tk_object(value)
    tk_object.destroy()

    
# Window
_tk = None
TYPE_WINDOW = "window"
WINDOW_OPENED_INDEX = 2
        
def display_window():
    global _tk
    if _tk:
        top = tk.Toplevel()
        def destroy_callback(event):
            if event.widget == event.widget.winfo_toplevel():
                window[WINDOW_OPENED_INDEX] = False
    else:
        _tk = tk.Tk()
        top = _tk
        def destroy_callback(event):
            global _tk
            if event.widget == event.widget.winfo_toplevel():
                _tk = None
                window[WINDOW_OPENED_INDEX] = False
    top.bind("<Destroy>", destroy_callback)
    top.title("micro_widget window")
    top.geometry("297x210")
    window = make_mw_value(TYPE_WINDOW, top, True)
    return window

def destroy_window(window):
    destroy_mw_value(window)
    
def is_window(value):
    return is_mw_value(value) and get_mw_value_type(value) == TYPE_WINDOW

def window_type_check(value):
    if not is_window(value):
        raise TypeError(f"Window expected, got {repr(value)}.")

def update_window(window):
    tk_window = get_value_tk_object(window)
    tk_window.update_idletasks()
    tk_window.update()

def is_window_opened(window):
    tk_window = get_value_tk_object(window)
    return  window[WINDOW_OPENED_INDEX]
    
    
def main_loop(window):
    tk_window = get_value_tk_object(window)
    tk_window.mainloop()
    
# Widget
WIDGET_WINDOW_INDEX = 2
WIDGET_X_INDEX = 3
WIDGET_Y_INDEX = 4

def make_widget(widget_type, tk_object, window, *args):
    widget = make_mw_value(widget_type, tk_object, window, 0, 0, *args)
    tk_update_position(widget)
    return widget

def destroy_widget(widget):
    destroy_mw_value(widget)

def get_widget_window(widget):
    return widget[WIDGET_WINDOW_INDEX]

def get_widget_x(widget):
    return widget[WIDGET_X_INDEX]

def get_widget_y(widget):
    return widget[WIDGET_Y_INDEX]

def set_widget_x(widget, x):
    integer_type_check(x)
    if x != widget[WIDGET_X_INDEX]:
        widget[WIDGET_X_INDEX] = x
        tk_update_position(widget)

def set_widget_y(widget, y):
    integer_type_check(y)
    if y != WIDGET_Y_INDEX:
        widget[WIDGET_Y_INDEX] = y
        tk_update_position(widget)

def tk_update_position(widget):
    x = get_widget_x(widget)
    y = get_widget_y(widget)
    get_value_tk_object(widget).place(x=x, y=y)
    
# Label
TYPE_LABEL = "label"
LABEL_TEXT_INDEX = 5
def make_label(window):
    window_type_check(window)
    tk_obj = ttk.Label(get_value_tk_object(window))
    return make_widget(TYPE_LABEL, tk_obj, window, "")

def is_label(value):
    return is_mw_value(value) and get_mw_value_type(value) == TYPE_LABEL

def label_type_check(value):
    if not is_label(value):
        raise TypeError(f"Label expected, got {repr(value)}.")
    
def destroy_label(label):
    label_type_check(label)
    destroy_widget(label)

def get_label_window(label):
    label_type_check(label)
    return get_widget_window(label)

def get_label_x(label):
    label_type_check(label)
    return get_widget_x(label)

def get_label_y(label):
    label_type_check(label)
    return get_widget_y(label)

def set_label_x(label, x):
    label_type_check(label)
    set_widget_x(label, x)

def set_label_y(label, y):
    label_type_check(label)
    set_widget_y(label, y)

def get_label_text(label):
    label_type_check(label)
    return label[LABEL_TEXT_INDEX]

def set_label_text(label, text):
    label_type_check(label)
    string_type_check(text)
    if label[LABEL_TEXT_INDEX] != text:
        label[LABEL_TEXT_INDEX] = text
        get_value_tk_object(label)["text"] = text



# Button
TYPE_BUTTON = "button"
BUTTON_TEXT_INDEX = 5
BUTTON_DATA_INDEX = 6
BUTTON_CLICK_HANDLER_INDEX = 7

def empty_handler(data):
    pass

def make_button(window):
    def command():
        button[BUTTON_CLICK_HANDLER_INDEX](button)        
    tk_obj = ttk.Button(get_value_tk_object(window))
    tk_obj["command"] = command
    button = make_widget(TYPE_BUTTON, tk_obj, window, "", None, empty_handler)
    return button

def is_button(value):
    return is_mw_value(value) and get_mw_value_type(value) == TYPE_BUTTON

def button_type_check(value):
    if not is_button(value):
        raise TypeError(f"Button expected, got {repr(value)}.")

def destroy_button(button):
    button_type_check(button)
    destroy_widget(button)

def get_button_window(button):
    button_type_check(button)
    return get_widget_window(button)

def get_button_x(button):
    button_type_check(button)
    return get_widget_x(button)

def get_button_y(button):
    button_type_check(button)
    return get_widget_y(button)

def set_button_x(button, x):
    button_type_check(button)
    set_widget_x(button, x)

def set_button_y(button, y):
    button_type_check(button)
    set_widget_y(button, y)
    
def set_button_text(button, text):
    button_type_check(button)
    string_type_check(text)
    button[BUTTON_TEXT_INDEX] = text
    get_value_tk_object(button)["text"] = text

def get_button_text(button):
    button_type_check(button)
    return button[BUTTON_TEXT_INDEX]

def set_button_data(button, data):
    button_type_check(button)
    button[BUTTON_DATA_INDEX] = data

def get_button_data(button):
    return button[BUTTON_DATA_INDEX]

def set_button_click_handler(button, click_handler):
    button_type_check(button)
    button[BUTTON_CLICK_HANDLER_INDEX] = click_handler

def get_button_click_handler(button):
    button_type_check(button)
    return button[BUTTON_CLICK_HANDLER_INDEX]
    
# Entry
TYPE_ENTRY = "entry"
ENTRY_TEXT_INDEX = 5
ENTRY_VAR_INDEX = 6
ENTRY_DATA_INDEX = 7
ENTRY_CHANGE_HANDLER_INDEX = 8

def make_entry(window):
    var = tk.StringVar()
    tk_obj = ttk.Entry(get_value_tk_object(window))
    entry = make_widget(TYPE_ENTRY, tk_obj, window, "", var, None, empty_handler)
    tk_obj["textvariable"] = var
    def var_write_command(*args):
        entry[ENTRY_TEXT_INDEX] = var.get()
        entry[ENTRY_CHANGE_HANDLER_INDEX](entry)
    var.trace_add("write", var_write_command)
    return entry
    
def is_entry(value):
    return is_mw_value(value) and get_mw_value_type(value) == TYPE_ENTRY

def entry_type_check(value):
    if not is_entry(value):
        raise TypeError(f"Entry expected, got {repr(value)}.")
    
def destroy_entry(entry):
    entry_type_check(entry)
    destroy_widget(entry)

def get_entry_window(entry):
    entry_type_check(entry)
    return get_widget_window(entry)

def get_entry_x(entry):
    entry_type_check(entry)
    return get_widget_x(entry)

def get_entry_y(entry):
    entry_type_check(entry)
    return get_widget_y(entry)

def set_entry_x(entry, x):
    entry_type_check(entry)
    set_widget_x(entry, x)

def set_entry_y(entry, y):
    entry_type_check(entry)
    set_widget_y(entry, y)
    
def get_entry_text(entry):
    return entry[ENTRY_TEXT_INDEX]

def set_entry_text(entry, text):
    entry_type_check(entry)
    string_type_check(text)
    if text != entry[ENTRY_TEXT_INDEX]:
        entry[ENTRY_TEXT_INDEX] = text
        entry[ENTRY_VAR_INDEX].set(text)

def set_entry_data(entry, data):
    entry_type_check(entry)
    entry[ENTRY_DATA_INDEX] = data

def get_entry_data(entry):
    entry_type_check(entry)
    return entry[ENTRY_DATA_INDEX]

def set_entry_change_handler(entry, change_handler):
    entry_type_check(entry)
    entry[ENTRY_CHANGE_HANDLER_INDEX] = change_handler

def get_entry_change_handler(entry):
    entry_type_check(entry)
    return entry[ENTRY_CHANGE_HANDLER_INDEX]

# TestovacĂ­ kĂłd:
""" 
w = display_window()
l = make_label(w)
set_label_text(l, "JmĂŠno:")
set_widget_x(l, 10)
set_widget_y(l, 10)
e = make_entry(w)
set_widget_x(e, 10)
set_widget_y(e, 30)
set_entry_text(e, "Josef")

def print_entry_text_handler(entry):
    print("Entry change:", get_entry_text(entry))
    
set_entry_change_handler(e, print_entry_text_handler)
b = make_button(w)
set_button_text(b, "OK")

def button_handler(button):
    print("Button pressed")
    
set_button_click_handler(b, button_handler)
set_widget_x(b, 10)
set_widget_y(b, 60)
"""
