import customtkinter
from password_generator import numbers, letters, both, copy

# -- Configurations --
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# -- Saved Passwords ---
passwords = {}

# -- Interface Functions --
def ui_numbers():
    try:
        generated_password = numbers(int(password_length.get()))
        passwords['numbers'] = generated_password
        copy(generated_password)
        label_password.configure(text=generated_password)

    except ValueError:
        label_password.configure(text="Digit the correct value")

def ui_letters():
    try:
        generated_password = letters(int(password_length.get()))
        passwords['letters'] = generated_password
        copy(generated_password)
        label_password.configure(text=generated_password)
    except ValueError:
        label_password.configure(text="Digit the correct value")

def ui_both():
    try:
        generated_password = both(int(password_length.get()))
        passwords['both'] = generated_password
        copy(generated_password)
        label_password.configure(text=generated_password)
    except ValueError:
        label_password.configure(text="Digit the correct value")


def last_passwords():
    label_last_passwords.configure(text="\n".join(passwords.values()))


# -- Window --
app = customtkinter.CTk()
app.title("Password Generator by Jonatas Figueiredo")
app.geometry("900x800")

# ---- Widgets ---
frame = customtkinter.CTkFrame(app)
frame.pack(padx=100, pady=80, fill="both", expand=True)

title = customtkinter.CTkLabel(frame, text="Password Generator", font=("Roboto",48))
title.pack(padx=60, pady=20)

subtitle = customtkinter.CTkLabel(frame, text="Generate your strong password", font=("Roboto",28))
subtitle.pack(padx=4, pady=4)

password_length = customtkinter.CTkEntry(frame, placeholder_text="Length",placeholder_text_color="green", width=400)
password_length.pack(padx=10,pady=10)

btn_numbers = customtkinter.CTkButton(frame, text="Numbers", command=ui_numbers)
btn_numbers.pack(padx=10, pady=10)

btn_letters = customtkinter.CTkButton(frame, text="Letters", command=ui_letters)
btn_letters.pack(padx=10, pady=10)

btn_both = customtkinter.CTkButton(frame, text="Numbers and Letters", command=ui_both)
btn_both.pack(padx=10, pady=10)

label_password = customtkinter.CTkLabel(frame, text="", font=("Courier",32))
label_password.pack(padx=10, pady=10)

btn_last_passwords = customtkinter.CTkButton(frame, text="Last Passwords", command=last_passwords)
btn_last_passwords.pack(padx=10, pady=10)

label_last_passwords = customtkinter.CTkLabel(frame, text="", font=("Courier",32))
label_last_passwords.pack(padx=10, pady=10)

# -- Application --
app.mainloop()