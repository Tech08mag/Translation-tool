import pyautogui
from pynput import keyboard
from translations import translate
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("400x240")

def on_key_press(key):
  if hasattr(key, "char") and key.char == "^":
    pyautogui.screenshot('image.png')
    translate("image.png", 2, "eng", "english", "german")



keyboard_listener = keyboard.Listener(on_press=on_key_press)
keyboard_listener.start()
app.mainloop()