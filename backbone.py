import random
import logging
from tkinter import Tk, Label, Button, Entry


class RPSBackBone:
    """Class to implement rock paper scissors logic"""

    def __init__(self) -> None:
        self.choices = ("Rock", "Paper", "Scissors")
        # Dictionary to compute outcome. Outer key is computer's choice,
        # inner key is human's choice, inner value is outcome
        self.outcome = {
            "Rock": {"Rock": "Tied", "Paper": "Won", "Scissors": "Failed"},
            "Paper": {"Rock": "Failed", "Paper": "Tied", "Scissors": "Won"},
            "Scissors": {"Rock": "Won", "Paper": "Failed", "Scissors": "Tied"},
        }
        self.computer_choice = None
        self.human_choice = None

    def choose_for_computer(self) -> None:
        """Randomly chooses Rock/Paper/Scissors for computer"""
        self.computer_choice = random.choice(self.choices)
        return self.computer_choice

    def human_chooses(self, human_choice: str = None) -> None:
        """Registers human's choice"""
        self.human_choice = human_choice

    def result(self) -> str:
        """Returns outcome & choices"""
        return (
            self.outcome.get(self.computer_choice).get(self.human_choice),
            self.computer_choice,
            self.human_choice,
        )


if __name__ == "__main__":
    rps = RPSBackBone()
    while True:
        rps.choose_for_computer()
        choice = input("Rock, Paper, Scissors: ")
        if choice in rps.choices:
            rps.human_chooses(choice)
            result, c_choice, h_choice = rps.result()
            print(f"Computer: {c_choice}, You: {h_choice}, Result: You {result}")
        else:
            break
