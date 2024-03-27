import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    # Get input from GUI widgets
    to_email = to_email_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)

    # Email configuration
    smtp_server = 'smtp.example.com'  # SMTP server address
    smtp_port = 587  # SMTP port (587 for TLS)
    sender_email = 'your_email@example.com'  # Sender's email address
    sender_password = 'your_password'  # Sender's email password

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add body to message
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS for security
        # Login to the SMTP server
        server.login(sender_email, sender_password)
        # Send email
        server.send_message(msg)
        # Close SMTP session
        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error sending email: {e}")

# Create GUI window
window = tk.Tk()
window.title("Email Sender")

# GUI widgets
to_email_label = tk.Label(window, text="To:")
to_email_label.pack()
to_email_entry = tk.Entry(window)
to_email_entry.pack()

subject_label = tk.Label(window, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(window)
subject_entry.pack()

body_label = tk.Label(window, text="Body:")
body_label.pack()
body_text = tk.Text(window, height=10, width=50)
body_text.pack()

send_button = tk.Button(window, text="Send Email", command=send_email)
send_button.pack()

# Start GUI main loop
window.mainloop()
