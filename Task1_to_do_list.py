import customtkinter as ctk
from tkinter import messagebox, simpledialog

# Appearance settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Store tasks and their done status
tasks = []

def add_task():
    task_text = task_entry.get().strip()
    if task_text:
        tasks.append({"task": task_text, "done": False})
        update_task_list()
        task_entry.delete(0, ctk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def toggle_task_done():
    # Since we're using a read-only textbox, we'll use a dialog to get the task number
    task_listbox.configure(state="normal")
    task_listbox.configure(state="disabled")

    # Ask user which task to toggle
    try:
        task_num = simpledialog.askinteger("Toggle Task", "Enter task number to mark/unmark:",
                                         minvalue=1, maxvalue=len(tasks))
        if task_num is not None:
            # Adjust for 0-based indexing
            task_index = task_num - 1
            tasks[task_index]["done"] = not tasks[task_index]["done"]
            update_task_list()
    except (ValueError, IndexError):
        messagebox.showwarning("Selection Error", "Invalid task number.")

# This function is defined below with the proper implementation for read-only textbox

def exit_app():
    app.destroy()

# --- GUI Setup ---
app = ctk.CTk()
app.title("Modern To-Do List App")
app.geometry("500x460")
app.configure(fg_color="#1a1a1a")  # Dark background

# Title Label
title_label = ctk.CTkLabel(app, text="TO-DO LIST", font=("Helvetica", 22, "bold"), text_color="#ffffff")
title_label.pack(pady=15)

# Task Entry Field
task_entry = ctk.CTkEntry(app, width=400, height=35, font=("Helvetica", 14),
                          placeholder_text="Enter your task here...",
                          fg_color="#2a2a2a", text_color="#ffffff", border_color="#555555")
task_entry.pack(pady=10)

# Buttons Frame
button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=5)

add_button = ctk.CTkButton(button_frame, text="Add Task", width=120, command=add_task,
                        fg_color="#444444", hover_color="#666666")
add_button.grid(row=0, column=0, padx=5)

done_button = ctk.CTkButton(button_frame, text="✓ Mark/Unmark", width=120, command=toggle_task_done,
                          fg_color="#444444", hover_color="#666666")
done_button.grid(row=0, column=1, padx=5)

exit_button = ctk.CTkButton(button_frame, text="Exit", width=120, command=exit_app,
                          fg_color="#444444", hover_color="#666666")
exit_button.grid(row=0, column=2, padx=5)

# Task Listbox (wrapped inside CTkFrame for style)
listbox_frame = ctk.CTkFrame(app, fg_color="#2a2a2a", corner_radius=10)
listbox_frame.pack(pady=15)

task_listbox = ctk.CTkTextbox(listbox_frame, width=440, height=180, font=("Helvetica", 13),
                              corner_radius=10, wrap="none", state="disabled", fg_color="#2a2a2a",
                              text_color="#ffffff", border_color="#555555")
task_listbox.pack()

# Update the task list in the read-only textbox
def update_task_list():
    task_listbox.configure(state="normal")  # Temporarily enable editing
    task_listbox.delete("0.0", ctk.END)  # Clear previous entries
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        task_listbox.insert(ctk.END, f"{idx}. [{status}] {task['task']}\n")
    task_listbox.configure(state="disabled")  # Make read-only again

app.mainloop()
