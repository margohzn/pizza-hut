from tkinter import * 
from tkinter.ttk import *

window = Tk()
window.geometry("600x350")
window.title("Pizza Hut")

def order():
    pizza_answer = selected_pizza.get()
    quantity_answer = quantity.get()
    size_answer = radio_button.get()
    summery = Label(window, text = f"You ordered {quantity_answer} {pizza_answer} in the size {size_answer}", font = ("times", 16)).grid(row = 5, column = 2, pady = 30)

#zero row
title = Label(window, text = "Welcome to pizza hut!", font = ("times", 30, "underline")).grid(row = 0, column = 2)

#first row 
label_1 = Label(window, text = "Select your fav pizza:", font = ("times", 20)).grid(row = 1, column = 1, pady = 30)

selected_pizza = StringVar()
pizza_types = Combobox(window, textvariable = selected_pizza, width = 15)
pizza_types["values"] = ("Pineapple Pizza", "Pepperoni Pizza", "Margherita Pizza", "Jambon Pizza", "Vegetarian Pizza")
pizza_types.grid( row = 1, column = 2)

#second row 
label_2 = Label(window, text = "Enter quantity:", font = ("times", 20)).grid(row = 2, column = 1)

quantity = IntVar()
quantitys = Combobox(window, textvariable = quantity, width = 15)
quantitys["values"] = tuple(range(20))
quantitys.grid(row = 2, column = 2)

#third row 
radio_button = StringVar()
Radiobutton(window, text = "S", variable = radio_button, value = "S").grid(row = 3, column = 1, pady = 30)
Radiobutton(window, text = "M", variable = radio_button, value = "M").grid(row = 3, column = 2)
Radiobutton(window, text = "L", variable = radio_button, value = "L").grid(row = 3, column = 3)

#forth row
button = Button(window, text = "Gnerate", command = order).grid(row = 4, column = 2)

window.mainloop()