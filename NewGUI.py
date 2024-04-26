import tkinter as tk
from Maincode import *


class BasicGui:
    def __init__(self, list_of_words):
        self.rootWin = tk.Tk()
        self.rootWin.title("Connections")
        self.rootWin.geometry("750x750")
        word_index = 0
        self.button_texts = set()
        # TODO: CREATE A LIST THAT STORES YOUR BUTTONS
        buttonList = [] # Append buttons here
        for row in range(4):
            for column in range(4):
                self.button = tk.Button(self.rootWin, text=list_of_words[word_index], height=5, width=10)
                self.button["command"] = lambda idx=(self.button["text"]): self.button_is_clicked(idx)
                self.button.grid(row=row, column=column)
                word_index = word_index + 1
        self.correct_label = tk.Label(self.rootWin, text="", wraplength=275)
        self.correct_label.grid(row=5, column=1, columnspan=2)
        self.clear_button = tk.Button(self.rootWin, text="clear")
        self.clear_button["command"] = self.clear_function
        self.clear_button.grid(row=5, column=3)

    def button_is_clicked(self, word):
        print(word)
        self.button_texts.add(word)

        print(self.button_texts)
        if len(self.button_texts) == 4:
            self.check_connection()

    def check_connection(self):
        found_match = False
        for k, v in word_list.items():
            differences = self.button_texts.difference(v)
            print(differences)

            if not differences:
                found_match = True
                for k, v in word_list.items():
                    if v == self.button_texts:
                        category_name = k
                        print(category_name)
                        # get colors to change of buttons - ask Amin
                        # list_of_colors = ["yellow", "green", "blue", "purple"]
                        # for x in list(self.button_texts):
                        #     if self.button.cget("text") == x: # Loop through buttons instead of looking at one button only
                        #         self.button.configure(highlightbackground="red")
                        self.correct_label["text"] = str("Correct! The Connection Category is:") + "\n" + str(category_name)
                        self.button_texts.clear()
                    else:
                        pass

        if not found_match:
            self.correct_label["text"] = str("Incorrect Connection")
            self.button_texts.clear()

                #button where x = text of button == self.button.configure(bg="green") - try to make different categories different colors
    #
    def clear_function(self):
        self.button_texts.clear()

    def run(self):
        self.rootWin.mainloop()


if __name__ == '__main__':
    list_of_words = random_words(word_list)
    myGui = BasicGui(list_of_words)
    myGui.run()
