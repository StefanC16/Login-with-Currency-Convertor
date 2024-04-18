import requests
import tkinter
from tkinter import messagebox

def convert_currency():
    from_currency = from_currency_entry.get().upper()
    to_currency = to_currency_entry.get().upper()
    amount = float(amount_entry.get())

    response = requests.get(
        f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

    converted_amount = response.json()['rates'][to_currency]
    result_label.config(text=f"Conversia sumei de {amount} {from_currency} = {converted_amount} {to_currency}")

def login():
    username = 'admin'
    password = 'admin'
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login", message="You successfully logged in.")
        hide_login_widgets()
        show_converter_widgets()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

def hide_login_widgets():
    login_label.grid_forget()
    username_label.grid_forget()
    username_entry.grid_forget()
    password_label.grid_forget()
    password_entry.grid_forget()
    login_button.grid_forget()
    #registration_link.grid_forget()

def show_converter_widgets():
    header_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    from_currency_label.grid(row=1, column=0)
    from_currency_entry.grid(row=1, column=1, pady=10)
    to_currency_label.grid(row=2, column=0)
    to_currency_entry.grid(row=2, column=1, pady=10)
    amount_label.grid(row=3, column=0)
    amount_entry.grid(row=3, column=1, pady=10)
    convert_button.grid(row=4, column=1, columnspan=2, pady=20)
    result_label.grid(row=5, column=0, columnspan=2, pady=10)

window = tkinter.Tk()
window.title("Currency Converter")
window.geometry("850x600")
window.configure(bg='#333333')

# Widget-uri pentru Login
frame_login = tkinter.Frame(window, bg='#333333')
login_label = tkinter.Label(frame_login, text="Login", bg='#333333', fg="#FF7930", font=("Arial", 30))
username_label = tkinter.Label(frame_login, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame_login, font=("Arial", 16))
password_entry = tkinter.Entry(frame_login, show="*", font=("Arial", 16))
password_label = tkinter.Label(frame_login, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(frame_login, text="Login", bg="#FF7930", fg="#FFFFFF", font=("Arial", 16), command=login)
#registration_link = tkinter.Label(frame_login, text="Register", bg='#FF7877', fg="#FFFFFF", font=("Arial", 12), cursor="hand2")

# Widget-uri pentru Currency Converter
frame_converter = tkinter.Frame(window, bg='#333333')
header_label = tkinter.Label(frame_converter, text="Convertor valutar", bg='#333333', fg="#F5BF33", font=("Arial", 30))
from_currency_label = tkinter.Label(frame_converter, text="Din moneda:", bg='#333333', fg="#F5BF33", font=("Arial", 16))
from_currency_entry = tkinter.Entry(frame_converter, bg='#333333', font=("Arial", 16))
to_currency_entry = tkinter.Entry(frame_converter, bg='#333333', font=("Arial", 16))
to_currency_label = tkinter.Label(frame_converter, text="In moneda:", bg='#333333', fg="#F5BF33", font=("Arial", 16))
amount_entry = tkinter.Entry(frame_converter, bg='#333333', font=("Arial", 16))
amount_label = tkinter.Label(frame_converter, text="Valoare:", bg='#333333', fg="#F5BF33", font=("Arial", 16))
convert_button = tkinter.Button(frame_converter, text="Converteaza", bg="#333333", fg="#F5BF33", font=("Arial", 16), command=convert_currency)
result_label = tkinter.Label(frame_converter, bg='#333333', fg="#F5BF33", font=("Arial", 16))

#registration_link.bind("<Button-1>", lambda event: open_registration_window())

# Layout-ul pentru widget-urile de Login
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
#registration_link.grid(row=4, column=0, columnspan=2, pady=10)
frame_login.pack()

# Layout-ul pentru widget-urile de Currency Converter
frame_converter.pack()

window.mainloop()