import tkinter as tk
from textblob import TextBlob

# Initialize the main window
root = tk.Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

def check_spelling(event=None):  # Allow for an optional event parameter
    word = enter_text.get().strip()
    if not word:
        spell.config(text="Please enter a word!", fg="red")
        return
    
    corrected_word = str(TextBlob(word).correct())
    spell.config(text=f"Correct Text is: {corrected_word}", fg="#364971")

# Heading Label
heading = tk.Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50, 0))

# Entry Box
enter_text = tk.Entry(root, justify="center", width=30, font=("Poppins", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

# Bind the Enter key to the check_spelling function
enter_text.bind("<Return>", check_spelling)

# Check Button
button = tk.Button(root, text="Check", font=("Arial", 20, "bold"), fg="white", bg="red", command=check_spelling)
button.pack()

# Spell Correction Label (initially empty)
spell = tk.Label(root, font=("Poppins", 20), bg="#dae6f6", fg="#364971")
spell.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
