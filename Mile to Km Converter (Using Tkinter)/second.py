from tkinter import *

window = Tk()
window.minsize(width=400, height=200)
window.title("Second Miles to Km Converter")
window.config(padx=300, pady=150)

def click_button():
    new_input = int(input.get())
    label_answer.config(text=(new_input * 1.60934))
    pass

input = Entry(width=10)
input.grid(column=1, row=0)

label_Miles = Label(text="Miles")
label_Miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

label_answer = Label(text="0")
label_answer.grid(column=1, row=1)

button = Button(text="Calculate", command=click_button)
button.grid(column=1, row=2)







window.mainloop()