
from tkinter import *


window = Tk()
window.title("Unit Converter")
window.minsize(width=400,height=200)
window.config(padx=80,pady=30)

unit_input = Entry(width=10)
unit_input.grid(column=1,row=0)

unit_label = Label(text = "Miles")
unit_label.grid(column=2,row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0,row=1)

result_label = Label(text="0")
result_label.grid(column=1,row=1)

result_unit = Label(text="km")
result_unit.grid(column=2,row=1)



def button_clicked():
    new_value = unit_input.get()
    result_label.config(text = float(new_value)*1.609)


button = Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=2)
window.mainloop()