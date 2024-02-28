import tkinter as tk
import random

def generate_homophonic_key():
    homophonic_chars = ['$', 'ö', 'æ', 'ß', 'þ', 'ø', 'ß', 'ø', '¥', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß', '£', '¥', '¢', 'ß']
    homophonic_counts = {
        'a': 9, 'ą': 1, 'b': 1, 'c': 4, 'ć': 1, 'd': 3, 'e': 8, 'ę': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 8, 'j': 2,
        'k': 4, 'l': 2, 'ł': 2, 'm': 3, 'n': 6, 'ń': 1, 'o': 8, 'ó': 1, 'p': 3, 'q': 1, 'r': 5, 's': 4, 'ś': 1,
        't': 4, 'u': 3, 'v': 1, 'w': 5, 'x': 1, 'y': 4, 'z': 6, 'ż': 1, 'ź': 1
    }
    
    key_chars = []
    for char, count in homophonic_counts.items():
        homophonic = [char.upper()] + [char.lower()] * (count - 1)
        random.shuffle(homophonic)
        key_chars.extend(homophonic)
    
    remaining_chars = 108 - len(key_chars)
    for _ in range(remaining_chars):
        key_chars.append(random.choice(homophonic_chars))
    
    random.shuffle(key_chars)
    return ''.join(key_chars)

def encrypt(text, homophonic_key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            index = ord(char.lower()) - ord('a')
            encrypted_char = homophonic_key[index]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, homophonic_key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            index = homophonic_key.find(char)
            original_char = chr(index + ord('a'))
            decrypted_text += original_char
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_text():
    text = entry_text.get()
    key = entry_key.get()
    homophonic_key = generate_homophonic_key()
    encrypted_text = encrypt(text, homophonic_key)
    entry_encrypted.delete(0, tk.END)
    entry_encrypted.insert(0, encrypted_text)

def decrypt_text():
    text = entry_encrypted.get()
    key = entry_key.get()
    homophonic_key = generate_homophonic_key()
    decrypted_text = decrypt(text, homophonic_key)
    entry_decrypted.delete(0, tk.END)
    entry_decrypted.insert(0, decrypted_text)

def generate_and_display_key():
    key = generate_homophonic_key()
    entry_key.delete(0, tk.END)
    entry_key.insert(0, key)

root = tk.Tk()
root.title("Szyfr Homofoniczny")

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

button_generate_key = tk.Button(frame_buttons, text="Generuj Klucz", command=generate_and_display_key)
button_generate_key.grid(row=0, column=2, padx=5)

frame_output = tk.Frame(root)
frame_output.pack(pady=10)

label_encrypted = tk.Label(frame_output, text="Zaszyfrowany tekst:")
label_encrypted.grid(row=0, column=0)

entry_encrypted = tk.Entry(frame_output)
entry_encrypted.grid(row=0, column=1)

frame_output_decrypt = tk.Frame(root)
frame_output_decrypt.pack(pady=10)

label_decrypted = tk.Label(frame_output_decrypt, text="Odszyfrowany tekst:")
label_decrypted.grid(row=0, column=0)

entry_decrypted = tk.Entry(frame_output_decrypt)
entry_decrypted.grid(row=0, column=1)

root.mainloop()
