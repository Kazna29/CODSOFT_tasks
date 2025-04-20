import customtkinter as ctk

def update_display(value):
    current = display.get()
    if current == "0" or current == "Error":
        display.set(value)
    else:
        display.set(current + value)

def clear():
    display.set("0")

def backspace():
    current = display.get()
    display.set(current[:-1] if len(current) > 1 else "0")

def calculate():
    try:
        result = eval(display.get())
        display.set(str(result))
    except Exception:
        display.set("Error")

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("360x520")
app.title("Modern Calculator")

display = ctk.StringVar(value="0")
entry = ctk.CTkEntry(app, textvariable=display, font=("Arial", 28), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")

# Color palette
digit_color = "#000000"
operation_color = "#2c2c2c"
special_color = "#cc7722"

# Row 1: C and ⌫ (2-column span each)
ctk.CTkButton(app, text="C", font=("Arial", 20), command=clear,
              fg_color=special_color, hover_color=special_color, text_color="white").grid(
    row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

ctk.CTkButton(app, text="⌫", font=("Arial", 20), command=backspace,
              fg_color=special_color, hover_color=special_color, text_color="white").grid(
    row=1, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# Correct layout: digits and operations
buttons = [
    (2, 0, "7", digit_color), (2, 1, "8", digit_color), (2, 2, "9", digit_color), (2, 3, "/", operation_color),
    (3, 0, "4", digit_color), (3, 1, "5", digit_color), (3, 2, "6", digit_color), (3, 3, "*", operation_color),
    (4, 0, "1", digit_color), (4, 1, "2", digit_color), (4, 2, "3", digit_color), (4, 3, "-", operation_color),
    (5, 0, "0", digit_color), (5, 1, ".", digit_color), (5, 2, "=", operation_color), (5, 3, "+", operation_color),
]

for row, col, label, color in buttons:
    cmd = calculate if label == "=" else lambda val=label: update_display(val)
    ctk.CTkButton(app, text=label, font=("Arial", 20), command=cmd,
                  fg_color=color, hover_color=color, text_color="white").grid(
        row=row, column=col, padx=5, pady=5, sticky="nsew")

# Make layout responsive
for i in range(4):
    app.grid_columnconfigure(i, weight=1)
for i in range(6):
    app.grid_rowconfigure(i, weight=1)

app.mainloop()
