import base64
from enum import Enum
from typing import Dict, Any, Union

from pydantic import BaseModel, HttpUrl, PydanticTypeError, constr


class Base64Error(PydanticTypeError):
    msg_template = 'base64 type expected'


class Base64(str):
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type='byte', format='base64')

    @classmethod
    def __get_validators__(cls) -> 'CallableGenerator':
        # included here and below so the error happens straight away
        from pydantic.validators import bytes_validator
        yield bytes_validator
        yield cls.validate

    @classmethod
    def validate(cls, value: Union[str]) -> str:
        try:
            if base64.b64encode(base64.b64decode(value)) == value:
                return value
        except:
            raise Base64Error


class ExtensionsEnum(str, Enum):
    '''Доступные расширения файла'''
    txt = 'txt'
    doc = 'doc'
    docx = 'docx'
    pdf = 'pdf'


class Document(BaseModel):
    '''Структура описывающая формат принемаемый API'''
    title: constr(min_length=1, max_length=1024)  # назва документа
    link: HttpUrl  # посилання на документ на сайте міськради
    file_content: Base64  # зміст документа в Base64 формате.
    file_type: ExtensionsEnum
