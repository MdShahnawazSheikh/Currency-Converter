import tkinter
import customtkinter
from customtkinter import *
from conversion import convert
PROJECT_NAME = "Currency Converter"


# Modes: system (default), light, dark
customtkinter.set_appearance_mode("Dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.iconbitmap('icon.ico')
app.minsize(600, 310)
app.maxsize(600, 310)
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

# Title
title = customtkinter.CTkLabel(master=app, text=PROJECT_NAME, font=('Arial', 30, 'bold'))
title.place(x=135, y=40)
# Title


# Convert from button
from_currency = CTkEntry(master=app)
from_currency.place(x=108, y=100)
# Convert from button

# Middle text
to_text = CTkLabel(master=app, text="TO", font=('Arial', 20, 'bold'))
to_text.place(x=258, y=100)
# Middle text

# Convert to button
to_currency = CTkEntry(master=app)
to_currency.place(x=300, y=100)
# Convert to button

# TO get amount from user
amount_box = CTkEntry(master=app)
amount_box.place(x=200, y=140)
# TO get amount from user


# Convert button
result_label = CTkLabel(master=app, text=f"Result: 0", font=('Arial', 20, 'bold'))
def convert_button_action():
    try:
        amount = float(amount_box.get())
            # To handle invalid entry exception
        try:
            response = convert((from_currency.get()).upper(), (to_currency.get()).upper(), amount)
            result_label.configure(text=f"Result: {response:.2f}")
            result_label.pack(side="bottom")
        except:
            result_label.configure(text=f"Invalid Currency Format!\nPlease enter 3 digit Currency Code")
            result_label.pack(side="bottom")
        # To handle invalid entry exception
    except:
        result_label.configure(text="Please enter amount!")
        result_label.pack(side="bottom")
   
convert_button = CTkButton(master=app, text="Convert", font=("Arial", 15, 'bold'), command=convert_button_action)
convert_button.place(x=200, y=175)
# Convert button


app.mainloop()