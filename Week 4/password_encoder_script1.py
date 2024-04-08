import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import random
import string
import pyperclip

class PasswordEncoderGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Encoder")

        # Configure pink color scheme
        self.master.configure(bg="#FFB6C1")  # LightPink color for the window background

        self.username_label = tk.Label(master, text="Username:", bg="#FFB6C1")  # LightPink color for the label background
        self.username_label.pack()

        self.username_entry = tk.Entry(master, bg="white")  # White color for the entry background
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:", bg="#FFB6C1")  # LightPink color for the label background
        self.password_label.pack()

        self.password_entry = tk.Entry(master, show="*", bg="white")  # White color for the entry background
        self.password_entry.pack()

        self.generate_button = tk.Button(master, text="Generate", command=self.generate_password, bg="#FF69B4")  # HotPink color for the button background
        self.generate_button.pack()

        self.encode_button = tk.Button(master, text="Encode & Save", command=self.encode_and_save, bg="#FF69B4")  # HotPink color for the button background
        self.encode_button.pack()

        self.status_label = tk.Label(master, text="", bg="#FFB6C1")  # LightPink color for the label background
        self.status_label.pack()

        # Generate a key for encryption/decryption
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def generate_password(self):
        # Generate a strong random password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(12))  # Generate a 12-character password
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def encode_and_save(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            encoded_password = self.encode(password)
            self.save_credentials(username, encoded_password)
            self.status_label.config(text="Credentials saved successfully.")
            # Copy the encoded password to the clipboard
            pyperclip.copy(encoded_password)
            messagebox.showinfo("Success", "Encoded password copied to clipboard.")
        else:
            self.status_label.config(text="Please enter username and password.")

    def encode(self, password):
        # Encrypt the password
        encrypted_password = self.cipher_suite.encrypt(password.encode())
        return encrypted_password.decode()

    def save_credentials(self, username, password):
        # Save the username and encrypted password to a .txt file
        with open("credentials.txt", "a") as file:
            file.write(f"Username: {username}\nPassword: {password}\n\n")

def main():
    root = tk.Tk()
    app = PasswordEncoderGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
