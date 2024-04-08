import tkinter as tk
from tkinter import messagebox

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")

        self.account_label = tk.Label(master, text="Account:")
        self.account_label.pack()

        self.account_entry = tk.Entry(master)
        self.account_entry.pack()

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.save_button = tk.Button(master, text="Save", command=self.save_password)
        self.save_button.pack()

        self.retrieve_button = tk.Button(master, text="Retrieve", command=self.retrieve_password)
        self.retrieve_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.credentials = {}  # Dictionary to store account-username-password triplets

    def save_password(self):
        account = self.account_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if account and username and password:
            self.credentials[account] = (username, password)
            self.clear_entries()
            self.result_label.config(text="Credentials saved successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter account, username, and password.")

    def retrieve_password(self):
        account = self.account_entry.get()

        if account in self.credentials:
            username, password = self.credentials[account]
            self.clear_entries()
            self.result_label.config(text=f"Account: {account}\nUsername: {username}\nPassword: {password}")
        else:
            messagebox.showerror("Error", "Account not found.")

    def clear_entries(self):
        self.account_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
app = PasswordManager(root)
root.mainloop()
