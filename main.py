from helpers.img import capture
from ocr.img_rec import get_text_from_image
from translation.translation import translate


def main():
    capture(1)
    text: str = get_text_from_image("screenshot.png")
    print(translate(text, "en", "de"))


if __name__ == "__main__":
    main()