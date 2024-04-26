import tkinter as tk
from Maincode import *


class BasicGui:
    def __init__(self, list_of_words):
        self.rootWin = tk.Tk()
        self.rootWin.title("Connections")
        self.rootWin.geometry("750x750")
        word_index = 0
        self.button_texts = set()
        for row in range(4):
            for column in range(4):
                self.button = tk.Button(self.rootWin, text=list_of_words[word_index], height=5, width=10)
                self.button["command"] = lambda idx = (self.button["text"]): self.button_is_clicked(idx)
                self.button.grid(row=row, column=column)
                word_index = word_index + 1
        self.correct_label = tk.Label(self.rootWin, text="")
        self.correct_label.grid(row=5, column=2)
        self.clear_button = tk.Button(self.rootWin, text="clear", command="clear_function")
        self.clear_button.grid(row=5, column=3)

    def button_is_clicked(self, word):
        print(word)
        self.button_texts.add(word)

        print(self.button_texts)
        if len(self.button_texts) == 4:
            self.check_connection()

    def check_connection(self):
        for k,v in word_list.items():
            differences = self.button_texts.difference(v)
            print(differences)

        if set() in differences:
            for k, v in word_list.items():
                if v == self.button_texts:
                    category_name = k
            self.correct_label[""] = "Correct! The Connection Category is category_name"
    #         list_of_colors = ["yellow", "green", "blue", "purple"]
    #         for x in button_texts:
    #
    #             #button where x = text of button == self.button.configure(bg="green") - try to make different categories different colors
    #         button_texts.clear()
    #         list_of_categories.clear()
    #     else:
    #         self.correct_label[""] = str("Incorrect Connection")
    #         button_texts.clear()
    #         list_of_categories.clear()
    #
    # def clear_function(self):
    #     button_texts.clear()
    #     list_of_categories.clear()

    def run(self):
        self.rootWin.mainloop()

if __name__ == '__main__':
    list_of_words = random_words(word_list)
    myGui = BasicGui(list_of_words)
    myGui.run()


