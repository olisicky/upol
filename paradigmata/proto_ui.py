# Knihovna na zobrazovĂĄnĂ­ objektĹŻ v prototypovĂŠm programovĂĄnĂ­
import proto
import tkinter

FONT_SIZE = 16
FONT_WIDTH = 11
ROW_SIZE = None
TEXT_PADDING_X = 8
TEXT_PADDING_Y = 3
FONT = ('Courier', FONT_SIZE)

def canvas_create_text(canvas, text):
    return canvas.create_text(
        0,
        0,
        font=FONT,
        anchor="nw",
        fill="black",
        text=text)

def canvas_create_rect(canvas, width=0, height=0):
    return canvas.create_rectangle(
        0,
        0,
        width,
        height,
        fill="white",
        outline="black")
    
def canvas_rect_update_width(canvas, rect, width):
    x1, y1, x2, y2 = canvas.coords(rect)
    canvas.coords(rect, x1, y1, x1 + width, y2)

def canvas_get_text_width(canvas, text):
    bbox = canvas.bbox(text)
    return (bbox[2] - bbox[0]) + 2 * TEXT_PADDING_X

class CanvasObject:
    def __init__(self, canvas):
        self.canvas = canvas


class RectObject(CanvasObject):
    def __init__(self, canvas, x=0, y=0, width=0, height=0):
        super().__init__(canvas)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def is_position_inside(self, x, y):
        return (x >= self.x
                and y >= self.y
                and x <= self.x + self.width
                and y <= self.y + self.height)
        
    def is_outside_canvas(self):
        height = self.canvas.winfo_height()
        width = self.canvas.winfo_width()
        return (self.x > width
                or self.y > height
                or self.x + self.width < 0
                or self.y + self.height < 0)

    def move_to(self, x, y):
        self.x = x
        self.y = y
        self.update_position()

    def update_position(self):
        pass

    
class Table(RectObject):
    def __init__(self, value, canvas, x, y):
        super().__init__(canvas, x, y)
        self.value = value
        
    def update_width(self):
        pass

    def find_value_id(self, x, y):
        return None


class AtomTable(Table):
    def __init__(self, value, canvas, x, y):
        super().__init__(value, canvas, x, y)
        self.atom_repr = repr(value)
        self.repr_width = len(self.atom_repr) * FONT_WIDTH
        self.width = self.repr_width + 2 * TEXT_PADDING_X
        self.height = ROW_SIZE
        self.display()
            
    def display(self):
        self.rect = canvas_create_rect(self.canvas, ROW_SIZE, ROW_SIZE)
        self.text = canvas_create_text(self.canvas, self.atom_repr)
        self.canvas.update_idletasks()
        self.update_width()
        self.update_position()

    def update_position(self):
        self.canvas.moveto(self.rect, self.x, self.y)
        self.canvas.moveto(self.text, self.x + TEXT_PADDING_X, self.y + TEXT_PADDING_Y)

    def update_width(self):
        self.width = canvas_get_text_width(self.canvas, self.text)
        canvas_rect_update_width(self.canvas, self.rect, self.width)

    def remove(self):
        self.canvas.delete(self.rect)
        self.canvas.delete(self.text)


class ValueRect(RectObject):
    def __init__(self, canvas, item, value_id):
        super().__init__(canvas, 0, 0, ROW_SIZE, ROW_SIZE)
        self.item = item
        self.value_id = value_id
        self.rect = None
        self.display()
        
    def display(self):
        self.rect = canvas_create_rect(self.canvas, ROW_SIZE, ROW_SIZE)

    def update_position(self):
        self.canvas.moveto(self.rect, self.x, self.y)

    def link_start(self):
        x = self.x + ROW_SIZE / 2
        y = self.y + ROW_SIZE / 2
        return x, y

    def get_value(self):
        return self.item

    def get_value_id(self):
        return self.value_id

    def remove(self):
        self.canvas.delete(self.rect)
        
