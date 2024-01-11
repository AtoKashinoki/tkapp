import tkapp
import tkinter


class Application(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.geometry("600x900")
        return


if __name__ == '__main__':
    root = tkinter.Tk()
    app = Application(root)
    app.mainloop()
    print(type(tkapp.ErrorClasses))

