from googletrans import Translator as GoogleTranslator
from utils.logger import Logger

class Translator:
    def __init__(self):
        self.logger = Logger()
        self.logger.info('Initializing translator')
        self.translator = GoogleTranslator()
        self.logger.debug('Google translator initialized')

    def get_available_languages(self):
        self.logger.debug('Getting available languages')
        return [
            "English", "Japanese", "Korean", "Chinese (Simplified)",
            "Spanish", "French", "German", "Italian", "Russian",
            "Portuguese", "Dutch", "Arabic", "Hindi", "Thai"
        ]

    def translate(self, text, source_lang, target_lang):
        try:
            self.logger.info(f'Translating text from {source_lang} to {target_lang}')
            # Convert language names to language codes
            source_code = self._get_language_code(source_lang)
            target_code = self._get_language_code(target_lang)
            
            self.logger.debug(f'Using language codes: {source_code} -> {target_code}')
            result = self.translator.translate(
                text,
                src=source_code,
                dest=target_code
            )
            
            self.logger.debug('Translation completed successfully')
            return result.text
            
        except Exception as e:
            self.logger.error(f'Translation error: {str(e)}')
            raise

    def _get_language_code(self, language_name):
        self.logger.debug(f'Converting language name to code: {language_name}')
        language_codes = {
            "English": "en",
            "Japanese": "ja",
            "Korean": "ko",
            "Chinese (Simplified)": "zh-cn",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Italian": "it",
            "Russian": "ru",
            "Portuguese": "pt",
            "Dutch": "nl",
            "Arabic": "ar",
            "Hindi": "hi",
            "Thai": "th"
        }
        return language_codes.get(language_name, "en") 