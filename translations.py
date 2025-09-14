from deep_translator import GoogleTranslator
from textblob import TextBlob
from ollama import generate


from image_manipulation import preproccessImage, getTextfromImage


def googleTranslate(text: str, sourcelng: str, targetlng: str):
    translated = GoogleTranslator(source='auto', target='de').translate(text=text)
    return translated

def correct_text_ollama(text: str):
    response = generate('llama3.1:8b', f'Correct the following text and remove the random characters, dont make things up! without telling me. return the text without anything else that include any type of notification) Keep in mind in the text are persons included who say something, DOnt make things up: {text}')
    return response["response"]

def correct_gramma_ollama(text: str, inputlanguage: str, outputlanguage: str):
    response = generate('zongwei/gemma3-translator:4b', f"Transalte this text from {inputlanguage} to {outputlanguage}(only return the translated text without anything else): {text}")
    return response["response"]

def correct_spelling(text:str):
    words = text.split()
    corrected_words = []
    newstring = ""
    for i in words:
        corrected_words.append(TextBlob(i))
    for i in corrected_words:
        newstring = newstring + str(i.correct()) + " "
    return newstring


def translate(img: str, translation_option: int, sourcelang: str, inputlanguage:str, outputlanguage: str):
    """1 for AI, 2 for google translate"""
    preproccessImage(img)
    text = getTextfromImage("image.png", sourcelang=sourcelang)
    print(text)
    text = correct_text_ollama(text)
    print(text)
    if translation_option == 1:
        return(correct_gramma_ollama(text, inputlanguage, outputlanguage))
    else:
        return(googleTranslate(text, sourcelang, outputlanguage))