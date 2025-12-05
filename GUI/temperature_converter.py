import tkinter as tk
from tkinter import ttk
from temperature import Temperature

class TemperatureGUIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temperature Converter")
        self.geometry("450x350")
        self.configure(bg="#FFA500")
        self.resizable(False, False)

        title_label = ttk.Label(self, text="Temperature Converter",
                                font=("Arial", 20, "bold"), background="#FFA500")
        title_label.pack(pady=10)

        self.main_frame = TemperatureConverterFrame(self)
        self.main_frame.pack(padx=20, pady=10)

class TemperatureConverterFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFA500")
        self.temperature = Temperature(0)
        self.input_unit = tk.StringVar(value="°C")

        def validate_float(P):
            if P == "":
                return True
            try:
                float(P)
                return True
            except ValueError:
                return False

        vcmd = self.register(validate_float)

        ttk.Label(self, text="°C").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_c = ttk.Entry(self, width=20, font=("Arial", 12),
                                 validate="key", validatecommand=(vcmd, "%P"))
        self.entry_c.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="K").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.entry_k = ttk.Entry(self, width=20, font=("Arial", 12),
                                 validate="key", validatecommand=(vcmd, "%P"))
        self.entry_k.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="°F").grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.entry_f = ttk.Entry(self, width=20, font=("Arial", 12),
                                 validate="key", validatecommand=(vcmd, "%P"))
        self.entry_f.grid(row=2, column=1, padx=5, pady=5)

        self.button_frame = ButtonFrame(self)
        self.button_frame.grid(row=3, column=0, columnspan=3, pady=15)

        self.button_frame.button1.config(command=self.convert_clicked)
        self.button_frame.button2.config(command=self.clear_clicked)

        self.result_label = ttk.Label(self, text="", font=("Arial", 12))
        self.result_label.grid(row=4, column=0, columnspan=3, pady=10)

    def convert_clicked(self):
        unit = self.input_unit.get()
        try:
            if unit == "°C":
                val = float(self.entry_c.get())
                self.temperature.celsius = val
            elif unit == "K":
                val = float(self.entry_k.get())
                self.temperature.kelvin = val
            else:
                val = float(self.entry_f.get())
                self.temperature.fahrenheit = val

            self.entry_c.delete(0, tk.END)
            self.entry_k.delete(0, tk.END)
            self.entry_f.delete(0, tk.END)

            self.entry_c.insert(0, f"{self.temperature.celsius:.2f}")
            self.entry_k.insert(0, f"{self.temperature.kelvin:.2f}")
            self.entry_f.insert(0, f"{self.temperature.fahrenheit:.2f}")

            self.result_label.config(text=f"Converted from {unit}")

        except ValueError as e:
            self.result_label.config(text=f"Error: {e}")

    def clear_clicked(self):
        self.entry_c.delete(0, tk.END)
        self.entry_k.delete(0, tk.END)
        self.entry_f.delete(0, tk.END)
        self.result_label.config(text="")

class ButtonFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFA500")
        self.button1 = ttk.Button(self, text="Convert")
        self.button1.grid(row=0, column=0, padx=10, pady=5)

        self.button2 = ttk.Button(self, text="Clear")
        self.button2.grid(row=0, column=1, padx=10, pady=5)

if __name__ == "__main__":
    app = TemperatureGUIApp()
    app.mainloop()