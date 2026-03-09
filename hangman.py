import tkinter as tk
from tkinter import messagebox
import random

class Hangman:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman")
        self.word_list = ['python', 'java', 'hangman', 'tkinter', 'code']
        self.secret_word = random.choice(self.word_list)
        self.guesses = []
        self.max_attempts = 6
        self.attempts = 0

        self.label_word = tk.Label(master, text=self.display_word(), font=("Helvetica", 24))
        self.label_word.pack(pady=20)

        self.entry_guess = tk.Entry(master)
        self.entry_guess.pack(pady=20)

        self.button_guess = tk.Button(master, text="Guess", command=self.check_guess)
        self.button_guess.pack(pady=20)

        self.label_attempts = tk.Label(master, text=f"Attempts left: {self.max_attempts - self.attempts}")
        self.label_attempts.pack(pady=20)

    def display_word(self):
        displayed = [letter if letter in self.guesses else '_' for letter in self.secret_word]
        return ' '.join(displayed)

    def check_guess(self):
        guess = self.entry_guess.get().lower()  
        self.entry_guess.delete(0, tk.END)
        if guess in self.guesses:
            messagebox.showinfo("Info", "You already guessed that letter.")
            return
        if guess in self.secret_word:
            self.guesses.append(guess)
            if all(letter in self.guesses for letter in self.secret_word):
                messagebox.showinfo("Win!", "Congratulations, you've won!")
                self.master.quit()
        else:
            self.attempts += 1
            if self.attempts >= self.max_attempts:
                messagebox.showinfo("Game Over", f"The word was '{self.secret_word}'.")
                self.master.quit()
        self.label_word.config(text=self.display_word())
        self.label_attempts.config(text=f"Attempts left: {self.max_attempts - self.attempts}")

if __name__ == '__main__':
    root = tk.Tk()
    game = Hangman(root)
    root.mainloop()