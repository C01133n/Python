import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = sender_email_entry.get()
    receiver_email = receiver_email_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    smtp_server = 'smtp.example.com'  # Update with your SMTP server
    smtp_port = 587  # Update with your SMTP server port
    smtp_username = 'your_smtp_username'  # Update with your SMTP username
    smtp_password = 'your_smtp_password'  # Update with your SMTP password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        messagebox.showinfo("Success", "Email sent successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email.\nError: {e}")

# Create the main window
root = tk.Tk()
root.title("Email Sender")

# Create widgets
sender_email_label = tk.Label(root, text="Sender Email:")
sender_email_entry = tk.Entry(root, width=40)
receiver_email_label = tk.Label(root, text="Receiver Email:")
receiver_email_entry = tk.Entry(root, width=40)
subject_label = tk.Label(root, text="Subject:")
subject_entry = tk.Entry(root, width=40)
message_label = tk.Label(root, text="Message:")
message_text = tk.Text(root, width=40, height=10)
send_button = tk.Button(root, text="Send Email", command=send_email)

# Place widgets using grid layout
sender_email_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
sender_email_entry.grid(row=0, column=1, padx=10, pady=5)
receiver_email_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
receiver_email_entry.grid(row=1, column=1, padx=10, pady=5)
subject_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
subject_entry.grid(row=2, column=1, padx=10, pady=5)
message_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
message_text.grid(row=3, column=1, padx=10, pady=5)
send_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
