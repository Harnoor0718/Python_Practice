import tkinter as tk
from tkinter import messagebox
import win32com.client

# Initialize Windows Speech API
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Function to speak names
def speak_names():
    names = entry.get().split(",")  # Get names separated by commas
    if not names:
        messagebox.showwarning("Input Error", "Please enter at least one name.")
        return
    for name in names:
        text = f"Congratulations {name.strip()}"
        print(text)
        speaker.Speak(text)

# Create GUI window
root = tk.Tk()
root.title("Congratulations Speaker")
root.geometry("400x150")

# Label
tk.Label(root, text="Enter names separated by commas:").pack(pady=10)

# Entry box
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Button
tk.Button(root, text="Say Congratulations!", command=speak_names).pack(pady=10)

root.mainloop()
