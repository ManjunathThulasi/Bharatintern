import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget to display the input and result
entry = tk.Entry(root, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 20), command=lambda b=button: button_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a clear button
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 20), command=clear).grid(row=row_val, column=col_val)

root.mainloop()






