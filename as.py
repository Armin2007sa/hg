import random
import tkinter as tk
from tkinter import filedialog

def generate_uid(username):
    uid = username + str(random.randint(10000, 99999))
    return uid + str(random.randint(100000000, 999999999))

def generate_lot():
    letters = [chr(random.randint(65, 90)) for _ in range(3)]
    digits = [str(random.randint(0, 9)) for _ in range(6)]
    return ''.join(letters) + ''.join(digits)

def generate_exp_date():
    exp_date = exp_entry.get()
    return exp_date

def generate_code():
    code = ''.join(str(random.randint(0, 9)) for _ in range(20))
    return code

def print_receipt():
    num_prints = int(num_entry.get())
    username = username_entry.get()

    receipt_list = []

    for _ in range(num_prints):
        uid = generate_uid(username)
        lot = generate_lot()
        code = generate_code()
        gtn = str(random.randint(10000000000000, 99999999999999))

        receipt = f"GTN: {gtn}\nUID: {uid}\nLot: {lot}\nEXP: {generate_exp_date()}\nCode: {code}"
        receipt_list.append(receipt)

    formatted_receipts = '\n\n******************************\n\n'.join(receipt_list)
    receipt_label = tk.Label(root, text=formatted_receipts)
    receipt_label.pack()

    
    save_path = filedialog.asksaveasfilename(defaultextension=".txt")

    if save_path:
        with open(save_path, "w") as file:
            file.write(formatted_receipts)

root = tk.Tk()
root.title("Receipt Generator")

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

num_label = tk.Label(root, text="Number of prints:")
num_label.pack()
num_entry = tk.Entry(root)
num_entry.pack()

exp_label = tk.Label(root, text="Expiration date (EXP):")
exp_label.pack()
exp_entry = tk.Entry(root)
exp_entry.pack()

submit_button = tk.Button(root, text="Submit", command=print_receipt)
submit_button.pack()

root.mainloop()