class ArrayTable(Table):
    def __init__(self, val, canvas, x, y):
        super().__init__(val, canvas, x ,y )
        self.width = ROW_SIZE 
        self.height = len(self.value) * ROW_SIZE
        self.rows = []
        self.display()

    def display(self):
        for i in range(len(self.value)):
            self.display_row(self.value[i], i)
        self.update_position()
            
    def display_row(self, item, value_id):
        self.rows.append(ValueRect(self.canvas, item, value_id))

    def update_position(self):
        x = self.x
        y = self.y
        for i in range(len(self.rows)):
            self.rows[i].move_to(x, y + i * ROW_SIZE)

    def get_row(self, value_id):
        return self.rows[value_id]
    
    def get_value(self, value_id):
        return self.get_row(value_id).get_value()
        
    def find_value_id(self, x, y):
        for row in self.rows:
            if row.is_position_inside(x, y):
                return row.get_value_id()

    def value_link_start(self, value_id):
        return self.get_row(value_id).link_start()

    def remove(self):
        for row in self.rows:
            self.canvas.delete(row.rect)
        
class ObjectRow(CanvasObject):
    def __init__(self, canvas, slot):
        super().__init__(canvas)
        self.canvas = canvas
        self.slot = slot
        self.x = 0
        self.y = 0
        self.message_width = ROW_SIZE
        self.display()
        
    def set_message_width(self, message_width):
        self.message_width = message_width
        canvas_rect_update_width(self.canvas, self.message_rect, self.message_width)

    def display(self):
        self.message_rect = canvas_create_rect(self.canvas, ROW_SIZE, ROW_SIZE)
        self.value_rect = canvas_create_rect(self.canvas, ROW_SIZE, ROW_SIZE)
        self.message_text = canvas_create_text(self.canvas, self.slot[0])

    def update_position(self, x, y):
        self.x = x
        self.y = y
        self.canvas.moveto(self.message_rect, x, y)
        self.canvas.moveto(self.value_rect, x + self.message_width, y)
        self.canvas.moveto(self.message_text, x + TEXT_PADDING_X, y + TEXT_PADDING_Y)

    def get_message_width(self):
        bbox = self.canvas.bbox(self.message_text)
        width = bbox[2] - bbox[0]
        return width

    def remove(self):
        self.canvas.delete(self.message_rect)
        self.canvas.delete(self.message_text)
        self.canvas.delete(self.value_rect)
        
        
        
