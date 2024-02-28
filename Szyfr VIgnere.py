import tkinter as tk
from tkinter import messagebox

def encrypt_vigenere(plaintext, key):
    encrypted_text = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_vigenere(ciphertext, key):
    decrypted_text = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_text():
    plaintext = entry_plaintext.get()
    key = entry_key.get()
    encrypted_text = encrypt_vigenere(plaintext, key)
    messagebox.showinfo("Zaszyfrowany tekst", encrypted_text)
    root.clipboard_clear()
    root.clipboard_append(encrypted_text)

def decrypt_text():
    ciphertext = entry_ciphertext.get()
    key = entry_key_decrypt.get()
    decrypted_text = decrypt_vigenere(ciphertext, key)
    messagebox.showinfo("Odszyfrowany tekst", decrypted_text)
    root.clipboard_clear()
    root.clipboard_append(decrypted_text)

root = tk.Tk()
root.title("Szyfr Vigenère")

frame_encrypt = tk.Frame(root)
frame_encrypt.pack(pady=10)

label_plaintext = tk.Label(frame_encrypt, text="Tekst jasny:")
label_plaintext.grid(row=0, column=0)

entry_plaintext = tk.Entry(frame_encrypt)
entry_plaintext.grid(row=0, column=1)

label_key = tk.Label(frame_encrypt, text="Klucz:")
label_key.grid(row=1, column=0)

entry_key = tk.Entry(frame_encrypt)
entry_key.grid(row=1, column=1)

frame_encrypt_buttons = tk.Frame(root)
frame_encrypt_buttons.pack(pady=5)

button_encrypt = tk.Button(frame_encrypt_buttons, text="Zaszyfruj", command=encrypt_text)
button_encrypt.grid(row=0, column=0, padx=5)

frame_separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
frame_separator.pack(fill=tk.X, padx=5, pady=5)

frame_decrypt = tk.Frame(root)
frame_decrypt.pack(pady=10)

label_ciphertext = tk.Label(frame_decrypt, text="Tekst zaszyfrowany:")
label_ciphertext.grid(row=0, column=0)

entry_ciphertext = tk.Entry(frame_decrypt)
entry_ciphertext.grid(row=0, column=1)

label_key_decrypt = tk.Label(frame_decrypt, text="Klucz:")
label_key_decrypt.grid(row=1, column=0)

entry_key_decrypt = tk.Entry(frame_decrypt)
entry_key_decrypt.grid(row=1, column=1)

frame_decrypt_buttons = tk.Frame(root)
frame_decrypt_buttons.pack(pady=5)

button_decrypt = tk.Button(frame_decrypt_buttons, text="Odszyfruj", command=decrypt_text)
button_decrypt.grid(row=0, column=0, padx=5)

root.mainloop()
