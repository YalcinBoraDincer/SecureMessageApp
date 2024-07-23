from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import base64
import hashlib

window = Tk()
window.title("Cryptology")
window.geometry('400x700')


def show_warning(message):
    messagebox.showwarning("Warning", message)


def show_info(message):
    messagebox.showinfo("Info", message)


def password_to_key(inputkey):
    digest = hashlib.sha256(inputkey.encode()).digest()
    key = base64.urlsafe_b64encode(digest)
    return key


def resize_image(image, size):
    return image.subsample(int(image.width() // size[0]), int(image.height() // size[1]))


def encrypt_message(key, message):
    try:
        if message == '':
            show_warning('The message is empty.')
            return None

        fernet = Fernet(key)
        encrypted = fernet.encrypt(message.encode())
        return encrypted

    except ValueError as ve:
        show_warning(f"ValueError: {ve}")
    except Exception as e:
        show_warning(f"An error occurred: {e}")


def decrypt_message(key, encrypted_message):
    try:
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_message).decode()
        return decrypted
    except Exception as e:
        show_warning(f"Decryption error: {e}")
        return None


def file_writing():
    try:
        user_input = secret_textbox.get("1.0", END).strip()
        user_key = password_entry.get()

        if not user_input:
            show_warning("Please enter a message.")
            return

        if not user_key:
            show_warning("Please enter a key.")
            return

        key = password_to_key(user_key)
        encrypted_user_input = encrypt_message(key, user_input)

        if encrypted_user_input is None:
            return

        with open("test.txt", 'a') as f:
            f.write(f"{title_entry.get()} : \n{encrypted_user_input.decode()}\n")

    except ValueError as ve:
        show_warning(f"ValueError: {ve}")
    except Exception as e:
        show_warning(f"An error occurred: {e}")


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
    try:
        user_key = password_entry.get()

        if not user_key:
            show_warning("Please enter a key.")
            return

        key = password_to_key(user_key)
        encrypted_message = secret_textbox.get("1.0", END).strip().encode()

        decrypted_message = decrypt_message(key, encrypted_message)

        if decrypted_message is None:
            return

        secret_textbox.delete("1.0", END)
        secret_textbox.insert("1.0", decrypted_message)

    except ValueError as ve:
        messagebox.showerror("Error", f"ValueError: {ve}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


decrypt_button = Button(text="Decrypt", font=("Arial", 10, "bold"), command=decrypt)
decrypt_button.pack(pady=5)

window.mainloop()
