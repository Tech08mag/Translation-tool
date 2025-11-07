from helpers.json_actions import read_json


import pytesseract as tess
from PIL import Image


def get_text_from_image_tess():
    img_path = read_json("settings.json", "screenshot_name")
    img = Image.open(img_path)
    lang: str = read_json("settings.json", "content_lang")
    text = tess.image_to_string(img, lang=lang)
    return text
