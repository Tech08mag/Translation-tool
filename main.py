from helper.img import capture
from ocr.preprocessing import preprocessing_handler
from translation.translation import translateGoogle, DeeplTranslator
from ocr.img_rec import get_text_from_image_tess


def test_image_quality() -> None:
    capture()
    preprocessing_handler("screenshot.png")

def start() -> str:
    capture()
    preprocessing_handler("screenshot.png")
    text: str = get_text_from_image_tess()
    return translateGoogle(text)