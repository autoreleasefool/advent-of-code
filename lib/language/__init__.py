from lib.language.language_helper import LanguageHelper as _LanguageHelper
from lib.language.language_id import LanguageID as _LanguageID
from lib.language.python_helper import PythonHelper as _PythonHelper

LanguageHelper = _LanguageHelper
LanguageID = _LanguageID
PythonHelper = _PythonHelper


def language_helper(language: LanguageID) -> LanguageHelper:
    if language == LanguageID.PYTHON:
        return PythonHelper()
