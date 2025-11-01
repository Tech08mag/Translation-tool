import pytesseract as tess
from PIL import Image

def get_text_from_image(img_path: str):
    img = Image.open(img_path)
    text = tess.image_to_string(img)
    return text