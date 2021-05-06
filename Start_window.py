import tkinter as tk


class PopWindow:

    def __init__(self):
        self.start = False
        self.pop_window = tk.Tk()
        self.pop_window.title("Game Start setup window")
        self.pop_window.geometry('550x400')

    def buttonClick(self):
        self.pop_window.destroy()


    def Button(self):
        self.button = tk.Button(self.pop_window, text="Prest To Start", command=self.buttonClick)
        self.button.pack()
        self.pop_window.mainloop()

