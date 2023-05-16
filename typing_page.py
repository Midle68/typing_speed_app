from tkinter import *
import numpy
import pandas
import random
import datetime
import math

FONT_COLOR = "#F4FFAF"
BACKGROUND_COLOR = "#5584AC"
ENGLISH_FONT = ("Hiragino Sans", 20, "normal")
RUSSIAN_FONT = ("PT Sans", 22, "normal")
MIDDLE_FONT = ('Hiragino Sans', 26, "normal")
BLUE = "#333C83"


class TypingPage:
    def __init__(self, global_frame, language):
        self.time = 5
        self.mistakes = 0
        self.language = language
        self.now = None
        self.period_timer = None

        # Choose random text based on the chosen language and set the width of the player's text widget
        if self.check_english():
            with open('./texts/english_texts.txt') as data_file:
                self.text = random.choice(data_file.readlines())
                text_width = 47
        else:
            with open("./texts/russian_texts.txt") as data_file:
                self.text = random.choice(data_file.readlines())
                text_width = 55

        self.text_list = [i for i in self.text if i != "\n"]

        # The images for the button (start and stop, hover and normal)
        self.start_normal_img = PhotoImage(file="./buttons/Start Normal.png")
        self.start_hover_img = PhotoImage(file="./buttons/Start Hover.png")
        self.stop_normal_img = PhotoImage(file="./buttons/Stop Normal.png")
        self.stop_hover_img = PhotoImage(file="./buttons/Stop Hover.png")

        self.global_frame = global_frame

        # Insert all the widget in the canvas
        self.canvas = Canvas(self.global_frame, width=700, height=200)
        self.canvas.grid(row=1, column=0, columnspan=3, pady=20)

        # English text limit - 280 symbols !!!
        # Russian text limit - 400 symbols !!!

        # ----- Widgets ----- #

        # Canvas where words of the text will be displayed
        self.canvas_text = self.canvas.create_text(350, 105, text="",
                                                   fill=BLUE, font=RUSSIAN_FONT, width=650)

        self.timer = Label(self.global_frame, text=f"Time: Start", font=MIDDLE_FONT,
                           bg=BACKGROUND_COLOR, fg="white")
        self.timer.grid(row=2, column=0)

        self.mistakes_label = Label(self.global_frame, text="Mistakes: Start", font=MIDDLE_FONT,
                                    bg=BACKGROUND_COLOR, fg="white")
        self.mistakes_label.grid(row=2, column=1)

        self.speed_label = Label(self.global_frame, text="Speed: Finish", font=MIDDLE_FONT,
                                 bg=BACKGROUND_COLOR, fg="white")
        self.speed_label.grid(row=2, column=2)

        self.accuracy_label = Label(self.global_frame, text="Accuracy: Finish", font=MIDDLE_FONT,
                                    bg=BACKGROUND_COLOR, fg="white")
        self.accuracy_label.grid(row=3, column=2)

        # Changing player_text_widget parameters
        self.player_text_widget = Text(self.global_frame, width=text_width, height=6, padx=18, font=ENGLISH_FONT)
        self.player_text_widget.grid(row=4, column=0, columnspan=3, pady=20)
        self.player_text_widget.insert(1.0, "Type here")
        self.player_text_widget.config(state=DISABLED, bg="#D1D1D1", fg="#9D9D9D")

        self.text_language()  # Changing some parameters considering the language

        self.start_stop_btn = Button(self.global_frame, text="Start", font=ENGLISH_FONT, fg=BLUE, borderwidth=0,
                                     image=self.start_normal_img, bg=BACKGROUND_COLOR, command=self.start_program)
        self.start_stop_btn.grid(row=5, column=0, columnspan=3)

        self.bind_start()  # Add start_stop_btn images on and off hover

    def check_english(self):
        if self.language == "English":
            return True
        else:
            return False

    def text_language(self):
        if self.check_english():  # Change some parameters considering the language
            self.canvas.itemconfig(self.canvas_text, text="The text will be displayed here.")
        else:
            self.canvas.itemconfig(self.canvas_text, text="Здесь будет отображен текст.")
            self.player_text_widget.config(font=RUSSIAN_FONT)

    def bind_start(self):  # Binding start hover and normal images
        self.start_stop_btn.bind("<Enter>", self.start_hover)
        self.start_stop_btn.bind("<Leave>", self.start_normal)

    def bind_stop(self):  # Binding stop hover and normal images
        self.start_stop_btn.bind("<Enter>", self.stop_hover)
        self.start_stop_btn.bind("<Leave>", self.stop_normal)

    def start_hover(self, e):  # Set start hover img
        self.start_stop_btn["image"] = self.start_hover_img
        self.start_stop_btn.image = self.start_hover_img

    def start_normal(self, e):  # Set start normal img
        self.start_stop_btn.config(image=self.start_normal_img)

    def stop_normal(self, e):  # Set stop normal img
        self.start_stop_btn["image"] = self.stop_normal_img
        self.start_stop_btn.image = self.stop_normal_img

    def stop_hover(self, e):  # Set stop hover img
        self.start_stop_btn["image"] = self.stop_hover_img
        self.start_stop_btn.image = self.stop_hover_img

    def start_program(self):
        self.stop_hover("e")

        # Добавить остановку всей программы по нажатию на self.start_stop_btn
        # self.start_stop_btn.config(command=self.stop_program)
        self.start_stop_btn.config(command=self.restart_program)
        self.mistakes_label.config(text=f"Mistakes: {self.mistakes}")

        self.timer.config(text=f"Time: {self.time}")

        self.bind_stop()  # Set btn images to stop normal and hover
        self.count_down()

    def count_down(self):  # Showing time-reduction
        self.time -= 1
        if self.time == 0:  # If 5 seconds passed, start counting up
            self.canvas.itemconfig(self.canvas_text, text=self.text)
            self.period_timer = self.global_frame.after(1000, lambda: self.change_pregame_timer(self.count_up))
        else:
            self.period_timer = self.global_frame.after(1000, lambda: self.change_pregame_timer(self.count_down))

    def change_pregame_timer(self, function):  # Working program whether counting up or down
        self.timer.config(text=f"Time: {self.time}")

        # If count up, allow player to type and receive the keys pressed
        if function == self.count_up:
            self.player_text_widget.config(state=NORMAL, bg="white", fg="black")
            self.player_text_widget.delete(1.0, END)
            self.player_text_widget.focus()
            self.time -= 1
            self.global_frame.bind_all("<KeyPress>", self.process_text)
            self.now = datetime.datetime.now()
        function()

    def count_up(self):
        self.time += 1
        self.timer.config(text=f"Time: {self.time}")
        self.period_timer = self.global_frame.after(1000, self.count_up)

    def process_text(self, e):  # Processing the typed text
        try:
            typed_letters = list(self.player_text_widget.get(1.0, END).strip())
            text_len = len(self.player_text_widget.get(1.0, END).strip())

            # Check if the typed letter matches the one in the original text
            # Pass if it's 'BackSpace'
            if typed_letters[-1] != self.text[text_len - 1] and e.keysym != "BackSpace":
                # If not - find its index and turn it into red
                self.player_text_widget.tag_add("red", f"1.{text_len - 1}", f"1.{text_len}")
                self.player_text_widget.tag_configure("red", foreground="red")
                self.mistakes += 1
                self.mistakes_label.config(text=f"Mistakes: {self.mistakes}")
        except IndexError:
            pass

        # If typed text matches the original one, stop program and compute the speed
        if self.text_list == list(self.player_text_widget.get(1.0, END).strip()):
            end = datetime.datetime.now()
            self.stop_program(end)

    def restart_program(self):  # Restart program and return everything to default
        # Unbind keys and change labels
        self.global_frame.unbind("<KeyPress>")
        self.global_frame.after_cancel(self.period_timer)
        self.timer.config(text="Time: Start")
        self.mistakes_label.config(text="Mistakes: Start")
        self.speed_label.config(text="Speed: Finish")
        self.accuracy_label.config(text="Accuracy: Finish")

        # Change hover state, bind on and off hover, start_stop_btn command
        self.start_stop_btn["image"] = self.start_hover_img
        self.start_stop_btn.image = self.start_hover_img
        self.bind_start()
        self.start_stop_btn.config(command=self.start_program)

        # Return attributes to normal values
        self.time = 5
        self.mistakes = 0
        self.text_language()

        # Make player_text_widget unavailable
        self.player_text_widget.config(state=NORMAL)
        self.player_text_widget.delete(1.0, END)
        self.player_text_widget.insert(1.0, "Type here")
        self.player_text_widget.config(state=DISABLED, bg="#D1D1D1", fg="#9D9D9D")

    def stop_program(self, end_time):  # Stop program when the typed text matches the original one
        # Change start_stop_btn images on and off hover
        self.start_stop_btn.config(image=self.start_normal_img)
        self.bind_start()

        # Make player_text_widget unavailable
        self.player_text_widget.config(state=DISABLED, bg="#D1D1D1", fg="#9D9D9D")
        self.global_frame.after_cancel(self.period_timer)
        self.global_frame.unbind("<KeyPress>")

        # Count speed in symbols per minute and accuracy in percent
        difference = (end_time - self.now).seconds
        symbols_per_minute = math.floor((len(self.text_list) / difference) * 60)
        accuracy = round(100 - self.mistakes / len(self.text_list) * 100, 2)

        # Insert the speed and accuracy
        self.speed_label.config(text=f"Speed: {symbols_per_minute} spm")
        self.accuracy_label.config(text=f"Accuracy: {accuracy}%")

        # Saving current date provided it's a Top-10 score
        current_date = datetime.datetime.now().strftime("%d %B %Y")

        # Saving the result inside the 'high_scores.csv'
        try:  # Checking if 'high_scores.csv' exists
            with open("high_scores.csv") as high_scores_file:
                high_scores = pandas.read_csv(high_scores_file)

            existing_data = pandas.DataFrame(
                {
                    "speed": high_scores["speed"].values,
                    "accuracy": high_scores["accuracy"].values,
                    "time": high_scores["time"].values,
                    "language": high_scores["language"].values
                },
                index=[i for i in range(len(high_scores.index) + 1) if i]
            )

            # Checking the number of scores for a chosen language
            high_scores_rows = 0
            for index, row in high_scores.iterrows():
                if row["language"] == self.language:
                    high_scores_rows += 1

            # If there are 10 results already, checking if the current one outperforms one of the previous
            if high_scores_rows == 10:
                for index, row in high_scores.iterrows():
                    if row["language"] == self.language:
                        if symbols_per_minute > row["speed"]:
                            high_score_index = list(numpy.where(high_scores["speed"] == row["speed"]))[0][0]
                            existing_data = existing_data.drop(index=high_score_index + 1)
                            current_data = pandas.DataFrame(
                                {
                                    "speed": [symbols_per_minute],
                                    "accuracy": [accuracy],
                                    "time": [current_date],
                                    "language": self.language
                                },
                                index=[high_score_index]
                            )
                            break
            else:
                # If there aren't 10 results - just adding the current one
                current_data = pandas.DataFrame(
                    {
                        "speed": [symbols_per_minute],
                        "accuracy": [accuracy],
                        "time": [current_date],
                        "language": self.language
                    },
                    index=[len(high_scores.index) + 1]
                )

            # Concat the existing results with the new one
            try:
                new_frame = pandas.concat([existing_data, current_data]).sort_values("speed", ascending=False)
                new_frame.to_csv("high_scores.csv")
            except UnboundLocalError:
                pass

        # If there aren't 'high_scores.csv' file, creating a new one
        except FileNotFoundError:
            current_data = pandas.DataFrame(
                {
                    "speed": [symbols_per_minute],
                    "accuracy": [accuracy],
                    "time": [current_date],
                    "language": self.language
                },
                index=[1]
            )

            pandas.DataFrame(current_data).to_csv("high_scores.csv")
