from tkinter import *
from cryptography.fernet import Fernet
import base64
import hashlib

window = Tk()
window.title("Cryptology")
window.geometry('400x600')


def password_to_key(inputkey):
    digest = hashlib.sha256(inputkey.encode()).digest()
    key = base64.urlsafe_b64encode(digest)
    return key


def resize_image(image, size):
    return image.subsample(int(image.width() // size[0]), int(image.height() // size[1]))


def encrypt_message(key, message):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    if message == '':
        print('Enter the value')
    else:
        return encrypted


def decrypt_message(key, encrypted_message):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message).decode()
    return decrypted


def file_writing():
    with open("test.txt", 'a') as f:
        user_input = secret_textbox.get("1.0", END).strip()
        user_key = password_entry.get()
        key = password_to_key(user_key)
        encrypted_user_input = encrypt_message(key, user_input)
        f.write(f"{title_entry.get()} : \n{encrypted_user_input.decode()}\n")


# Image
img = PhotoImage(file='image.png')
resized_image = resize_image(img, (100, 100))
img_label = Label(window, image=resized_image)
img_label.pack(pady=20)

# Widgets
title_label = Label(text="Enter Your Title", font=("Arial", 12, "bold"))
title_entry = Entry()
secret_label = Label(text="Enter Secret", font=("Arial", 12, "bold"))
secret_textbox = Text(width=30, height=10)
password_label = Label(text="Enter Your Master Key", font=("Arial", 12, "bold"))
password_entry = Entry()
save_encrypt_button = Button(text="Save & Encrypt", font=("Arial", 10, "bold"), command=file_writing)

title_label.pack(pady=10)
title_entry.pack(pady=5)
secret_label.pack(pady=10)
secret_textbox.pack(pady=10)
password_label.pack(pady=10)
password_entry.pack(pady=5)
save_encrypt_button.pack(pady=20)


def decrypt():
    user_key = password_entry.get()
    key = password_to_key(user_key)
    encrypted_message = secret_textbox.get("1.0", END).strip().encode()
    decrypted_message = decrypt_message(key, encrypted_message)
    secret_textbox.delete("1.0", END)
    secret_textbox.insert("1.0", decrypted_message)


decrypt_button = Button(text="Decrypt", font=("Arial", 10, "bold"), command=decrypt)
decrypt_button.pack(pady=5)

window.mainloop()
