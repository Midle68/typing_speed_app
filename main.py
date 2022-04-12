#  TODO A: GUI
#      TODO 1: (+) Create GUI for main page
#      TODO 2: (+) Create Buttons in Photoshop:
#        (+) Start English & Start Russian in normal and hover states
#        (+) High Scores button in normal and hover states
#      TODO 3: (+) Change font for the 'self.headline'. [Result - "Hiragino Sans"]
#      TODO 4: (+) Provide the operation of clearing function 'self.clear()' in 'user_interface.py'
#      TODO 5: (+) Add 'Typing Page'
#        (+) Set the valid parameters for the text to be properly displayed
#        (+) Add Text-Entry widget and all the parameters to it
#        (+) Add "Start" button + style it (image of a btn)
#      TODO 6: (+) Add page for 'high_scores'
#        (+) Create UI for high scores page
#        (+) Add high scores in English and Russian + Separate them (10 best scores for each)
#      TODO 7: (+) Add button on all the pages to return to the main menu

#  TODO B: Data
#      TODO 1: (+) Add texts in English
#      TODO 2: (+) Add texts in Russian
#      TODO 3: (+) Show text in a canvas (self.canvas in typing_page.py) depending on the chosen language

#  TODO C: Program
#      TODO 1: (+) 'Start' button function:
#        (+) 5-seconds timer shown (another Canvas needed?)
#        (+) Text in self.canvas appears
#        (+) self.text state turns to NORMAL with focus() on this widget
#      TODO 2: (+) Perceive the typing information
#      TODO 3: (+) Turn the wrong letter in red
#      TODO 4: (+) Show on the interface the final result:
#        (+) Symbols per minute (may be wpm?)
#        (+) Amount of errors made
#        (+) Accuracy in %
#      TODO 5: (+) Restart program on button 'Stop'
#      TODO 6: (+) Stop program when the text typed is equal to the text that is to be typed
#      TODO 7: (+) Save 10 best results

#  TODO after A & B & C:
#      TODO ( B ) 4: (+) Add texts in english and russian
#      TODO ( A ) 6: (+) Add page for 'High Score

#  TODO D: Code
#      TODO 1: (+) Add notes to the code
#      TODO 2: (+) Refactor the code


from user_interface import UserInterface


def main():
    user_interface = UserInterface()
    user_interface.create_user_interface()


main()
