from helpers.img import capture
from ocr.img_rec import get_text_from_image_tess, get_text_from_image_paddle
from translation.translation import translateGoogle, translateMymemory, translateDeepL


def main():
    capture()
    text: str = get_text_from_image_tess()
    
    print(translateMymemory(text))

    print(translateGoogle(text))
    print(translateDeepL("lol"))


if __name__ == "__main__":
    main()