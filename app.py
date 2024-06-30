import logging
from tkinter import Tk, Label, Button, Entry
import time


class RockPaperScissorsApp:
    """GUI app for Rock Paper Scissor"""

    def __init__(self) -> None:
        """Create root window and place widgets"""
        self.root_window = Tk()
        self.create_widgets()
        self.place_widgets()

    def create_widgets(self) -> None:
        """Function to create widgets in root window"""
        self.computer_choice_label = Label(self.root_window, text="Rock")
        self.human_choice_label = Label(self.root_window, text="Rock")
        self.outcome_label = Label(self.root_window, text="Outcome")
        self.rock_button = Button(self.root_window, text="Rock")
        self.paper_button = Button(self.root_window, text="Paper")
        self.scissors_button = Button(self.root_window, text="Scissors")
        self.exit_button = Button(self.root_window, text="Exit", command=self.close)

    def place_widgets(self) -> None:
        """Function to place widgets in grid layout"""
        self.computer_choice_label.grid(row=0, column=0)
        self.human_choice_label.grid(row=0, column=1)
        self.outcome_label.grid(row=0, column=2)
        self.rock_button.grid(row=1, column=0)
        self.paper_button.grid(row=1, column=1)
        self.scissors_button.grid(row=1, column=2)
        self.exit_button.grid(row=2, column=2)

    def run(self) -> None:
        self.root_window.mainloop()

    def close(self) -> None:
        self.root_window.destroy()


if __name__ == "__main__":
    app = RockPaperScissorsApp()
    app.run()
