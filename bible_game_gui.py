import random
import tkinter as tk
from tkinter import messagebox

old_testament_books = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
    "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel",
    "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra",
    "Nehemiah", "Esther", "Job", "Psalm", "Proverbs",
    "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah", "Lamentations",
    "Ezekiel", "Daniel", "Hosea", "Joel", "Amos",
    "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk",
    "Zephaniah", "Haggai", "Zechariah", "Malachi"
]

new_testament_books = [
    "Matthew", "Mark", "Luke", "John", "Acts",
    "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians",
    "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy",
    "2 Timothy", "Titus", "Philemon", "Hebrews", "James",
    "1 Peter", "2 Peter", "1 John", "2 John", "3 John",
    "Jude", "Revelation"
]

def shuffle_book(book):
    return "".join(random.sample(book, len(book)))

def categorize_testament(book):
    if book in old_testament_books:
        return "Old Testament"
    elif book in new_testament_books:
        return "New Testament"
    else:
        return "Unknown Testament"

class BibleGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bible Game")

        self.label = tk.Label(root, text="Welcome to the Bible Book Game!")
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        self.rounds_played = 0
        self.score = 0
        self.skips_used = 0
        self.current_book = ""

    def start_game(self):
        if self.rounds_played < 10:
            self.rounds_played += 1
            self.label.config(text=f"Round {self.rounds_played}: Unscramble the following Bible book:")

            # Shuffle books for the game
            all_books = old_testament_books + new_testament_books
            self.current_book = random.choice(all_books)
            shuffled_book = shuffle_book(self.current_book)

            self.display_text = f"Unscramble: {shuffled_book}"

            self.text_label = tk.Label(self.root, text=self.display_text)
            self.text_label.pack(pady=10)

            self.entry = tk.Entry(self.root)
            self.entry.pack(pady=10)

            self.submit_button = tk.Button(self.root, text="Submit", command=self.check_guess)
            self.submit_button.pack(pady=10)

            self.skip_button = tk.Button(self.root, text="Skip", command=self.skip_scramble)
            self.skip_button.pack(pady=10)
        else:
            self.end_game()

    def check_guess(self):
        player_guess = self.entry.get()

        if player_guess.lower() == self.current_book.lower():
            messagebox.showinfo("Congratulations", "You guessed it correctly!")
            testament_guess = messagebox.askquestion("Categorize", f"Is '{self.current_book}' from the Old or New Testament?", icon='question', type='yesno', detail="Old-yes\nNew-no")

            if testament_guess.lower() == 'yes':
                testament_guess = 'Old Testament'
            elif testament_guess.lower() == 'no':
                testament_guess = 'New Testament'

            if testament_guess.lower() == categorize_testament(self.current_book).lower():
                messagebox.showinfo("Correct", f"Correct! '{self.current_book}' is from the {categorize_testament(self.current_book)}.")
                self.score += 1
            else:
                messagebox.showinfo("Incorrect", f"Sorry, '{self.current_book}' is from the {categorize_testament(self.current_book)}.")
            self.reset_game()
        else:
            messagebox.showinfo("Incorrect", f"Sorry, that's incorrect. The correct answer is: {self.current_book}")
            self.reset_game()

    def skip_scramble(self):
        if self.skips_used < 2:
            self.skips_used += 1
            messagebox.showinfo("Skip", "You skipped this scramble. Try the next one.")
            self.reset_game()
        else:
            messagebox.showinfo("No More Skips", "You've used all your skips for this game.")

    def reset_game(self):
        self.text_label.destroy()
        self.entry.destroy()
        self.submit_button.destroy()
        self.skip_button.destroy()
        self.start_game()

    def end_game(self):
        messagebox.showinfo("Game Over", f"Game Over! Your score is {self.score}/10.")

if __name__ == "__main__":
    root = tk.Tk()
    game = BibleGameGUI(root)
    root.mainloop()
