from tkinter import *

def button_clicked():
    new_input = int(input.get())
    label_answer.config(text=(new_input * 1.60934))




window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=400, height=200)
window.config(padx=20, pady=20)
# window.config(padx=100, pady=100), this is a widget configuration


label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)
# Label() are for text input
# grid is for coordinate positioning

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)
# input is to get users input

label_answer = Label(text="0")
label_answer.grid(column=1, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
# button is assigns a clickable text that can return command






window.mainloop()
# this is necessary to show display on the screen