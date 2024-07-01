import logging
from tkinter import Tk, Label, Button, Entry
import time
from backbone import RPSBackBone


class RockPaperScissorsApp:
    """GUI app for Rock Paper Scissor"""

    def __init__(self) -> None:
        """Create root window and place widgets"""
        self.root_window = Tk()
        self.create_widgets()
        self.place_widgets()
        self.rock_paper_scissors = RPSBackBone()

    def create_widgets(self) -> None:
        """Function to create widgets in root window"""
        self.computer_choice_label = Label(self.root_window, text="Rock")
        self.human_choice_label = Label(self.root_window, text="Rock")
        self.outcome_label = Label(self.root_window, text="Outcome")
        self.rock_button = Button(
            self.root_window, text="Rock", command=lambda: self.user_plays("Rock")
        )
        self.paper_button = Button(
            self.root_window, text="Paper", command=lambda: self.user_plays("Paper")
        )
        self.scissors_button = Button(
            self.root_window,
            text="Scissors",
            command=lambda: self.user_plays("Scissors"),
        )
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

    def user_plays(self, user_choice: str) -> None:
        """Callback function when user clicks a button (Rock/Paper/Scissors)"""
        self.rock_paper_scissors.choose_for_computer()
        self.rock_paper_scissors.human_chooses(user_choice)
        result, c_choice, h_choice = self.rock_paper_scissors.result()
        outcome = f"You {result}"
        self.computer_choice_label.config(text=c_choice)
        self.human_choice_label.config(text=h_choice)
        self.outcome_label.config(text=outcome)

    def run(self) -> None:
        self.root_window.mainloop()

    def close(self) -> None:
        self.root_window.destroy()


if __name__ == "__main__":
    app = RockPaperScissorsApp()
    app.run()
