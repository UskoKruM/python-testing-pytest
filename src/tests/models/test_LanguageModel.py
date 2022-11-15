# Models
from src.models.LanguageModel import LanguageModel


def test_get_languages_not_none():
    languages = LanguageModel.get_languages()
    assert languages != None


def test_get_languages_has_elements():
    languages = LanguageModel.get_languages()
    assert len(languages) > 0


def test_get_languages_check_elements_length():
    languages = LanguageModel.get_languages()
    for language in languages:
        assert len(language) > 0
