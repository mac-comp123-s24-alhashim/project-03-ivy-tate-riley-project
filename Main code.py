import tkinter as tk
import random

word_list = [{"eon" : "Number Anagrams", "there" : "Number Anagrams", "net" : "Number Anagrams", "tow" : "Number Anagrams"},
                    {"clean" : "Orderly", "neat" : "Orderly", "tidy" : "Orderly", "trim" : "Orderly"},
                    {"ear" : "Drum ____", "kettle" : "Drum ____", "oil" : "Drum ____", "steel" : "Drum ____"},
                    {"integer" : "Python Object Types", "boolean" : "Python Object Types", "float" : "Python Object Types", "string" : "Python Object Types"},
                    {"silly" : "Humerous", "goofy" : "Humerous", "funny" : "Humerous", "hilarious" : "Humerous"},
                    {"solid" : "Rock ____", "music" : "Rock ____", "bottom" : "Rock ____", "on": "Rock ____"},
                    {"petal" : "Parts of a Flower", "stem" : "Parts of a Flower", "leaf" : "Parts of a Flower", "thorn" : "Parts of a Flower"},
                    {"none" : "Words Containing Numbers", "tennis" : "Words Containing Numbers", ""}]

## flip dictionary order {Category name : [word1, word2, word3, word4]}

def random_groups(lst):
    groups = random.sample(lst, k=4)
    return groups

def random_text(lst):
    


# def check_connection(button_click1, button_click2, button_click3, button_click4):
#     if button_click1 == button_click2:
#         if button_click1 == button_click3:
#             if button_click1 == button_click4:
#                 if button_click1 == 1:
#                     txt=self.correct_label[""]
#                     self.correct_label[""] = str("Correct! The Connection Category is Number Anagrams")
#                     self.button1.configure(bg="yellow")
#                     self.button7.configure(bg="yellow")
#                     self.button9.configure(bg="yellow")
#                     self.button12.configure(bg="yellow")
#                     ##add list clearing feature
#
#                 elif button_click1 == 2:
#                     txt = self.correct_label[""]
#                     self.correct_label[""] = str("Correct! The Connection Category is Orderly")
#                     self.button2.configure(bg="green")
#                     self.button4.configure(bg="green")
#                     self.button11.configure(bg="green")
#                     self.button13.configure(bg="green")
#                     ##add list clearing feature
#                 elif button_click1 == 3:
#                     txt = self.correct_label[""]
#                     self.correct_label[""] = str("Correct! The Connection Category is Drum___")
#                     self.button3.configure(bg="blue")
#                     self.button5.configure(bg="blue")
#                     self.button10.configure(bg="blue")
#                     self.button15.configure(bg="blue")
#                     ##add list clearing feature
#                 elif button_click1 == 4:
#                     txt = self.correct_label[""]
#                     self.correct_label[""] = str("Correct! The Connection Category is Python Object Types")
#                     self.button6.configure(bg="purple")
#                     self.button8.configure(bg="purple")
#                     self.button14.configure(bg="purple")
#                     self.button16.configure(bg="purple")
#                     ##add list clearing feature
#
#             else:
#                 txt = self.correct_label[""]
#                 self.correct_label[""] = str("Incorrect")
#
#         else:
#             txt = self.correct_label[""]
#             self.correct_label[""] = str("Incorrect")
#
#     else:
#         txt = self.correct_label[""]
#         self.correct_label[""] = str("Incorrect")