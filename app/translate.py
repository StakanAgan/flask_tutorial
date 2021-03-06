import json
import uuid

import requests
from flask import current_app

from flask_babel import _


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    base_url = 'https://api.cognitive.microsofttranslator.com/'
    path = 'translate?api-version=3.0'
    params = {
        'api-version': '3.0',
        'from': source_language,
        'to': dest_language
    }
    constructed_url = base_url + path

    headers = {
        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': 'northeurope',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = [{
        'text': text
    }]
    response = requests.post(constructed_url, headers=headers, json=body, params=params)
    if response.status_code != 200:
        return _('Error: the translation service failed.')
    return response.json()[0]['translations'][0]['text']


# TODO: encapsulate request logic in method
def detect(text):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    base_url = 'https://api.cognitive.microsofttranslator.com/'
    path = 'detect?api-version=3.0'
    params = {
        'api-version': '3.0',
    }
    constructed_url = base_url + path

    headers = {
        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': 'northeurope',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = [{
        'text': text
    }]
    response = requests.post(constructed_url, headers=headers, json=body, params=params)
    if response.status_code != 200:
        return _('Error: the translation service failed.')
    return response.json()[0]['language']
