from tkinter import *
from collections import Counter

root = Tk()
root.title("Word Frequency Counter by CSC-DS Team 9")
root.geometry("644x343")

Label(root, text="Enter text to analyze:").pack(pady=5)
text_input = Entry(root, width=50)
text_input.pack(pady=5)

output_label = Label(root, text="", justify=LEFT)
output_label.pack(pady=10)

def check():
    text = text_input.get().strip().lower()
    if not text:
        output_label.config(text="Please enter some text.")
        return
    words = text.split()
    frequency = Counter(words)
    freq_text = "\n".join(f"{word}: {count}" for word, count in frequency.items())
    output_label.config(text=f"Word Frequencies:\n{freq_text}")

Button(root, text="Count Frequencies", command=check).pack(pady=5)

root.mainloop()

