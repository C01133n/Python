import tkinter as tk
# Import the PasswordManager, RegistrationForm, and PasswordEncoder classes from their respective scripts

from registration_form_script import RegistrationForm
from password_manager_script import PasswordManager
from password_encoder_script import PasswordEncoder

# Create the main window for the password manager
root = tk.Tk()
password_manager = PasswordManager(root) 
password_encoder = PasswordEncoder()

# Create the registration form window with password encoder integration
registration_form = RegistrationForm(root, password_manager, password_encoder)

root.mainloop()
