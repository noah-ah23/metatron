import tkinter as tk
from tkinter import scrolledtext
cipher_map = {
    "A": "95bb1b7e", "B": "09496ec4", "C": "58e705b3", "D": "a42b", "E": "x",
    "F": "72d74997", "G": "4751536b", "H": "b2574b15032b", "I": "iI628", "J": "urlb739j",
    "K": "74ke328", "L": "ue7304ml8", "M": "6825msi7", "N": "738hd53uj", "O": "jhx3679b",
    "P": "ia629mke", "Q": "nd68k", "R": "k7922p0", "S": "um37os", "T": "uej36",
    "U": "z3", "V": "z4", "W": "z5", "X": "638znm", "Y": "z17",
    "Z": "z8"
}
decipher_map = {v: k for k, v in cipher_map.items()}
def encrypt(text):
    result = "".join(cipher_map.get(char.upper(), char) for char in text)
    log_console(f"decypher: {result}")
    return result
def decrypt(text):
    temp = ""
    result = ""
    for char in text:
        temp += char
        if temp in decipher_map:
            result += decipher_map[temp]
            temp = ""
    log_console(f"encypher: {result}")
    return result
def log_console(message):
    console_output.config(state=tk.NORMAL)
    console_output.insert(tk.END, f"[LOG] {message}\n")
    console_output.config(state=tk.DISABLED)
    console_output.yview(tk.END)
def encrypt_text():
    text = input_entry.get()
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypt(text))
    output_text.config(state=tk.DISABLED)
def decrypt_text():
    text = input_entry.get()
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypt(text))
    output_text.config(state=tk.DISABLED)
root = tk.Tk()
root.title("Metatron – Cypher en- & decryption")
root.geometry("700x500")
root.configure(bg="black")
title_label = tk.Label(root, text="Metatron", font=("Courier", 16, "bold"), bg="black", fg="red")
title_label.pack(pady=10)
input_label = tk.Label(root, text="your message here:", bg="black", fg="lime")
input_label.pack()
input_entry = tk.Entry(root, width=50, bg="black", fg="lime", insertbackground="lime", font=("Courier", 12))
input_entry.pack(pady=5)
output_label = tk.Label(root, text="Metatron is an easy tool to cypher & secure your messages", bg="black", fg="lime")
output_label.pack()
output_text = scrolledtext.ScrolledText(root, height=3, width=50, state=tk.DISABLED, bg="black", fg="lime", font=("Courier", 12))
output_text.pack(pady=10)
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=10)
btn_encrypt = tk.Button(button_frame, text="encypher", command=encrypt_text, bg="red", fg="white", width=10, font=("Courier", 12))
btn_encrypt.grid(row=0, column=0, padx=10, pady=5)
btn_decrypt = tk.Button(button_frame, text="decypher", command=decrypt_text, bg="red", fg="white", width=10, font=("Courier", 12))
btn_decrypt.grid(row=0, column=1, padx=10, pady=5)
btn_exit = tk.Button(root, text="exit", command=root.quit, bg="red", fg="white", width=15, font=("Courier", 12))
btn_exit.pack(pady=10)
console_label = tk.Label(root, text="Logs:", bg="black", fg="lime")
console_label.pack()
console_output = scrolledtext.ScrolledText(root, height=8, width=80, state=tk.DISABLED, bg="black", fg="lime", font=("Courier", 10))
console_output.pack(pady=10)
root.mainloop()
