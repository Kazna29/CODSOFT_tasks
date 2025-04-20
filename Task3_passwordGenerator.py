import random
import string
import customtkinter as ctk

# Set appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Updated size and maximize
        self.root.geometry("600x650")  # Increased default size
        self.root.update_idletasks()
        self.root.state("zoomed")  # Maximizes the window (Windows only)
        self.root.resizable(True, True)

        # Character sets
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.numbers = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

        # Create the UI
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = ctk.CTkLabel(
            self.root, 
            text="Password Generator", 
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title_label.pack(pady=(30, 20))

        # Main frame
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(padx=30, pady=20, fill="both", expand=True)

        # Password length section
        length_label = ctk.CTkLabel(
            main_frame,
            text="Password Length:",
            font=ctk.CTkFont(size=16)
        )
        length_label.pack(pady=(20, 5), anchor="w")

        self.length_var = ctk.IntVar(value=12)
        self.length_slider = ctk.CTkSlider(
            main_frame,
            from_=4,
            to=32,
            number_of_steps=28,
            variable=self.length_var,
            command=self.update_length_label
        )
        self.length_slider.pack(fill="x", pady=5)

        self.length_display = ctk.CTkLabel(
            main_frame,
            text="12 characters",
            font=ctk.CTkFont(size=14)
        )
        self.length_display.pack(pady=(0, 15))

        # Password strength section
        strength_label = ctk.CTkLabel(
            main_frame,
            text="Password Strength:",
            font=ctk.CTkFont(size=16)
        )
        strength_label.pack(pady=(10, 5), anchor="w")

        self.strength_var = ctk.StringVar(value="medium")

        strength_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        strength_frame.pack(fill="x", pady=5)

        strengths = [
            ("Low (Numbers Only)", "low"),
            ("Medium (Letters + Numbers)", "medium"),
            ("High (Letters + Numbers + Symbols)", "high")
        ]

        for text, value in strengths:
            radio = ctk.CTkRadioButton(
                strength_frame,
                text=text,
                value=value,
                variable=self.strength_var,
                font=ctk.CTkFont(size=14)
            )
            radio.pack(anchor="w", pady=5)

        generate_button = ctk.CTkButton(
            main_frame,
            text="Generate Password",
            command=self.generate_password,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#2E8B57",
            hover_color="#3CB371"
        )
        generate_button.pack(pady=20)

        password_label = ctk.CTkLabel(
            main_frame,
            text="Your Password:",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        password_label.pack(pady=(15, 5), anchor="w")

        self.password_var = ctk.StringVar(value="")
        self.password_display = ctk.CTkEntry(
            main_frame,
            textvariable=self.password_var,
            font=ctk.CTkFont(size=16, family="Courier"),
            justify="center",
            height=45,
            fg_color="#222222",
            text_color="#00FF00",
            border_color="#555555",
            state="readonly"
        )
        self.password_display.pack(fill="x", pady=10)

        copy_button = ctk.CTkButton(
            main_frame,
            text="Copy to Clipboard",
            command=self.copy_to_clipboard,
            height=35,
            font=ctk.CTkFont(size=14),
            fg_color="#4169E1",
            hover_color="#1E90FF"
        )
        copy_button.pack(pady=10)

        # Generate initial password
        self.generate_password()

    def update_length_label(self, value=None):
        length = self.length_var.get()
        self.length_display.configure(text=f"{length} characters")

    def generate_password(self):
        length = self.length_var.get()
        strength = self.strength_var.get()

        if strength == "low":
            char_pool = self.numbers
        elif strength == "medium":
            char_pool = self.lowercase + self.uppercase + self.numbers
        else:
            char_pool = self.lowercase + self.uppercase + self.numbers + self.symbols

        password = ''.join(random.choice(char_pool) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)

            original_fg = self.password_display.cget("fg_color")
            self.password_display.configure(fg_color="#004400")
            self.root.after(200, lambda: self.password_display.configure(fg_color=original_fg))

if __name__ == "__main__":
    root = ctk.CTk()
    app = PasswordGenerator(root)
    root.mainloop()
