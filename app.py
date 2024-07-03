import logging
import time
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from backbone import RPSBackBone


class RockPaperScissorsApp:
    """GUI app for Rock Paper Scissor"""

    def __init__(self) -> None:
        """Create root window and place widgets"""
        self.root_window = tb.Window(themename="lumen")
        self.set_root_window_parameters()
        self.create_widgets()
        self.place_widgets()
        self.rock_paper_scissors = RPSBackBone()

    def set_root_window_parameters(self) -> None:
        self.root_window.title("Rock Paper Scissors")
        # self.root_window.iconbitmap("./images/icon.ico")
        self.root_window.geometry("640x200")

    def create_widgets(self) -> None:
        """Function to create widgets in root window"""
        self.computer_label = tb.Label(
            self.root_window,
            text="Computer's choice",
            bootstyle="default",
        )
        self.human_label = tb.Label(
            self.root_window,
            text="Your choice",
            bootstyle="default",
        )
        self.computer_choice_label = tb.Label(
            self.root_window, text="Rock", bootstyle="default"
        )
        self.human_choice_label = tb.Label(
            self.root_window, text="Rock", bootstyle="default"
        )
        self.outcome_label = tb.Label(
            self.root_window,
            text="Let's play",
            bootstyle="default",
        )
        self.rock_button = tb.Button(
            self.root_window,
            text="Rock",
            command=lambda: self.user_plays("Rock"),
            bootstyle="primary",
        )
        self.paper_button = tb.Button(
            self.root_window,
            text="Paper",
            command=lambda: self.user_plays("Paper"),
            bootstyle="primary",
        )
        self.scissors_button = tb.Button(
            self.root_window,
            text="Scissors",
            command=lambda: self.user_plays("Scissors"),
            bootstyle="primary",
        )
        self.exit_button = tb.Button(
            self.root_window, text="Exit", command=self.close, bootstyle="danger"
        )

    def place_widgets(self) -> None:
        """Function to place widgets in grid layout"""
        label_width1 = 33
        button_width1 = 20
        self.computer_label.grid(row=0, column=0, padx=10, pady=10, sticky="we")
        self.computer_label.configure(width=label_width1)
        self.human_label.grid(row=0, column=2)
        self.human_label.configure(width=label_width1)
        self.computer_choice_label.grid(row=1, column=0)
        self.human_choice_label.grid(row=1, column=2)
        self.outcome_label.grid(row=2, column=1)
        self.rock_button.grid(row=3, column=0)
        self.rock_button.configure(width=button_width1)
        self.paper_button.grid(row=3, column=1)
        self.paper_button.configure(width=button_width1)
        self.scissors_button.grid(row=3, column=2, pady=10)
        self.scissors_button.configure(width=button_width1)
        self.exit_button.grid(row=4, column=2)
        self.exit_button.configure(width=10)

    def user_plays(self, user_choice: str) -> None:
        """Callback function when user clicks a tb.Button (Rock/Paper/Scissors)"""
        self.rock_paper_scissors.choose_for_computer()
        self.rock_paper_scissors.human_chooses(user_choice)
        result, c_choice, h_choice = self.rock_paper_scissors.result()
        outcome = f"You {result}"
        self.computer_choice_label.configure(text=c_choice)
        self.human_choice_label.configure(text=h_choice)
        self.outcome_label.configure(text=outcome)

    def run(self) -> None:
        self.root_window.mainloop()

    def close(self) -> None:
        self.root_window.destroy()


if __name__ == "__main__":
    app = RockPaperScissorsApp()
    app.run()
