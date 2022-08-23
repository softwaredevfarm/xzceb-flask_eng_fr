'''
Translator
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#print(language_translator.list_identifiable_languages().get_result())

def englishToFrench(englishText):
    '''
    Converts text from eng to french
    '''
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def frenchToEnglish(frenchText):
    '''
    Converts text from french to eng
    '''
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text


