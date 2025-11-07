from helpers.img import capture
from ocr.preprocessing import preprocessing_handler

from ocr.img_rec import get_text_from_image_tess
from translation.translation import translateGoogle, PonsTranslator


def main():
    capture()
    preprocessing_handler("screenshot.png")
    text: str = get_text_from_image_tess()
    print(PonsTranslator(text))


if __name__ == "__main__":
    main()