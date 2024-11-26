import tkinter as tk


class Janela:
    # Conjunto de instâncias da classe
    _instances = []

    @classmethod
    def getInstances(cls):  #Fornece o conjunto de instâncias da classe
        return cls._instances
    
    def __init__(self, nome, sizeX, sizeY):
        self.window = tk.Tk(useTk=False)
        self.name = nome
        self.sizex = sizeX
        self.sizey = sizeY
        self.buttons = []

        Janela._instances.append(self)

    def createWindow(self, inst):
        if inst == 0:
            self.window = tk.Tk()

        else:
            self.window = tk.Toplevel()

        self.window.title(self.name)

        self.window.minsize(self.sizex, self.sizey)
        #self.window.maxsize(self.sizex, self.sizey)

    def update(self):
        self.window.mainloop()

    def createButton(self, nome, action, args=None, placex=0, placey=0, relative=False, anch="nw", color="LightGoldenRodYellow"):
        if args != None:
            btn = tk.Button(self.window, text=nome, command=lambda: action(args), bg=color)
        else:
            btn = tk.Button(self.window, text=nome, command=action, bg=color)
        if not relative:
            btn.place(x=placex, y=placey)
        else:
            btn.place(relx=placex, rely=placey, anchor=anch)
        self.buttons.append(btn)
        return btn
