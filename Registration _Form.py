import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class CountrySelector(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.selected_country = tk.StringVar()
        label = ttk.Label(self, text="Country:")
        label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self.country = ttk.Combobox(self, textvariable=self.selected_country, state='readonly')
        self.country['values'] = ['France', 'Canada', 'Germany', 'Italy', 'UK', 'USA']
        self.country.grid(row=0, column=1, padx=5, pady=5)
        self.country.bind('<<ComboboxSelected>>', self.country_chosen)

    def country_chosen(self, event):
        showinfo(title='Result', message=f'You selected {self.selected_country.get()}!')


class RadioButton(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.selection = tk.StringVar(value="Male")
        label = ttk.Label(self, text="Gender:")
        label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        frame = tk.Frame(self)
        frame.grid(row=0, column=1, sticky=tk.W)
        rb1 = ttk.Radiobutton(frame, text="Male", value="Male", variable=self.selection)
        rb2 = ttk.Radiobutton(frame, text="Female", value="Female", variable=self.selection)
        rb1.pack(side=tk.LEFT, padx=5)
        rb2.pack(side=tk.LEFT, padx=5)


class CheckBox(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = ttk.Label(self, text="Programming:")
        label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self.java = tk.BooleanVar()
        self.python = tk.BooleanVar()

        frame = tk.Frame(self)
        frame.grid(row=0, column=1, sticky=tk.W)

        checkbox1 = ttk.Checkbutton(frame, text='Java', variable=self.java)
        checkbox2 = ttk.Checkbutton(frame, text='Python', variable=self.python)
        checkbox1.pack(side=tk.LEFT, padx=5)
        checkbox2.pack(side=tk.LEFT, padx=5)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('450x350')
    root.title('Registration Form')

    title_label = ttk.Label(root, text="Registration Form", font=("Arial", 18, "bold"))
    title_label.pack(pady=10)

    full_name_frame = tk.Frame(root)
    full_name_frame.pack(fill=tk.X, padx=10, pady=5)
    ttk.Label(full_name_frame, text="Full Name:").grid(row=0, column=0, sticky=tk.W, padx=5)
    full_name_entry = ttk.Entry(full_name_frame)
    full_name_entry.grid(row=0, column=1, padx=5)

    email_frame = tk.Frame(root)
    email_frame.pack(fill=tk.X, padx=10, pady=5)
    ttk.Label(email_frame, text="Email:").grid(row=0, column=0, sticky=tk.W, padx=5)
    email_entry = ttk.Entry(email_frame)
    email_entry.grid(row=0, column=1, padx=5)

    gender_row = RadioButton(root)
    gender_row.pack(fill=tk.X, padx=10, pady=5)

    country_row = CountrySelector(root)
    country_row.pack(fill=tk.X, padx=10, pady=5)

    programming_row = CheckBox(root)
    programming_row.pack(fill=tk.X, padx=10, pady=5)

    submit_label = ttk.Label(root, text="Submit", font=("Helvetica", 12))
    submit_label.pack(pady=10)

    root.mainloop()
