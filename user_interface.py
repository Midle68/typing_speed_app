from tkinter import *
from typing_page import TypingPage
from high_scores import HighScores

BACK_GROUND = "#5584AC"
FONT_GROUND = "#F4FFAF"
HEADLINE_FONT = ("Hiragino Sans", 40, "normal")


class UserInterface:
    def __init__(self):
        self.global_frame = None
        self.headline = None
        self.menu_btn = None

    def create_user_interface(self):  # Function to create interface everytime user clicks on smth

        def start_english_hover(e):  # Change start_english_btn img when hover
            start_english_btn["image"] = english_hover
            start_english_btn.image = english_hover

        def start_english_normal(e):  # Change start_english_btn img to normal
            start_english_btn.config(image=english_normal)

        def start_russian_hover(e):  # Change start_russian_btn img when hover

            start_russian_btn["image"] = russian_hover
            start_english_btn.image = russian_hover

        def start_russian_normal(e):  # Change start_russian_btn img to normal
            start_russian_btn.config(image=russian_normal)

        def start_high_scores_hover(e):  # Change start_high_scores_btn img when hover
            high_scores_btn["image"] = high_scores_hover
            high_scores_btn.image = high_scores_hover

        def start_high_scores_normal(e):  # Change start_high_scores_btn img to normal
            high_scores_btn.config(image=high_scores_normal)

        def menu_normal(e):
            self.menu_btn.config(image=menu_normal_img)

        def menu_hover(e):
            self.menu_btn["image"] = menu_hover_img
            self.menu_btn.image = menu_hover_img

        def open_menu():
            root.destroy()
            self.create_user_interface()

        # Options of the window frame
        root = Tk()
        root.title("Typing Speed App")
        root.config(pady=50, padx=100, bg=BACK_GROUND)

        # Global frame where all the elements are placed
        self.global_frame = Frame(root, bg=BACK_GROUND)
        self.global_frame.grid(row=1, column=0, pady=20)

        # Headline of the App
        self.headline = Label(self.global_frame, text="Typing Speed App",
                              font=HEADLINE_FONT, bg=BACK_GROUND, fg=FONT_GROUND)
        self.headline.grid(row=0, column=0, columnspan=2)

        # ----- Buttons ----- #

        # Menu button
        menu_normal_img = PhotoImage(file="./buttons/Menu Normal.png")
        menu_hover_img = PhotoImage(file="./buttons/Menu Hover.png")
        self.menu_btn = Button(self.global_frame, image=menu_normal_img, borderwidth=0, command=open_menu)
        self.menu_btn.grid(row=0, column=2)
        self.menu_btn.bind("<Enter>", menu_hover)
        self.menu_btn.bind("<Leave>", menu_normal)

        # English button
        english_normal = PhotoImage(file="./buttons/Start English Normal.png")
        english_hover = PhotoImage(file="./buttons/Start English Hover.png")
        start_english_btn = Button(self.global_frame, image=english_normal, borderwidth=0,
                                   bg=BACK_GROUND, command=lambda: self.typing_page(language="English"))
        start_english_btn.grid(row=1, column=0)
        start_english_btn.bind("<Enter>", start_english_hover)
        start_english_btn.bind("<Leave>", start_english_normal)

        # Add empty space between 'Start English' & 'Start Russian' btns and 'High Scores' btn
        empty_space = Label(self.global_frame, width=7, height=15, bg=BACK_GROUND)
        empty_space.grid(row=1, column=1)

        # Russian button
        russian_normal = PhotoImage(file="./buttons/Start Russian Normal.png")
        russian_hover = PhotoImage(file="./buttons/Start Russian Hover.png")
        start_russian_btn = Button(self.global_frame, image=russian_normal, borderwidth=0,
                                   bg=BACK_GROUND, command=lambda: self.typing_page(language="Russian"))
        start_russian_btn.grid(row=1, column=2)
        start_russian_btn.bind("<Enter>", start_russian_hover)
        start_russian_btn.bind("<Leave>", start_russian_normal)

        # High score button
        high_scores_normal = PhotoImage(file="./buttons/High Scores Normal.png")
        high_scores_hover = PhotoImage(file="./buttons/High Scores Hover.png")
        high_scores_btn = Button(self.global_frame, image=high_scores_normal, borderwidth=0,
                                 fg=FONT_GROUND, command=self.high_scores_page)
        high_scores_btn.grid(row=2, column=0, columnspan=3)
        high_scores_btn.bind("<Enter>", start_high_scores_hover)
        high_scores_btn.bind("<Leave>", start_high_scores_normal)

        root.mainloop()

    def clear_gui(self):  # Clearing the app window
        widget_list = self.global_frame.winfo_children()
        for i in range(len(widget_list)):
            if i > 1:
                widget_list[i].destroy()

    def typing_page(self, language):  # Open 'typing page' based on the chosen language
        self.clear_gui()
        TypingPage(self.global_frame, language)

    def high_scores_page(self):  # Open the high score page with 10 best scores for each language
        self.clear_gui()
        self.headline.grid(columnspan=14, pady=10)
        self.menu_btn.grid(column=14)
        HighScores(self.global_frame)
