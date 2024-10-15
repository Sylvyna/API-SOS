import tkinter as tk
import tkinter.ttk as ttk
import APPui as baseui


class GUI_app(baseui.GUI_appUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = GUI_app()
    app.run()
