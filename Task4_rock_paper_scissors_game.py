import customtkinter as ctk
import random

# Initialize customtkinter
ctk.set_appearance_mode("System")

# Game ASCII Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]

# Main App
app = ctk.CTk()
app.geometry("600x600")
app.title("Rock Paper Scissors")

# Result Label
result_label = ctk.CTkLabel(app, text="Choose Rock, Paper or Scissors", font=("Arial", 18))
result_label.pack(pady=20)

# Display Area
user_display = ctk.CTkLabel(app, text="", font=("Courier", 12), justify="left")
user_display.pack(pady=10)

computer_display = ctk.CTkLabel(app, text="", font=("Courier", 12), justify="left")
computer_display.pack(pady=10)

# Outcome Label
outcome_label = ctk.CTkLabel(app, text="", font=("Arial", 18, "bold"))
outcome_label.pack(pady=20)

def play(user_choice):
    computer_choice = random.randint(0, 2)

    user_display.configure(text=f"You chose:\n{game_images[user_choice]}")
    computer_display.configure(text=f"Computer chose:\n{game_images[computer_choice]}")

    if user_choice == computer_choice:
        outcome = "It's a draw!!!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        outcome = "You won!"
    else:
        outcome = "You lose!"

    outcome_label.configure(text=outcome)

# Buttons for Choices
btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=10)

rock_btn = ctk.CTkButton(btn_frame, text="Rock", command=lambda: play(0), width=100)
paper_btn = ctk.CTkButton(btn_frame, text="Paper", command=lambda: play(1), width=100)
scissors_btn = ctk.CTkButton(btn_frame, text="Scissors", command=lambda: play(2), width=100)

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

# Run App
app.mainloop()
