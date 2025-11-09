from helper.json_actions import read_json

from deep_translator import GoogleTranslator, MyMemoryTranslator, DeeplTranslator, YandexTranslator


def translateGoogle(msg: str):
    source_lang: str = read_json("settings.json", "source_lang_google")
    if source_lang == "":
        source_lang = "auto"
    target_lang: str = read_json("settings.json", "target_lang_google")
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    return translator.translate(msg)


def translateMymemory(msg: str):
    source_lang: str = read_json("settings.json", "source_lang_google")
    if source_lang == "":
        source_lang = "auto"
    target_lang: str = read_json("settings.json", "target_lang_google")
    return MyMemoryTranslator(source=source_lang, target=target_lang).translate(msg)


def translateDeepL(msg: str):
    api_token: str = read_json("settings.json", "deepl_api_token")
    use_free_api: bool = read_json("settings.json",  "use_free_api")
    source_lang: str = read_json("settings.json", "source_lang_google")
    target_lang: str = read_json("settings.json", "target_lang_google")
    return DeeplTranslator(api_key=api_token, source=source_lang, target=target_lang, use_free_api=use_free_api).translate(msg)


def translateYandex(msg: str):
    api_token: str = read_json("settings.json", "yandex_api_token")
    source_lang: str = read_json("settings.json", "source_lang_google")
    target_lang: str = read_json("settings.json", "target_lang_google")
    return YandexTranslator(api_token).translate(msg, source=source_lang, target=target_lang)
