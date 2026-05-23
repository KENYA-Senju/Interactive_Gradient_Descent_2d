import tkinter as tk
from tkinter import ttk
import numpy as np
import random


from DescentMod import descent_run

class InteractiveApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Gradient Descent Interactive")

        self.default_font = ("Arial", 12)
        self.padding = 10

        self.buildUI()

    def buildUI(self):
        self.create_labels()
        self.create_entries()
        self.create_button()

    def create_labels(self):
        # Learning Rate Label
        self.lr_label = tk.Label(
            self.window,
            text="Learning Rate",
            font=self.default_font
        )
        self.lr_label.grid(row=0, column=0, padx=self.padding, pady=(self.padding, 0), sticky="w")

        # Starting Point Label
        self.sp_label = tk.Label(
            self.window,
            text="Starting Point",
            font=self.default_font
        )
        self.sp_label.grid(row=2, column=0, padx=self.padding, pady=(self.padding, 0), sticky="w")

        # Function Label
        self.func_label = tk.Label(
            self.window,
            text="Function f(x)",
            font=self.default_font
        )
        self.func_label.grid(row=4, column=0, padx=self.padding, pady=(self.padding, 0), sticky="w")

    def create_entries(self):
        # Learning Rate Entry
        self.lr_entry = tk.Entry(
            self.window,
            font=self.default_font,
            width=30
        )
        self.lr_entry.grid(row=1, column=0, padx=self.padding, pady=(0, self.padding), sticky="w")
        self.lr_entry.insert(0, "0.03")

        # Starting Point Entry with random default
        self.sp_entry = tk.Entry(
            self.window,
            font=self.default_font,
            width=30
        )
        self.sp_entry.grid(row=3, column=0, padx=self.padding, pady=(0, self.padding), sticky="w")
        default_start = random.choice(np.linspace(-50, 50, 400))
        self.sp_entry.insert(0, f"{default_start:.4f}")

        # Function Entry with tooltip
        self.func_entry = tk.Entry(
            self.window,
            font=self.default_font,
            width=30
        )
        self.func_entry.grid(row=5, column=0, padx=self.padding, pady=(0, 0), sticky="w")
        self.func_entry.insert(0, "x**2")

        # Tooltip/help text for function entry
        self.func_help = tk.Label(
            self.window,
            text="",
            font=("Arial", 9),
            fg="gray",
            wraplength=250,
            justify="left"
        )
        self.func_help_lr = tk.Label(
            self.window,
            text="",
            font=("Arial", 9),
            fg="gray",
            wraplength=250,
            justify="left"
        )
        self.func_help.grid(row=6, column=0, padx=self.padding, pady=(0, self.padding), sticky="w")
        self.func_help_lr.grid(row=2, column=0, padx=self.padding, pady=(0, self.padding), sticky="w")

        # Bind hover events for tooltip
        self.func_entry.bind( "<FocusIn>", self.show_func_help)
        self.func_entry.bind("<FocusOut>", self.hide_func_help)

        self.lr_entry.bind("<Enter>", self.show_func_help_lr)
        self.lr_entry.bind("<Leave>", self.hide_func_help_lr)


        self.func_entry.bind("<Enter>",  self.show_func_help)
        self.func_entry.bind("<Leave>", self.hide_func_help_if_not_focused)

    def show_func_help(self, event=None):
        help_text = (
                "Format: Use 'x' as the variable.\n"
                "Operators: +, -, *, /, ** (power)\n"
                "Functions: np.sin(x), np.cos(x), np.exp(x), np.log(x), etc.\n"
                "Examples: x**2, 3*x**2 - 2*x + 1, np.sin(x)"
            )
        

        self.func_help.config(text=help_text)
    def show_func_help_lr(self, event=None):
        help_textx = (
            "Recommendation: 0.025 ± 0.025 → Good rule of thumb\n"
            "Warning: Never go beyond ≥ 1 — overshooting"
        )

        

        self.func_help_lr.config(text=help_textx)

    def hide_func_help(self, event=None):
        self.func_help.config(text="")

    def hide_func_help_lr(self, event=None):
        self.func_help_lr.config(text="")

    def hide_func_help_if_not_focused(self, event=None):
        if self.window.focus_get() != self.func_entry:
            self.hide_func_help()

    def create_button(self):
        self.launch_btn = tk.Button(
            self.window,
            text="Launch",
            font=self.default_font,
            width=15,
            command=self.on_launch
        )
        self.launch_btn.grid(row=7, column=0, padx=self.padding, pady=self.padding * 2)

    def on_launch(self):
        # Retrieve values from entries
        learning_rate = float(self.lr_entry.get())
        starting_point = float(self.sp_entry.get())
        func_string = self.func_entry.get()

        print(f"Learning Rate: {learning_rate}")
        print(f"Starting Point: {starting_point}")
        print(f"Function: {func_string}")
        descent_run(learning_rate, starting_point, func_string)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = InteractiveApp()
    app.run()



