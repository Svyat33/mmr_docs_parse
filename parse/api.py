import json
import os

import requests
from dotenv import load_dotenv
from requests import Response

from parse.struct import Document

load_dotenv()
LNK = "https://interes.shtab.net/api/document/detect/"
KEY = os.getenv("RADA_API_KEY")


def send_document(doc: Document) -> Response:
    '''Отправляем документ на распознавание.'''
    return requests.post(LNK, json=json.loads(doc.json()), headers={'AUTHORIZATION': KEY})
