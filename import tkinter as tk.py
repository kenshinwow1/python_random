import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("300x200")

        self.secret_number = random.randint(1, 100)
        self.max_attempts = 5
        self.attempts = 0

        self.label = tk.Label(master, text="Enter your guess:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Guess", command=self.check_guess)
        self.button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        guess = self.entry.get()
        self.entry.delete(0, tk.END)

        try:
            guess = int(guess)
            self.attempts += 1

            if guess == self.secret_number:
                messagebox.showinfo("Congratulations", f"Congratulations! You guessed the number in {self.attempts} attempts.")
                self.master.destroy()
            elif guess < self.secret_number:
                self.result_label.config(text="Too low. Try again.")
            else:
                self.result_label.config(text="Too high. Try again.")

            if self.attempts == self.max_attempts and guess != self.secret_number:
                messagebox.showinfo("Game Over", f"Sorry, you've run out of attempts. The correct number was {self.secret_number}.")
                self.master.destroy()
        
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

def main():
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

