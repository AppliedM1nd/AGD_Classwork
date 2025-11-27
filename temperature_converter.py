import tkinter as tk
from tkinter import ttk

class ButtonFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.button1 = ttk.Button(self, text="Convert")
        self.button1.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.button2 = ttk.Button(self, text="Clear")
        self.button2.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

class CheckBox(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.show_calc = tk.BooleanVar()
        frame = tk.Frame(self)
        frame.grid(row=0, column=1, sticky=tk.W)
        checkbox1 = ttk.Checkbutton(frame, text='Show Calculation', variable=self.show_calc)
        checkbox1.pack(side=tk.LEFT, padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('450x350')
    root.title('Temperature Converter')
    root.configure(bg="#FFA500")  # light red background for main window only

    title_label = ttk.Label(root, text="Temperature Converter", font=("Arial", 18, "bold"))
    title_label.pack(pady=10)

    general_frame = tk.Frame(root)
    general_frame.pack(fill=tk.X, padx=10, pady=5)

    selection = tk.StringVar(value="°C")

    temperature_entry_c = ttk.Entry(general_frame, width=30)
    temperature_entry_c.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
    rb_c = ttk.Radiobutton(general_frame, text="°C", value="°C", variable=selection)
    rb_c.grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)

    temperature_entry_k = ttk.Entry(general_frame, width=30)
    temperature_entry_k.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
    rb_k = ttk.Radiobutton(general_frame, text="K", value="K", variable=selection)
    rb_k.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)

    temperature_entry_f = ttk.Entry(general_frame, width=30)
    temperature_entry_f.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
    rb_f = ttk.Radiobutton(general_frame, text="°F", value="°F", variable=selection)
    rb_f.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)

    button_frame = ButtonFrame(root)
    button_frame.pack(pady=10)

    button_frame2 = CheckBox(root)
    button_frame2.pack(pady=10)

    root.mainloop()
