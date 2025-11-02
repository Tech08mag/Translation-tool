# Translation Tool

## Content:
- [Requirements](#requirements) 
- [To Do](#to-do)
- [Features](#features)
    - [Translators](#translators)
- [Setup](#setup):
    - [Linux](#linux)
    - [Windows](#windows)
- [Ressources](#ressources)
- [Credits](#credits)


## Requirements:
- https://github.com/tesseract-ocr/tesseract
- https://github.com/PaddlePaddle/PaddleOCR?tab=readme-ov-file
- [Installation Guide](https://www.paddlepaddle.org.cn/en/install/quick?docurl=undefined)


## To Do
- [ ] GUI
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


## Setup:
### Linux:
1. Install tesseract-ocr
```sh
sudo apt install tesseract-ocr
```

2. Run the Program
```sh
uv run main.py
```

### Windows:

## Ressources:
- 
## Credits:
Idea & test data: octronix\
Supported by the ["Speichern Vergessen Community"](https://discord.gg/mnzyJECkdS)

Libarys & Software:
- GUI:
    - [NiceGUI](https://nicegui.io/)
- OCR:   
    - [tesseract](https://github.com/tesseract-ocr/tesseract)

- Translation:
    - [deep-translator](https://github.com/nidhaloff/deep-translator)

- Screen Capture:
    - [python-mss](https://github.com/BoboTiG/python-mss)