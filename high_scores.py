from tkinter import *
from tkinter import ttk
import pandas

FONT_COLOR = "#F4FFAF"
BACKGROUND_COLOR = "#5584AC"
HEAD_FONT = ('Hiragino Sans', 26, "normal")
ENGLISH_FONT = ('Hiragino Sans', 20, "normal")
RUSSIAN_FONT = ("PT Sans", 20, "normal")


class HighScores:
    def __init__(self, global_frame):
        self.global_frame = global_frame

        with open("high_scores.csv") as high_scores_file:
            high_scores = pandas.read_csv(high_scores_file)

        # English Rating

        # Counting number of scores in english texts
        rows = 0
        for index, row in high_scores.iterrows():
            if row["language"] == "English":
                rows += 1

        # Creating Rating Table for best scores in english texts
        english_rating = Label(self.global_frame, text="English Texts Rating", font=HEAD_FONT,
                               bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        english_rating.grid(row=1, column=0, columnspan=7, pady=10)

        headline_en = Label(self.global_frame, text="Ranking", font=ENGLISH_FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
        headline_en.grid(row=2, column=0, pady=10)

        first_line_en = ttk.Separator(self.global_frame, orient=VERTICAL)
        first_line_en.grid(row=2, column=1, rowspan=rows + 2, sticky="ns", padx=10)

        head_speed_en = Label(self.global_frame, text="Symbols\nper minute", font=ENGLISH_FONT,
                              fg=FONT_COLOR, bg=BACKGROUND_COLOR)
        head_speed_en.grid(row=2, column=2)

        second_line_en = ttk.Separator(self.global_frame, orient=VERTICAL)
        second_line_en.grid(row=2, column=3, rowspan=rows + 2, sticky="ns", padx=10)

        head_accuracy_en = Label(self.global_frame, text="Accuracy in %", font=ENGLISH_FONT, fg=FONT_COLOR,
                                 bg=BACKGROUND_COLOR)
        head_accuracy_en.grid(row=2, column=4)

        third_line_en = ttk.Separator(self.global_frame, orient=VERTICAL)
        third_line_en.grid(row=2, column=5, rowspan=rows + 2, sticky="ns", padx=10)

        head_date_en = Label(self.global_frame, text="Date", font=ENGLISH_FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
        head_date_en.grid(row=2, column=6)

        horizontal_line_en = ttk.Separator(self.global_frame, orient=HORIZONTAL)
        horizontal_line_en.grid(row=3, column=0, columnspan=7, sticky="ew", pady=10)

        # Inserting scores inside the table
        number = 1
        for index, row in high_scores.iterrows():
            if row["language"] == "English":
                num_label = Label(self.global_frame, text=f"{number}", font=ENGLISH_FONT, fg=FONT_COLOR,
                                  bg=BACKGROUND_COLOR)
                num_label.grid(row=number + 3, column=0)

                speed = Label(self.global_frame, text=row["speed"], font=ENGLISH_FONT,
                              fg=FONT_COLOR, bg=BACKGROUND_COLOR)
                speed.grid(row=number + 3, column=2)

                accuracy = Label(self.global_frame, text=row["accuracy"], font=ENGLISH_FONT,
                                 fg=FONT_COLOR, bg=BACKGROUND_COLOR)
                accuracy.grid(row=number + 3, column=4)

                date = Label(self.global_frame, text=row["time"], font=ENGLISH_FONT,
                             fg=FONT_COLOR, bg=BACKGROUND_COLOR)
                date.grid(row=number + 3, column=6)

                number += 1

        empty_label = Label(self.global_frame, width=10, bg=BACKGROUND_COLOR)
        empty_label.grid(row=1, column=7, rowspan=len(high_scores.index) + 2)

        # Russian Rating

        # Counting number of scores in russian texts
        rows = 0
        for index, row in high_scores.iterrows():
            if row["language"] == "Russian":
                rows += 1

        russian_rating = Label(self.global_frame, text="Рейтинг по Русским Текстам", font=("PT Sans", 26, "normal"),
                               bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        russian_rating.grid(row=1, column=8, columnspan=7, pady=10)

        headline_ru = Label(self.global_frame, text="Рейтинг", font=RUSSIAN_FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
        headline_ru.grid(row=2, column=8)

        first_line_ru = ttk.Separator(self.global_frame, orient=VERTICAL)
        first_line_ru.grid(row=2, column=9, rowspan=rows + 2, sticky="ns", padx=10)

        head_speed_ru = Label(self.global_frame, text="Символов\nв минуту", font=RUSSIAN_FONT,
                              fg=FONT_COLOR, bg=BACKGROUND_COLOR)
        head_speed_ru.grid(row=2, column=10)

        second_line_ru = ttk.Separator(self.global_frame, orient=VERTICAL)
        second_line_ru.grid(row=2, column=11, rowspan=rows + 2, sticky="ns", padx=10)

        head_accuracy_en = Label(self.global_frame, text="Точность в %", font=RUSSIAN_FONT, fg=FONT_COLOR,
                                 bg=BACKGROUND_COLOR)
        head_accuracy_en.grid(row=2, column=12)

        third_line_ru = ttk.Separator(self.global_frame, orient=VERTICAL)
        third_line_ru.grid(row=2, column=13, rowspan=rows + 2, sticky="ns", padx=10)

        head_date_ru = Label(self.global_frame, text="Дата", font=RUSSIAN_FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
        head_date_ru.grid(row=2, column=14)

        horizontal_line_ru = ttk.Separator(self.global_frame, orient=HORIZONTAL)
        horizontal_line_ru.grid(row=3, column=8, columnspan=7, sticky="ew", pady=10)

        number = 1
        for index, row in high_scores.iterrows():
            if row["language"] == "Russian":
                num_label = Label(self.global_frame, text=f"{number}", font=ENGLISH_FONT, fg=FONT_COLOR,
                                  bg=BACKGROUND_COLOR)
                num_label.grid(row=number + 3, column=8)

                speed = Label(self.global_frame, text=row["speed"], font=ENGLISH_FONT,
                              fg=FONT_COLOR, bg=BACKGROUND_COLOR)
                speed.grid(row=number + 3, column=10)

                accuracy = Label(self.global_frame, text=row["accuracy"], font=ENGLISH_FONT,
                                 fg=FONT_COLOR, bg=BACKGROUND_COLOR)
                accuracy.grid(row=number + 3, column=12)

                date = Label(self.global_frame, text=row["time"], font=ENGLISH_FONT,
                             fg=FONT_COLOR, bg=BACKGROUND_COLOR)
                date.grid(row=number + 3, column=14)

                number += 1
