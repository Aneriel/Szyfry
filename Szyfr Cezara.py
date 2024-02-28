import tkinter as tk

def encrypt(text, shift):
    alphabet = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'
    encrypted_text = ""
    for char in text:
        if char.lower() in alphabet:  
            index = (alphabet.index(char.lower()) + shift) % len(alphabet)
            encrypted_text += alphabet[index]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    alphabet = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'
    decrypted_text = ""
    for char in text:
        if char.lower() in alphabet:
            index = (alphabet.index(char.lower()) - shift) % len(alphabet)
            decrypted_text += alphabet[index]
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_text():
    text = entry_text.get().replace(" ", "")
    shift = int(entry_shift.get())
    encrypted_text = encrypt(text, shift)
    entry_encrypted.delete(0, tk.END)
    entry_encrypted.insert(0, encrypted_text)

def decrypt_text():
    text = entry_text2.get().replace(" ", "")
    shift = int(entry_shift2.get())
    decrypted_text = decrypt(text, shift)
    entry_decrypted.delete(0, tk.END)
    entry_decrypted.insert(0, decrypted_text)

root = tk.Tk()
root.title("Szyfr Cezara")

frame_encrypt = tk.Frame(root)
frame_encrypt.pack(side=tk.LEFT, padx=10)

frame_decrypt = tk.Frame(root)
frame_decrypt.pack(side=tk.RIGHT, padx=10)

# Panel szyfrowania
label_text = tk.Label(frame_encrypt, text="Tekst:")
label_text.grid(row=0, column=0)

entry_text = tk.Entry(frame_encrypt)
entry_text.grid(row=0, column=1)

label_shift = tk.Label(frame_encrypt, text="Przesunięcie:")
label_shift.grid(row=1, column=0)

entry_shift = tk.Entry(frame_encrypt)
entry_shift.grid(row=1, column=1)

button_encrypt = tk.Button(frame_encrypt, text="Zaszyfruj", command=encrypt_text)
button_encrypt.grid(row=2, columnspan=2, pady=5)

label_encrypted = tk.Label(frame_encrypt, text="Zaszyfrowany tekst:")
label_encrypted.grid(row=3, column=0)

entry_encrypted = tk.Entry(frame_encrypt)
entry_encrypted.grid(row=3, column=1)

# Panel deszyfrowania
label_text2 = tk.Label(frame_decrypt, text="Tekst:")
label_text2.grid(row=0, column=0)

entry_text2 = tk.Entry(frame_decrypt)
entry_text2.grid(row=0, column=1)

label_shift2 = tk.Label(frame_decrypt, text="Przesunięcie:")
label_shift2.grid(row=1, column=0)

entry_shift2 = tk.Entry(frame_decrypt)
entry_shift2.grid(row=1, column=1)

button_decrypt = tk.Button(frame_decrypt, text="Odszyfruj", command=decrypt_text)
button_decrypt.grid(row=2, columnspan=2, pady=5)

label_decrypted = tk.Label(frame_decrypt, text="Odszyfrowany tekst:")
label_decrypted.grid(row=3, column=0)

entry_decrypted = tk.Entry(frame_decrypt)
entry_decrypted.grid(row=3, column=1)

root.mainloop()
