from deep_translator import GoogleTranslator
from utils.logger import Logger

class Translator:
    def __init__(self):
        self.logger = Logger()
        self.logger.info('Initializing translator')
        self.logger.debug('Deep translator initialized')

    def get_available_languages(self):
        self.logger.debug('Getting available languages')
        return [
            "Auto Detect",
            "English",
            "Japanese",
            "Korean",
            "Chinese (Simplified)",
            "Chinese (Traditional)",
            "Spanish",
            "French",
            "German",
            "Italian",
            "Russian",
            "Portuguese",
            "Dutch",
            "Arabic",
            "Hindi",
            "Thai",
            "Vietnamese",
            "Indonesian",
            "Malay",
            "Filipino",
            "Turkish",
            "Greek",
            "Polish",
            "Ukrainian",
            "Romanian",
            "Hungarian",
            "Czech",
            "Swedish",
            "Danish",
            "Finnish",
            "Norwegian",
            "Hebrew",
            "Persian",
            "Bengali",
            "Urdu",
            "Punjabi"
        ]

    def translate(self, text, source_lang, target_lang):
        try:
            self.logger.info(f'Translating text from {source_lang} to {target_lang}')
            # Convert language names to language codes
            source_code = self._get_language_code(source_lang)
            target_code = self._get_language_code(target_lang)
            
            self.logger.debug(f'Using language codes: {source_code} -> {target_code}')
            translator = GoogleTranslator(source=source_code, target=target_code)
            result = translator.translate(text)
            
            self.logger.debug('Translation completed successfully')
            return result
            
        except Exception as e:
            self.logger.error(f'Translation error: {str(e)}')
            raise

    def _get_language_code(self, language_name):
        self.logger.debug(f'Converting language name to code: {language_name}')
        language_codes = {
            "Auto Detect": "auto",
            "English": "en",
            "Japanese": "ja",
            "Korean": "ko",
            "Chinese (Simplified)": "zh-CN",
            "Chinese (Traditional)": "zh-TW",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Italian": "it",
            "Russian": "ru",
            "Portuguese": "pt",
            "Dutch": "nl",
            "Arabic": "ar",
            "Hindi": "hi",
            "Thai": "th",
            "Vietnamese": "vi",
            "Indonesian": "id",
            "Malay": "ms",
            "Filipino": "tl",
            "Turkish": "tr",
            "Greek": "el",
            "Polish": "pl",
            "Ukrainian": "uk",
            "Romanian": "ro",
            "Hungarian": "hu",
            "Czech": "cs",
            "Swedish": "sv",
            "Danish": "da",
            "Finnish": "fi",
            "Norwegian": "no",
            "Hebrew": "he",
            "Persian": "fa",
            "Bengali": "bn",
            "Urdu": "ur",
            "Punjabi": "pa"
        }
        return language_codes.get(language_name, "en") 