import tkinter as tk
import random
from NewGUI import *

word_list = {"Number Anagrams" : ["eon", "there", "net", "tow"],
             "Orderly" : ["clean", "neat", "tidy", "trim"],
             "Drum ____" : ["ear", "kettle", "oil", "steel"],
             "Python Object Types" : ["integer", "boolean", "float", "string"],
             "Humerous" : ["silly", "goofy", "funny", "hilarious"],
             "Rock ____" : ["solid", "music", "bottom", "on"],
             "Parts of a Flower" : ["petal", "stem", "leaf", "thorn"],
             "Words Containing Numbers" : ["none", "tennis", "sixth", "weight"]}

def random_words(lst):
    all_keys = list(lst.values())
    four_keys = random.sample(all_keys, 4)
    flat_list = []
    for xs in four_keys:
        for x in xs:
            flat_list.append(x)
    random_words = random.sample(flat_list, 16)

    return random_words

list_of_words = random_words(word_list)
print(list_of_words)


# def clear_function(self):
#     button_texts.clear()
#     list_of_categories.clear()





def check_connection(self, button_click1, button_click2, button_click3, button_click4):
    button_clicks = []
    for x in range(4):
        text = self.button.text()
        button_clicks = button_clicks + text
    return button_clicks
    # if button_click1 == button_click2:
    #     if button_click1 == button_click3:
    #         if button_click1 == button_click4:
    #             if button_click1 == 1:
    #                 txt=self.correct_label[""]
    #                 self.correct_label[""] = str("Correct! The Connection Category is Number Anagrams")
    #                 self.button1.configure(bg="yellow")
    #                 self.button7.configure(bg="yellow")
    #                 self.button9.configure(bg="yellow")
    #                 self.button12.configure(bg="yellow")
    #                 ##add list clearing feature
    #
    #             elif button_click1 == 2:
    #                 txt = self.correct_label[""]
    #                 self.correct_label[""] = str("Correct! The Connection Category is Orderly")
    #                 self.button2.configure(bg="green")
    #                 self.button4.configure(bg="green")
    #                 self.button11.configure(bg="green")
    #                 self.button13.configure(bg="green")
    #                 ##add list clearing feature
    #             elif button_click1 == 3:
    #                 txt = self.correct_label[""]
    #                 self.correct_label[""] = str("Correct! The Connection Category is Drum___")
    #                 self.button3.configure(bg="blue")
    #                 self.button5.configure(bg="blue")
    #                 self.button10.configure(bg="blue")
    #                 self.button15.configure(bg="blue")
    #                 ##add list clearing feature
    #             elif button_click1 == 4:
    #                 txt = self.correct_label[""]
    #                 self.correct_label[""] = str("Correct! The Connection Category is Python Object Types")
    #                 self.button6.configure(bg="purple")
    #                 self.button8.configure(bg="purple")
    #                 self.button14.configure(bg="purple")
    #                 self.button16.configure(bg="purple")
    #                 ##add list clearing feature
    #
    #         else:
    #             txt = self.correct_label[""]
    #             self.correct_label[""] = str("Incorrect")
    #
    #     else:
    #         txt = self.correct_label[""]
    #         self.correct_label[""] = str("Incorrect")
    #
    # else:
    #     txt = self.correct_label[""]
    #     self.correct_label[""] = str("Incorrect")



myGui = BasicGui(list_of_words)
myGui.run()