from tkinter import *
from tkinter import ttk


class Window:
    def __init__(self, master):
        self.master = master
        master.title("De-stract")
        canvas = Canvas(master, width=800, height=0, background="black")
        title = Label(master, text="De-stract", foreground="black", font=("Avenir", 72))
        title.grid()

        nb = ttk.Notebook(master)
        style = ttk.Style()

        style.theme_create("yummy", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [290, 5, 2, 0]}},
            "TNotebook.Tab": {
                "configure": {"padding": [30, 1], "background": "white"},
                "map": {"background": [("selected", "black")], "foreground": [("selected", "white")],
                        "expand": [("selected", [1, 1, 1, 0])]}}})

        style.theme_use("yummy")

        page1 = ttk.Frame(nb, width=800, height=600)
        page2 = ttk.Frame(nb, width=800, height=600)
        nb.add(page1, text="Main")
        nb.add(page2, text="Sound Settings")

        slogan = Label(root, text="Gucci Gang").grid()

        choices = Listbox(page1, selectmode=SINGLE)
        choiceButton = Button(page1, text="Begin", command=lambda: userChoice(choices))
        quitButton = Button(page1, text="Exit", command=quit)

        def userChoice(choices):
            choice = choices.curselection()
            for i in choice:
                print(choices.get(i))
            win = Toplevel()
            # display message
            message = "Dstract is running!"
            Label(win, text=message).pack()
            Button(win, text='End Session', command=win.destroy).pack()

        choices.insert(1, "Chemistry")
        choices.insert(2, "Physics")
        choices.insert(3, "Economics")

        choices.pack()
        choiceButton.pack()
        quitButton.pack()

        nb.grid()
        canvas.grid()


root = Tk()
window = Window(root)
root.mainloop()