from helpers.img import capture
from ocr.img_rec import get_text_from_image_tess
from translation.translation import translate


def main():
    capture()
    text: str = get_text_from_image_tess()
    print(translate(text, "en", "de"))


if __name__ == "__main__":
    main()