from main import start

import tkinter as tk
from tkinter import Label
import json
from PIL import ImageTk, Image

class TranslationToolGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.settings = self._load_json("settings.json")
        self.options = self._load_json("options.json")
        self.settings_entries = {}
        self._init_window()
        self._create_settings_frame()
        self._create_save_button()
        self.create_test_button()
        self._create_start_button()
        

    def _load_json(self, filename):
        with open(filename, "r") as f:
            return json.load(f)

    def _init_window(self):
        self.window.configure(bg="lightblue")
        self.window.title("Translation Tool")
        self.window.geometry("400x500")
        self.window.iconphoto(False, tk.PhotoImage(file="data/speichern_vergessen.png"))
        self.window.bind("<Control-Shift-Escape>", lambda e: self.window.quit())
        self.window.bind("<Control-t>", lambda e: self._start())
        self.window.bind("<F5>", lambda e: self._test())

    def _create_settings_frame(self):
        self.settings_frame = tk.Frame(self.window, padx=10, pady=10, background="blue")
        self.settings_frame.pack(fill=tk.BOTH)
        self._create_settings_entries()

    def _create_settings_entries(self):
        for row, (key, value) in enumerate(self.settings.items()):
            self._create_setting_row(row, key, value)

    def _create_setting_row(self, row, key, value):
        label = tk.Label(self.settings_frame, text=f"{key}:", bg="blue", fg="orange")
        label.grid(row=row, column=0, sticky="w", pady=5)

        if isinstance(value, bool):
            var = tk.BooleanVar(value=value)
            entry = tk.Checkbutton(self.settings_frame, variable=var)
        else:
            var = tk.StringVar(value=str(value))
            entry = tk.Entry(self.settings_frame, textvariable=var)

        entry.grid(row=row, column=1, sticky="ew", pady=5)
        self.settings_entries[key] = var

    def _create_save_button(self):
        save_button = tk.Button(
            self.window, text="Save Settings", command=self._save_settings
        )
        save_button.pack(pady=10)

    def _save_settings(self):
        new_settings = {key: var.get() for key, var in self.settings_entries.items()}
        with open("settings.json", "w") as f:
            json.dump(new_settings, f, indent=4)

    def _create_start_button(self):
        start_button = tk.Button(self.window, text="Start", command=self._start)
        start_button.pack(pady=10)

    def _start(self):
        text_window = tk.Toplevel(self.window)
        text_window.title("Translation Output")
        text_window.geometry("320x240")
        text_window.grid_rowconfigure(0, weight=1)
        text_window.grid_columnconfigure(0, weight=1)
        text: str = start()
        text_label = tk.Label(text_window, text=text)
        text_label.pack(padx=10, pady=10)

    def create_test_button(self):
        test_button = tk.Button(self.window, text="Test", command=self._test)
        test_button.pack(pady=10)

    def _test(self):
        start()
        img_window = tk.Toplevel(self.window)
        img_window.title("Screenshot Preview")
        img_window.geometry("320x240")
        

        img = self._load_json("settings.json")["screenshot_name"]
        img = Image.open(img)
        img = ImageTk.PhotoImage(img)
        panel = Label(img_window, image=img)
        panel.image = img
        panel.pack(expand=True, padx=10, pady=10)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = TranslationToolGUI()
    app.run()
