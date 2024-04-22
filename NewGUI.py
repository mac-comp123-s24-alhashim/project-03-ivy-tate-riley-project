import tkinter as tk
from Maincode import *
import cv2

class BasicGui:
    def __init__(self, list_of_words):
        self.rootWin = tk.Tk()
        self.rootWin.title("Connections")
        self.rootWin.geometry("750x750")
        word_index = 0
        for row in range(4):
            for column in range(4):
                self.button = tk.Button(self.rootWin, text=list_of_words[word_index], height=5, width=10)
                self.button.grid(row=row, column=column)
                word_index = word_index + 1

    def check_connection(self, button_click1, button_click2, button_click3, button_click4):
        button_clicks = []
        for x in range(4):
            text = self.button.text()
            button_clicks = button_clicks + text
        return button_clicks


    def run(self):
        self.rootWin.mainloop()
        print(check_connection())

