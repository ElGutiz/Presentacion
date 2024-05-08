# level_1 = 3145 #1,000
# level_2 = 1363 #10,000
# level_3 = 123 #50,000
# level_4 = 96  #150,000
# level_5 = 5   #500,000

# ans = (1000 * level_1) + (10000 * level_2) + (50000 * level_3) + (150000 * level_4) + (500000 * level_5)

# print(f"{ans:,d}")


# # level_1 = 2543 #750
# # level_2 = 1438 #7,500
# # level_3 = 88   #150,000
# # level_4 = 0   #500,000

# # ans = (750 * level_1) + (7500 * level_2) + (37500 * level_3) + (500000 * level_4)

# # print(f"{ans:,d}")


import tkinter as tk
from tkinter import ttk, messagebox

def update_labels(*args):
    operation = operation_cb.get()
    if operation == 'Oro' or operation == 'Madera':
        label1.config(text="Objetos de 1,000:")
        label2.config(text="Objetos de 10,000:")
        label3.config(text="Objetos de 50,000:")
        label4.config(text="Objetos de 150,000:")
        label5.config(text="Objetos de 500,000:")

    elif operation == 'Mineral':
        label1.config(text="Objetos de 750:")
        label2.config(text="Objetos de 7,500:")
        label3.config(text="Objetos de 37,500:")
        label4.config(text="Objetos de 112,500:")
        label5.config(text="Objetos de 375,000:")

    elif operation == 'Maná':
        label1.config(text="Objetos de 500:")
        label2.config(text="Objetos de 3,000:")
        label3.config(text="Objetos de 15,000:")
        label4.config(text="Objetos de 50,000:")
        label5.config(text="Objetos de 200,000:")

def calculate():
    try:
        # Retrieve and convert values
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        num3 = int(entry3.get())
        num4 = int(entry4.get())
        num5 = int(entry5.get())

        # Get the selected operation
        operation = operation_cb.get()

        # Perform calculation based on the selected operation
        if operation == 'Oro' or operation == 'Madera':
            result = (1000 * num1) + (10000 * num2) + (50000 * num3) + (150000 * num4) + (500000 * num5)
        elif operation == 'Mineral':
            result = (750 * num1) + (7500 * num2) + (37500 * num3) + (112500 * num4) + (375000 * num5)
        elif operation == 'Maná':
            result = (500 * num1) + (3000 * num2) + (15000 * num3) + (50000 * num4) + (200000 * num5)
        else:
            messagebox.showerror("Error", "Invalid operation selected")
            return

        # Display the result using a messagebox
        messagebox.showinfo("Result", f"El numero de materiales a recibir es: {result:,d}")
    except ValueError:
        # Error handling for non-numeric input
        messagebox.showerror("Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Calculator with Operations")

# Combobox for selecting the operation
operations = ['Oro', 'Madera', 'Mineral', 'Maná']
operation_cb = ttk.Combobox(root, values=operations, state="readonly")
operation_cb.grid(row=0, column=1, padx=10, pady=10)
operation_cb.set("Oro")  # set default value
operation_cb.bind('<<ComboboxSelected>>', update_labels)

# Label for combobox
operation_label = tk.Label(root, text="Select operation:")
operation_label.grid(row=0, column=0)

# Create and grid the entry widgets
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1, padx=10, pady=10)
entry1.insert(0, 0)

entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, padx=10, pady=10)
entry2.insert(0, 0)

entry3 = tk.Entry(root)
entry3.grid(row=3, column=1, padx=10, pady=10)
entry3.insert(0, 0)

entry4 = tk.Entry(root)
entry4.grid(row=4, column=1, padx=10, pady=10)
entry4.insert(0, 0)

entry5 = tk.Entry(root)
entry5.grid(row=5, column=1, padx=10, pady=10)
entry5.insert(0, 0)

# Labels for the entry widgets
label1 = tk.Label(root, text="Objetos de 1,000:")
label1.grid(row=1, column=0)

label2 = tk.Label(root, text="Objetos de 10,000:")
label2.grid(row=2, column=0)

label3 = tk.Label(root, text="Objetos de 50,000:")
label3.grid(row=3, column=0)

label4 = tk.Label(root, text="Objetos de 150,000:")
label4.grid(row=4, column=0)

label5 = tk.Label(root, text="Objetos de 500,000:")
label5.grid(row=5, column=0)

# Button to trigger calculation
calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=6, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()


