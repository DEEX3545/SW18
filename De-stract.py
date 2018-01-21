from tkinter import *
from tkinter import ttk

class Window:
    def __init__(self, master):
        self.master = master
        master.title("De-stract")
        canvas = Canvas(master, width=800, height=0, background="black")
        title = Label(master, text="De-stract", foreground="white", background="black", font=("Avenir", 72))
        title.grid()

        nb = ttk.Notebook(master)

        page1 = ttk.Frame(nb, width=800, height=600)
        page2 = ttk.Frame(nb, width=800, height=600)
        nb.add(page1, text="Main")
        nb.add(page2, text="Sound Settings")

        nb.grid()
        canvas.grid()


root = Tk()
window = Window(root)
root.mainloop()
