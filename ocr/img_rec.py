from helpers.json_actions import read_json


from paddleocr import PaddleOCR
import pytesseract as tess
from PIL import Image


ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False)


def get_text_from_image_tess():
    img_path = read_json("settings.json", "screenshot_name")
    img = Image.open(img_path)
    lang: str = read_json("settings.json", "content_lang")
    text = tess.image_to_string(img, lang=lang)
    return text


def get_text_from_image_paddle():
    img_path = read_json("settings.json", "screenshot_name")
    return ocr.predict(img_path)