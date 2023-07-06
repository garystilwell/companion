from langcodes import Language, find
from google.cloud import translate_v2
from google.oauth2.service_account import Credentials

translate_client = translate_v2.Client()


def init_language(credentials: Credentials):
    global translate_client
    translate_client = translate_v2.Client(credentials=credentials)


def translate(text, to) -> str:
    result = translate_client.translate(text, target_language=to, format_="html")
    return result["translatedText"]


def detect_language(text: str) -> str:
    return translate_client.detect_language(text)["language"]


def is_text_of_language(text: str, language_code: str) -> bool:
    return detect_language(text) == language_code


def language_name_to_iso6391(language_name):
    return find(language_name).language


def iso6391_to_language_name(language_code, name_in_same_language=False):
    display_lang = language_code if name_in_same_language else "en"
    return Language.get(language_code).display_name(display_lang)


def locale_code_to_language(locale_code, name_in_same_language=False):
    display_lang = locale_code.split('-')[0] if name_in_same_language else "en"
    return Language.get(locale_code).display_name(display_lang).title()
