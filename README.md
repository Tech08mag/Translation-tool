# Translation Tool

## Content:
- [Requirements](#requirements) 
- [To Do](#to-do)
- [Features](#features)
    - [Translators](#translators)
- [Setup](#setup):
    - [Linux](#linux)
    - [Windows](#windows)
    - [Options and Tuneing](#options-and-tuneing)
-[Testing](#testing)
- [Ressources](#ressources)
- [Credits](#credits)


## Requirements:
- https://github.com/tesseract-ocr/tesseract


## To Do
- [ ] Installation/Setup Script Windows
- [ ] German Readme
- [ ] write a setup guide
- [ ] add [Libre Translate](https://github.com/LibreTranslate/LibreTranslate) integration
- [ ] add [EasyNMT](https://github.com/UKPLab/EasyNMT)
- [ ] add [paddleOCR](https://github.com/PaddlePaddle/PaddleOCR) as an pytesseract alternative


## Features
### Translators:
- [x] Google Translate integration
- [x] Mymemory Translator (One Request has a character Limit of 500)
- [x] (Not tested!) DeepL Translator integration (require [Api Token](https://developers.deepl.com/docs/getting-started/intro))
- [X] (Not tested!) Yandex Translator integration (require [Api Token](https://yandex.cloud/en/docs/translate/operations/sa-api-key))

## Key Binds
- [X] Control + Shift + Escape to quit
- [X] Control + t to start translating
- [X] F5 to test the image quality after preprocessing

- [x] Image preprocessing for better accurency

## Setup:
### Linux:
1. Install tesseract-ocr
```sh
sudo apt install tesseract-ocr
```

2. Run the Program
```sh
uv run gui.py
```

### Windows:

## testing
```sh
chmod +x test.sh
```

```sh
./test.sh
```

## Credits:
Idea & test data: octronix\
Supported by the ["Speichern Vergessen Community"](https://discord.gg/mnzyJECkdS)

Libarys & Software:
- GUI:
    - [Tkinter](https://docs.python.org/3/library/tkinter.html)
- OCR:   
    - [tesseract](https://github.com/tesseract-ocr/tesseract)

- Translation:
    - [deep-translator](https://github.com/nidhaloff/deep-translator)

- Screen Capture:
    - [python-mss](https://github.com/BoboTiG/python-mss)