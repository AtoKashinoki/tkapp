import tkapp
import tkinter


class Application(tkinter.Frame):
    def __init__(self, master: tkinter.Tk):
        super().__init__(master)
        self.master = master
        master.geometry("900x600")
        return


if __name__ == '__main__':
    root = tkinter.Tk()
    app = Application(root)
    app.mainloop()
