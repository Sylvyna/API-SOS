import tkinter as tk
import tkinter.ttk as ttk
import os
from bin.sos_api import login_cuit, consulta_f2002


def cafecito():
    os.system('start "" "https://cafecito.app/abustos"')


def abrir_credenciales():
    os.system('notepad "./bin/Login.json"')


def abrir_csv():
        os.startfile(r".\contribuyentes.csv")


class GUI_appUI:
    def __init__(self, master=None):
        # build ui
        Toplevel_1 = tk.Tk() if master is None else tk.Toplevel(master)
        Toplevel_1.configure(
            background="#2e2e2e",
            cursor="arrow",
            height=250,
            width=520)
        Toplevel_1.iconbitmap("bin/ABP-blanco-en-fondo-negro.ico")
        Toplevel_1.minsize(340, 520)
        Toplevel_1.overrideredirect("False")
        Toplevel_1.resizable(False, False)
        Toplevel_1.title("Descarga Papeles de Tabajo SOS")
        Label_3 = ttk.Label(Toplevel_1)
        self.img_ABPsinFondo = tk.PhotoImage(
            file="bin/ABP-blanco-sin-fondo.png")
        Label_3.configure(
            background="#2e2e2e",
            compound="bottom",
            font="TkFixedFont",
            image=self.img_ABPsinFondo)
        Label_3.pack(side="top")
        Label_1 = ttk.Label(Toplevel_1)
        Label_1.configure(
            background="#2e2e2e",
            compound="top",
            font="TkDefaultFont",
            foreground="#ffffff",
            justify="center",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Descarga masiva de Papeles de Trabajo de IVA para la realización del F2002\n',
            wraplength=325)
        Label_1.pack(expand=True, side="top")
        Label_2 = ttk.Label(Toplevel_1)
        Label_2.configure(
            background="#2e2e2e",
            foreground="#ffffff",
            justify="center",
            text='por Agustín Bustos Piasentini\nhttps://www.Agustin-Bustos-Piasentini.com.ar/')
        Label_2.pack(expand=True, side="top")
        self.Credenciales = ttk.Button(Toplevel_1, name="credenciales")
        self.Credenciales.configure(
            text='Abrir Credenciales', command=abrir_credenciales)
        self.Credenciales.pack(expand=True, pady=4, side="top")
        self.Obtener_Tokens = ttk.Button(Toplevel_1, name="obtener_tokens")
        self.Obtener_Tokens.configure(
            text='Obtener Tokens de Acceso', command=login_cuit)
        self.Obtener_Tokens.pack(expand=True, padx=0, pady=4, side="top")
        self.Editar_CSV = ttk.Button(Toplevel_1, name="editar_csv")
        self.Editar_CSV.configure(text='Editar CSV' , command=abrir_csv)
        self.Editar_CSV.pack(expand=True, pady=4, side="top")
        self.Descarga_PT = ttk.Button(Toplevel_1, name="descarga_pt", command=consulta_f2002)
        self.Descarga_PT.configure(
            text='Descarga Masiva de Papeles de Trabajo')
        self.Descarga_PT.pack(expand=True, pady=4, side="top")
        self.Donaciones = ttk.Button(Toplevel_1, name="donaciones")
        self.Donaciones.configure(text='Donaciones', command=cafecito)
        self.Donaciones.pack(side="top")
        label1 = ttk.Label(Toplevel_1)
        self.img_soscontador_150x78 = tk.PhotoImage(
            file="bin/sos-contador_-small.png")
        label1.configure(
            background="#2e2e2e",
            image=self.img_soscontador_150x78,
            text='label1')
        label1.pack(side="top")

        # Main widget
        self.mainwindow = Toplevel_1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = GUI_appUI()
    app.run()
