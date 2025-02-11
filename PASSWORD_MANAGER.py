from tkinter import *  # Importing all modules from Tkinter
from tkinter import messagebox  # Importing messagebox for displaying alerts
from random import choice, randint, shuffle  # Importing random functions for password generation
import string  # Importing string module for character sets
import pyperclip  # Importing pyperclip to copy passwords to clipboard


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generates a random password using letters, numbers, and symbols."""
    letters = string.ascii_letters  # All uppercase and lowercase letters
    numbers = string.digits  # Digits 0-9
    symbols = "!#$%&()*+"  # Commonly used special symbols

    # Generating random characters from each category
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combining all characters into a list and shuffling for randomness
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Converting list to string
    password = "".join(password_list)

    password_entry.delete(0, 'end')  # Clearing any existing password in the entry field
    password_entry.insert(0, password)  # Inserting the generated password into the field
    pyperclip.copy(password)  # Copying the password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Saves the entered website, email, and password to a file."""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check if any fields are empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.txt", "r") as data_file:
                data = data_file.readlines()  # Reading existing data
        except FileNotFoundError:
            data = []  # If file not found, initialize an empty list

        found = False  # Flag to check if website and email exist already
        for index, line in enumerate(data):
            line = line.strip()
            stored_website, stored_email, stored_password = line.split(" | ")

            # If the website and email already exist in the file
            if website == stored_website and email == stored_email:
                found = True
                changing_password = messagebox.askokcancel(
                    title=website,
                    message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\n"
                            f"Do you want to change the password?"
                )
                if changing_password:
                    # Update existing password
                    data[index] = f"{website} | {email} | {password}\n"
                    with open("data.txt", "w") as data_file:
                        data_file.writelines(data)  # Save updated data
                    clear_entries()

        # If the website and email are not found, add a new entry
        if not found:
            is_ok = messagebox.askokcancel(
                title=website,
                message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it OK to save?"
            )
            if is_ok:
                with open("data.txt", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password}\n")
                clear_entries()


def clear_entries():
    """Clears all input fields."""
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

frame = Frame(window)
frame.grid(row=0, column=0)

canvas = Canvas(frame, height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(frame, text="Website:", fg="black", font=("Arial", 12, "bold"))
website_label.grid(row=1, column=0)

email_label = Label(frame, text="Email/Username:", fg="black", font=("Arial", 12, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(frame, text="Password:", fg="black", font=("Arial", 12, "bold"))
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(frame, bg="#ffffff", font=("Arial", 11, "bold"), bd=2)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()

email_entry = Entry(frame, bg="#ffffff", font=("Arial", 11, "bold"), bd=2)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

password_entry = Entry(frame, bg="#ffffff", font=("Arial", 11, "bold"), bd=2)
password_entry.grid(row=3, column=1, sticky="ew")

# Buttons
generate_password_button = Button(frame, text="Generate Password", command=generate_password,
                                  bg="#007BFF", fg="white",
                                  font=("Arial", 11, "bold"))
generate_password_button.grid(row=3, column=2)

add_button = Button(frame, text="Add", width=36, command=save, bg="#4CAF50", fg="white",
                    font=("Arial", 11, "bold"))
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
