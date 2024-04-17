import tkinter as tk
class BasicGui:
    def __init__(self):
        self.rootWin = tk.Tk()
        self.rootWin.title("Connections")
        self.rootWin.geometry("750x750")
        for row in range(4):
            for column in range(4):
                self.button = tk.Button(self.rootWin, text=random_text, height=5, width=10)
                self.button.grid(row=row, column=column)
    def run(self):
        self.rootWin.mainloop()

myGui = BasicGui()
myGui.run()
