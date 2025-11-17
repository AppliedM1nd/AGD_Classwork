import tkinter as tk

class mainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.txt = tk.Label(self, text="My tkinter app",
                            bg="blue2",
                            fg="white",
                            )
        self.btn = tk.Button(self, text="Press me",
                             bg ="orange2",
                             fg="red2",
                             width=15)
        self.edt = tk.Entry(self)

        self.sld = tk.Scale(self,
                            from_=0,
                            to=100,
                            orient=tk.HORIZONTAL,)

        self.config(bg="mistyrose")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'nswe'}
        self.txt.grid(column=0, row=0, padx=10, pady=10)
        self.btn.grid(column=1, row=0, padx=10, pady=10)
        self.edt.grid(column=0, row=1, padx=10, pady=10)
        self.sld.grid(column=1, row=1, padx=10, pady=10)

        self.columnconfigure(0,weight=2)
        self.columnconfigure(1,weight=1)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=2)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x500+100+100')
    root.title("Tkinter Class Example")
    main_frame = mainFrame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    root.mainloop()