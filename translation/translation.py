from deep_translator import GoogleTranslator

def translate(msg: str, source_lang: str, target_lang: str):
    langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
    print(langs_dict)
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    return translator.translate(msg)