class ObjectTable(Table):
    def __init__(self, val, canvas, x, y):
        super().__init__(val, canvas, x ,y )
        self.slots = list(proto.get_slots(val).items())
        self.message_width = 0
        self.width = self.message_width + ROW_SIZE 
        self.height = len(self.slots) * ROW_SIZE
        self.rows = []
        self.display()

    def display(self):
        for slot in self.slots:
            self.display_row(slot)
        self.canvas.update_idletasks()
        self.update_width()
        self.update_position()

            
    def display_row(self, slot):
        self.rows.append(ObjectRow(self.canvas, slot))

    def update_position(self):
        x = self.x
        y = self.y
        for i in range(len(self.rows)):
            self.rows[i].update_position(x, y + i * ROW_SIZE)

    def get_value(self, value_id):
        slot = self.slots[value_id]
        return slot[1]
        
    def find_value_id(self, x, y):
        if x >= self.x + self.message_width and x <= self.x + ROW_SIZE + self.message_width:
            value_id = int((y - self.y) // ROW_SIZE)
            return value_id

    def value_link_start(self, value_id):
        x = self.x + self.message_width + ROW_SIZE / 2
        y = self.y + ROW_SIZE * value_id + ROW_SIZE / 2
        return x, y

    def get_max_message_width(self):
        message_width = 0
        for row in self.rows:
            width = row.get_message_width()
            message_width = max(message_width, width)
        return message_width
        
    def update_width(self):
        message_width = self.get_max_message_width()
        self.message_width = message_width + 2 * TEXT_PADDING_X
        self.width = self.message_width + ROW_SIZE
        for row in self.rows:
            row.set_message_width(self.message_width)
            
    def remove(self):
        for row in self.rows:
            row.remove()

    
class Link(CanvasObject):
    def __init__(self, canvas, from_table, value_id, to_table):
        super().__init__(canvas)
        self.canvas = canvas
        self.from_table = from_table
        self.value_id = value_id
        self.to_table = to_table
        self.line = None
        self.display()

    def display(self):
        self.line = self.canvas.create_line(0, 0, 0, 0)
        self.update()

    def start_position(self):
        return self.from_table.value_link_start(self.value_id)

    def end_position(self):
        return self.to_table.x, self.to_table.y

    def update(self):
        x1, y1 = self.start_position()
        x2, y2 = self.end_position()
        self.canvas.coords(self.line, x1, y1, x2, y2)

    def is_from(self, from_table, value_id):
        return self.from_table == from_table and self.value_id == value_id
        
class ProtoUI:
    def __init__(self):
        top = tkinter.Tk()
        top.title("proto_ui")
        canvas = tkinter.Canvas(top, width=800, height=600)
        canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
        canvas.bind("<ButtonPress>", lambda event: self.button_press(event.num, event.x, event.y))
        canvas.bind("<ButtonRelease>", lambda event: self.button_release(event.num, event.x, event.y))
        canvas.bind("<Motion>", lambda event: self.motion(event.x, event.y))
        self.top = top
        self.canvas = canvas
        self.tables = []
        self.table_pressed = None
        self.is_dragged = False
        self.start_x = None
        self.start_y = None
        self.links = []
        self.ensure_row_size()

    def ensure_row_size(self):
        global ROW_SIZE
        if ROW_SIZE == None:
            text = self.canvas.create_text(10, 10, font=FONT, anchor="nw", text="M")
            self.canvas.update_idletasks()
            bbox = self.canvas.bbox(text)
            ROW_SIZE = bbox[3] - bbox[1] + 2 * TEXT_PADDING_Y
            self.canvas.delete(text)

    def update_links(self):
        for link in self.links:
            link.update()
                 
    def motion(self, x, y):
        if self.table_pressed:
            self.table_pressed.move_to(x - self.start_x, y - self.start_y)
            self.is_dragged = True
            self.update_links()

    def table_press(self, table, x, y):
        self.table_pressed = table
        self.start_x = x - table.x
        self.start_y = y - table.y
        self.is_dragged = False
           
    def button_press(self, button, x, y):
        table = self.table_below(x, y)
        if table:
            self.table_press(table, x, y)
            
    def add_link(self, from_table, value_id):
        value = from_table.get_value(value_id)
        x1, y1 = from_table.value_link_start(value_id)
        value_table = self.display_value(value, x1 + 2 * ROW_SIZE, y1)
        self.links.append(Link(self.canvas, from_table, value_id, value_table))

    def find_link(self, from_table, value_id):
        for link in self.links:
            if link.is_from(from_table, value_id):
                return link
            
    def remove_or_add_link(self, from_table, value_id):
        link = self.find_link(from_table, value_id)
        if link:
            self.remove_link(link)
        else:
            self.add_link(from_table, value_id)

    def button_release(self, button, x, y):
        if self.table_pressed and not self.is_dragged:
            value_id = self.table_pressed.find_value_id(x, y)
            if value_id != None:
                self.remove_or_add_link(self.table_pressed, value_id)
                
        if self.table_pressed and self.is_dragged:
            if self.table_pressed.is_outside_canvas():
                self.remove_table(self.table_pressed)
            
            
        self.table_pressed = None

    def find_table(self, value):
        for table in self.tables:
            if table.value == value:
                return table
    
    def table_below(self, x, y):
        for table in reversed(self.tables):
            if table.is_position_inside(x, y):
                return table

    def create_table(self, value, x, y):
        if type(value) == list:
            table = ArrayTable(value, self.canvas, x, y)
        elif isinstance(value, proto.Object):
            table = ObjectTable(value, self.canvas, x, y)
        else:
            table = AtomTable(value, self.canvas, x, y)
        self.tables.append(table)
        return table
        
    def display_value(self, value, x=0, y=0):
        table = self.find_table(value)
        if table:
            return table
        else:
            return self.create_table(value, x, y)

    def remove_table(self, table):
        for link in list(self.links):
            if link.from_table == table or link.to_table == table:
                self.remove_link(link)
        table.remove()
        self.tables.remove(table)

    def remove_link(self, link):
        self.canvas.delete(link.line)
        self.links.remove(link)

        
def display_object(obj):
    ProtoUI().display_value(obj, 10, 10)

"""
o1 = proto.obj.clone()
o2 = o1.clone().set_slot("a", 1)
o3 = proto.obj.clone().set_slot("items", [o1, o2])
display_object(o3)
"""