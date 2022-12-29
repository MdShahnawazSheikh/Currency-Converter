import tkinter
import customtkinter
from customtkinter import *
from conversion import convert
import pandas
PROJECT_NAME = "Currency Converter"


# Creating list of currencies
data = pandas.read_csv("currency_codes.csv")
raw = data.AlphabeticCode.to_list()
currencies = []
for code in raw:
    if code not in currencies:
        currencies.append(code)
# Creating list of currencies


# Modes: system (default), light, dark
customtkinter.set_appearance_mode("Dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.minsize(600, 300)
app.maxsize(600, 300)
app.title(PROJECT_NAME)
app.configure(padx=30, pady=30)
############################Switching Mode Functionality#########################
def mode_button():
    def switch_to_light():
        customtkinter.set_appearance_mode("Light")
        switch.configure(text="Light Mode")

    def switch_to_dark():
        customtkinter.set_appearance_mode("Dark")
        switch.configure(text="Dark Mode")
    if switch.get() == 1:
        switch_to_light()
    else:
        switch_to_dark()


switch = CTkSwitch(master=app, text="Dark Mode", command=mode_button, bg_color='transparent')
switch.pack()
############################Switching Mode Functionality#########################

title = customtkinter.CTkLabel(master=app, text=PROJECT_NAME, font=('Arial', 30, 'bold'))
title.place(x=135, y=40)


# Convert from button
from_value = StringVar()
from_value.set("SELECT")
from_currency = CTkOptionMenu(master=app,values=currencies, variable=from_value)
from_currency.place(x=100, y=100)
# Convert from button

# Middle text
to_text = CTkLabel(master=app, text="TO", font=('Arial', 20, 'bold'))
to_text.place(x=258, y=100)
# Middle text

# Convert to button
to_value = StringVar()
to_value.set("SELECT")

to_currency = CTkOptionMenu(master=app,variable=to_value, values=currencies)
to_currency.place(x=300, y=100)
# Convert to button

# TO get amount from user
amount_box = CTkEntry(master=app)
amount_box.place(x=200, y=140)
# TO get amount from user


# Convert button
result_label = CTkLabel(master=app, text=f"Result: 0", font=('Arial', 20, 'bold'))
def convert_button():
    amount = float(amount_box.get())
    response = convert(from_value.get(), to_value.get(), amount)
    result_label.configure(text=f"Result: {response:.2f}")
    result_label.pack(side="bottom")

convert_button = CTkButton(master=app, text="Convert", font=("Arial", 15, 'bold'), command=convert_button)
convert_button.place(x=200, y=175)
# Convert button


app.mainloop()