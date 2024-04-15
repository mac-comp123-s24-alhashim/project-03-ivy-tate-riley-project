import tkinter as tk



def check_connection(button_click1, button_click2, button_click3, button_click4):
    if button_click1 == button_click2:
        if button_click1 == button_click3:
            if button_click1 == button_click4:
                if button_click1 == 1:
                    txt=self.correct_label[""]
                    self.correct_label[""] = str("Correct! The Connection Category is Number Anagrams")
                    self.button1.configure(bg="yellow")
                    self.button7.configure(bg="yellow")
                    self.button9.configure(bg="yellow")
                    self.button12.configure(bg="yellow")
                    ##add list clearing feature

                elif button_click1 == 2:
                    txt = self.correct_label[""]
                    self.correct_label[""] = str("Correct! The Connection Category is Orderly")
                    self.button2.configure(bg="green")
                    self.button4.configure(bg="green")
                    self.button11.configure(bg="green")
                    self.button13.configure(bg="green")
                    ##add list clearing feature
                elif button_click1 == 3:
                    txt = self.correct_label[""]
                    self.correct_label[""] = str("Correct! The Connection Category is Drum___")
                    self.button3.configure(bg="blue")
                    self.button5.configure(bg="blue")
                    self.button10.configure(bg="blue")
                    self.button15.configure(bg="blue")
                    ##add list clearing feature
                elif button_click1 == 4:
                    txt = self.correct_label[""]
                    self.correct_label[""] = str("Correct! The Connection Category is Python Object Types")
                    self.button6.configure(bg="purple")
                    self.button8.configure(bg="purple")
                    self.button14.configure(bg="purple")
                    self.button16.configure(bg="purple")
                    ##add list clearing feature

            else:
                txt = self.correct_label[""]
                self.correct_label[""] = str("Incorrect")

        else:
            txt = self.correct_label[""]
            self.correct_label[""] = str("Incorrect")

    else:
        txt = self.correct_label[""]
        self.correct_label[""] = str("Incorrect")