from helpers.img import capture
from ocr.img_rec import get_text_from_image_tess
from translation.translation import translateGoogle, translateMymemory


def main():
    capture()
    text: str = get_text_from_image_tess()
    print(translateMymemory(text))

    print(translateGoogle(text))


if __name__ == "__main__":
    main()