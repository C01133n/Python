import tkinter as tk
from tkinter import messagebox

# Placeholder for the PasswordManager class
class PasswordManager:
    def __init__(self, master):
        self.credentials = {}  # Placeholder for storing credentials

# Define the RegistrationForm class
class RegistrationForm:
    def __init__(self, master, password_manager):
        self.master = master
        self.master.title("Registration Form")
        self.password_manager = password_manager

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(master, text="Register", command=self.register_account)
        self.register_button.pack()

    def register_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            self.password_manager.credentials[username] = password
            self.clear_entries()
            messagebox.showinfo("Success", "Account registered successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter username and password.")

    def clear_entries(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

# Create the main window for the password manager
root = tk.Tk()
password_manager = PasswordManager(root) 

# Create the registration form window
registration_form = RegistrationForm(root, password_manager)

root.mainloop()
