from tkinter import *
from cryptography.fernet import Fernet

window = Tk()
window.title("Cryptology")
window.geometry('400x1000')

key = Fernet.generate_key()
print(f"Key: {key.decode()}")


def resize_image(image, size):
    return image.subsample(int(image.width() // size[0]), int(image.height() // size[1]))


def encrypt_message(key, message):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    print(encrypted)
    return encrypted


def decrypt_message(key, encrypted_message):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message).decode()
    return print(decrypted)


'''def encrypt_user_text():
    user_input_secret = secret_textbox.get("1.0", END)
    user_key = password_entry.get()
    
    encrypted_user_input = encrypt_message(key, user_input_secret)
    return encrypted_user_input'''
def file_writing():
    with open("test.txt", 'a') as f:
        user_input = secret_textbox.get("1.0", END).strip()
        encrypted_user_input = encrypt_message(key, user_input)
        f.write(f"{title_entry.get()} : \n{encrypted_user_input.decode()}\n")










#Image
img = PhotoImage(file='image.png')
resized_image = resize_image(img, (100, 100))
img_label = Label(window, image=resized_image)
img_label.pack(pady=20)

#Widgets
title_label = Label(text="Enter Your Title", font=("Arial", 12, "bold"))
title_entry = Entry()
secret_label = Label(text="Enter Secret", font=("Arial", 12, "bold"))
secret_textbox = Text(width=30, height=30)
password_label = Label(text="Enter Your Master Key", font=("Arial", 12, "bold"))
password_entry = Entry()
save_encrypt_button = Button(text="Save & Encrypt", font=("Arial", 10, "bold"),command=file_writing )
decrypt_button = Button(text="Decrypt", font=("Arial", 10, "bold"),)

title_label.pack(pady=10)
title_entry.pack(pady=5)
secret_label.pack(pady=10)
secret_textbox.pack(pady=10)
password_label.pack(pady=10)
password_entry.pack(pady=5)
save_encrypt_button.pack(pady=20)
decrypt_button.pack(pady=5)
data = encrypt_message(key, 'Bora')
decrypt_message(key, data)



window.mainloop()
