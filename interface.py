import customtkinter
from password_generator import numbers, letters, both

# -- Configurations --
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# -- Interface Functions --
def UI_numbers():
    try:
        generated_password = numbers(int(password_length.get()))
        label_password.configure(text=generated_password)
    except ValueError:
        label_password.configure(text="Digit the correct value")

def UI_letters():
    try:
        generated_password = letters(int(password_length.get()))
        label_password.configure(text=generated_password)
    except ValueError:
        label_password.configure(text="Digit the correct value")

def UI_both():
    try:
        generated_password = both(int(password_length.get()))
        label_password.configure(text=generated_password)
    except ValueError:
        label_password.configure(text="Digit the correct value")

# -- Window --
app = customtkinter.CTk()
app.title("Password Generator by Jonatas Figueiredo")
app.geometry("450x400")

# ---- Widgets ---
frame = customtkinter.CTkFrame(app)
frame.pack(padx=50, pady=30, fill="both", expand=False)

title = customtkinter.CTkLabel(frame, text="Password Generator", font=("Roboto",24))
title.pack(padx=30, pady=10)

subtitle = customtkinter.CTkLabel(frame, text="Generate your strong password", font=("Roboto",14))
subtitle.pack(padx=2, pady=2)

password_length = customtkinter.CTkEntry(frame, placeholder_text="Length",placeholder_text_color="green", width=200)
password_length.pack(padx=5,pady=5)

btn_numbers = customtkinter.CTkButton(frame, text="Numbers", command=UI_numbers)
btn_numbers.pack(padx=5, pady=5)

btn_letters = customtkinter.CTkButton(frame, text="Letters", command=UI_letters)
btn_letters.pack(padx=5, pady=5)

btn_both = customtkinter.CTkButton(frame, text="Numbers and Letters", command=UI_both)
btn_both.pack(padx=5, pady=5)

label_password = customtkinter.CTkLabel(frame, text="", font=("Courier",16))
label_password.pack(padx=5, pady=5)

# -- Application --
app.mainloop()