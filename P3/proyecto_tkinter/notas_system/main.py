from tkinter import *
from view.menu_principal import MenuPrincipal

if __name__ == "__main__":
    ventana = Tk()
    ventana.title("Gestión de Notas")
    ventana.geometry("600x400")
    ventana.resizable(False, False)

    MenuPrincipal(ventana)

    ventana.mainloop()
