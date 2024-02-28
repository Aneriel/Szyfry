import tkinter as tk
import random

def generate_polybius_table(key):
    key = key.lower().replace(" ", "")
    alphabet = 'abcdefghiklmnopqrstuvwxyz'  # Zgodnie z szyfrem Polibiusza
    key_set = set(key)
    polybius_table = list(key)
    for char in alphabet:
        if char not in polybius_table and char != 'j':
            polybius_table.append(char)
    return polybius_table

def generate_random_key():
    alphabet = 'abcdefghiklmnopqrstuvwxyz'  # Zgodnie z szyfrem Polibiusza
    random_key = random.sample(alphabet, len(alphabet))
    return ''.join(random_key)

def encrypt(text, polybius_table):
    encrypted_text = ""
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char == 'j':
                char = 'i'  # Zamiana litery 'j' na 'i', zgodnie z szyfrem Polibiusza
            if char in polybius_table:
                index = polybius_table.index(char)
                row = index // 5
                col = index % 5
                encrypted_text += str(row + 1) + str(col + 1)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, polybius_table):
    decrypted_text = ""
    for i in range(0, len(text), 2):
        chunk = text[i:i+2]
        if chunk.isdigit():
            row = int(chunk[0]) - 1
            col = int(chunk[1]) - 1
            index = row * 5 + col
            decrypted_text += polybius_table[index]
        else:
            decrypted_text += chunk
    return decrypted_text

def encrypt_text():
    text = entry_text.get().replace(" ", "")
    key = entry_key.get()
    polybius_table = generate_polybius_table(key)
    encrypted_text = encrypt(text, polybius_table)
    entry_encrypted.delete(0, tk.END)
    entry_encrypted.insert(0, encrypted_text)

def decrypt_text():
    text = entry_encrypted.get()
    key = entry_key.get()
    polybius_table = generate_polybius_table(key)
    decrypted_text = decrypt(text, polybius_table)
    entry_decrypted.delete(0, tk.END)
    entry_decrypted.insert(0, decrypted_text)

def display_table():
    key = entry_key.get()
    polybius_table = generate_polybius_table(key)
    for i in range(5):
        for j in range(5):
            index = i * 5 + j
            entry_cells[index].delete(0, tk.END)
            entry_cells[index].insert(0, polybius_table[index])

def generate_random_key_and_display():
    random_key = generate_random_key()
    entry_key.delete(0, tk.END)
    entry_key.insert(0, random_key)
    display_table()

root = tk.Tk()
root.title("Szyfr Polibiusza")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_text = tk.Label(frame_input, text="Tekst:")
label_text.grid(row=0, column=0)

entry_text = tk.Entry(frame_input)
entry_text.grid(row=0, column=1)

label_key = tk.Label(frame_input, text="Klucz:")
label_key.grid(row=1, column=0)

entry_key = tk.Entry(frame_input)
entry_key.grid(row=1, column=1)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

button_encrypt = tk.Button(frame_buttons, text="Zaszyfruj", command=encrypt_text)
button_encrypt.grid(row=0, column=0, padx=5)

button_decrypt = tk.Button(frame_buttons, text="Odszyfruj", command=decrypt_text)
button_decrypt.grid(row=0, column=1, padx=5)

button_table = tk.Button(frame_buttons, text="Wyświetl Tabelę", command=display_table)
button_table.grid(row=0, column=2, padx=5)

button_random_key = tk.Button(frame_buttons, text="Losowy Klucz", command=generate_random_key_and_display)
button_random_key.grid(row=0, column=3, padx=5)

frame_output = tk.Frame(root)
frame_output.pack(pady=10)

label_encrypted = tk.Label(frame_output, text="Zaszyfrowany tekst:")
label_encrypted.grid(row=0, column=0)

entry_encrypted = tk.Entry(frame_output)
entry_encrypted.grid(row=0, column=1)

label_decrypted = tk.Label(frame_output, text="Odszyfrowany tekst:")
label_decrypted.grid(row=1, column=0)

entry_decrypted = tk.Entry(frame_output)
entry_decrypted.grid(row=1, column=1)

frame_table = tk.Frame(root)
frame_table.pack(pady=10)

entry_cells = []

for i in range(5):
    for j in range(5):
        entry_cell = tk.Entry(frame_table, width=4)
        entry_cell.grid(row=i, column=j, padx=3, pady=3)
        entry_cells.append(entry_cell)

root.mainloop()
