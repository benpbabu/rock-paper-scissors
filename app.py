import logging
import time
from PIL import ImageTk, Image
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from backbone import RPSBackBone


class RockPaperScissorsApp:
    """GUI app for Rock Paper Scissor"""

    def __init__(self) -> None:
        """Create root window and place widgets"""
        self.root_window = tb.Window(themename="lumen")
        self.set_root_window_parameters()
        self.load_images()
        self.create_widgets()
        self.place_widgets()
        self.rock_paper_scissors = RPSBackBone()

    def load_images(self):
        self.failed = ImageTk.PhotoImage(Image.open("images/failed.png"))
        self.paper = ImageTk.PhotoImage(Image.open("images/paper.png"))
        self.rock = ImageTk.PhotoImage(Image.open("images/rock.png"))
        self.scissors = ImageTk.PhotoImage(Image.open("images/scissors.png"))
        self.tied = ImageTk.PhotoImage(Image.open("images/tied.png"))
        self.won = ImageTk.PhotoImage(Image.open("images/won.png"))
        self.images = {
            "Won": self.won,
            "Failed": self.failed,
            "Tied": self.tied,
            "Rock": self.rock,
            "Paper": self.paper,
            "Scissors": self.scissors,
        }

    def set_root_window_parameters(self) -> None:
        self.root_window.title("Rock Paper Scissors")
        # self.root_window.iconbitmap("./images/icon.ico")
        self.root_window.geometry("800x540")

    def create_widgets(self) -> None:
        """Function to create widgets in root window"""
        self.computer_label = tb.Label(
            self.root_window,
            text="Computer's choice",
            font=("helvetica", 14),
            justify="center",
            bootstyle="default",
        )
        self.human_label = tb.Label(
            self.root_window,
            text="Your choice",
            font=("helvetica", 14),
            justify="center",
            bootstyle="default",
        )
        self.computer_choice_label = tb.Label(
            self.root_window, image=self.rock, bootstyle="default"
        )
        self.human_choice_label = tb.Label(
            self.root_window, image=self.rock, bootstyle="default"
        )
        self.outcome_label = tb.Label(
            self.root_window,
            image=self.tied,
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

    # def place_widgets(self) -> None:
    #     """Function to place widgets in grid layout"""
    #     label_width1 = 33
    #     button_width1 = 20
    #     self.computer_label.grid(row=0, column=0, padx=30, pady=10)
    #     self.computer_label.configure(width=label_width1)
    #     self.human_label.grid(row=0, column=2)
    #     self.human_label.configure(width=label_width1)
    #     self.computer_choice_label.grid(row=1, column=0)
    #     self.human_choice_label.grid(row=1, column=2)
    #     self.outcome_label.grid(row=1, column=1)
    #     self.rock_button.grid(row=3, column=2, pady=10)
    #     self.rock_button.configure(width=button_width1)
    #     self.paper_button.grid(row=4, column=2, pady=10)
    #     self.paper_button.configure(width=button_width1)
    #     self.scissors_button.grid(row=5, column=2, pady=10)
    #     self.scissors_button.configure(width=button_width1)
    #     self.exit_button.grid(row=6, column=2, pady=20)
    #     self.exit_button.configure(width=10)

    def place_widgets(self) -> None:
        """Function to place widgets in grid layout"""
        # label_width1 = 100
        button_width1 = 150
        button_width2 = 120
        self.computer_label.place(relx=0.2, rely=0.03, anchor="center")
        self.human_label.place(relx=0.8, rely=0.03, anchor="center")
        self.computer_choice_label.place(relx=0.2, rely=0.3, anchor="center")
        self.human_choice_label.place(relx=0.83, rely=0.3, anchor="center")
        self.outcome_label.place(relx=0.5, rely=0.3, anchor="center")
        self.rock_button.place(
            relx=0.83, rely=0.6, anchor="center", width=button_width1
        )
        # self.rock_button.configure(width=button_width1)
        self.paper_button.place(
            relx=0.83, rely=0.7, anchor="center", width=button_width1
        )
        # self.paper_button.configure(width=button_width1)
        self.scissors_button.place(
            relx=0.83, rely=0.8, anchor="center", width=button_width1
        )
        # self.scissors_button.configure(width=button_width1)
        self.exit_button.place(
            relx=0.83, rely=0.9, anchor="center", width=button_width2
        )
        # self.exit_button.configure(width=10)

    def user_plays(self, user_choice: str) -> None:
        """Callback function when user clicks a tb.Button (Rock/Paper/Scissors)"""
        self.rock_paper_scissors.choose_for_computer()
        self.rock_paper_scissors.human_chooses(user_choice)
        result, c_choice, h_choice = self.rock_paper_scissors.result()
        self.computer_choice_label.configure(image=self.images[c_choice])
        self.human_choice_label.configure(image=self.images[h_choice])
        self.outcome_label.configure(image=self.images[result])

    def run(self) -> None:
        self.root_window.mainloop()

    def close(self) -> None:
        self.root_window.destroy()


if __name__ == "__main__":
    app = RockPaperScissorsApp()
    app.run()
