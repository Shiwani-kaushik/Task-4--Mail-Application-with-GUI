import tkinter as tk
from tkinter import messagebox


def send_email():
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    # Code to send the email
    # Replace this with your actual email sending logic

    messagebox.showinfo("Email Sent", "Your email has been sent successfully!")


# Create the main window
window = tk.Tk()
window.title("Mail Application")

# Recipient Entry
recipient_label = tk.Label(window, text="Recipient:")
recipient_label.pack()
recipient_entry = tk.Entry(window)
recipient_entry.pack()

# Subject Entry
subject_label = tk.Label(window, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(window)
subject_entry.pack()

# Message Text Box
message_label = tk.Label(window, text="Message:")
message_label.pack()
message_text = tk.Text(window, height=10, width=50)
message_text.pack()

# Send Button
send_button = tk.Button(window, text="Send", command=send_email)
send_button.pack()

# Run the application
window.mainloop()
